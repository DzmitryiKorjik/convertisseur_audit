import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import io

# Liste d'encodages qu'on va essayer
ENCODINGS = ['cp1252', 'ISO-8859-1', 'utf-8-sig', 'utf-16', 'latin1']

def convertir_fichier(request):
    erreur = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']
            contenu = fichier.read()
            fichier.seek(0)

            df = None
            for enc in ENCODINGS:
                try:
                    # Essayer de lire avec une des encodages possibles
                    df = pd.read_csv(io.BytesIO(contenu), sep="|", decimal=",", encoding=enc)
                    print(f"✅ Encodage utilisé: {enc}")
                    break
                except Exception as e:
                    continue

            if df is None:
                erreur = "Erreur : impossible de lire le fichier avec les encodages connus."
            else:
                try:
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='Feuille1')
                    output.seek(0)

                    response = HttpResponse(output.read(),
                                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                    response['Content-Disposition'] = 'attachment; filename=tableau_converti.xlsx'
                    return response
                except Exception as e:
                    erreur = f"Erreur lors de la conversion : {str(e)}"
    else:
        form = UploadFileForm()

    return render(request, 'convertisseur_app/index.html', {'form': form, 'erreur': erreur})
