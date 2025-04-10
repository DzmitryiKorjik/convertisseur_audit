# Convertisseur CSV en Excel

## Ce projet Django permet de convertir un fichier .txt ou .csv avec des données séparées par des pipes (|) en un fichier Excel .xlsx. L'application prend en charge les encodages courants et permet à l'utilisateur de télécharger le fichier converti directement depuis le navigateur.

## Prérequis

- Python 3.x
- Django 5.x
- Pandas
- XlsxWriter
- Chardet (pour la détection automatique de l'encodage)

## 📦 Installation

### Étape 1 : Cloner le projet

1. Clone ce projet dans ton répertoire local en utilisant git :

    ```bash
    git clone https://github.com/ton-utilisateur/convertisseur-csv-en-excel.git
    ```

### Étape 2 : Créer un environnement virtuel

2. Crée un environnement virtuel pour isoler les dépendances du projet :

    ```bash
    cd convertisseur-csv-en-excel
    python -m venv env
    ```

### Active l'environnement virtuel :

- Sur Windows :

    ```bash
    source env\Scripts\activate
    ```

- Sur Mac/Linux :

    ```bash
    source env/bin/activate
    ```

### Étape 3 : Installer les dépendances

3. Installe les bibliothèques nécessaires avec pip :

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Lancer le projet

## 🛠️ Structure du projet

```
convertisseur_project/
│
├── convertisseur_app/          # Application principale
│   ├── migrations/             # Dossier de migrations de base de données
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                # Formulaire pour télécharger un fichier
│   ├── models.py
│   ├── tests.py
│   ├── views.py                # Logique de conversion
│   └── templates/
│       └── convertisseur_app/
│           └── index.html      # Template principal
│
├── convertisseur_project/      # Dossier du projet Django
│   ├── __init__.py
│   ├── settings.py             # Paramètres du projet
│   ├── urls.py                 # Routes du projet
│   ├── asgi.py
│   └── wsgi.py
│
├── env/                        # Environnement virtuel
│
├── manage.py                   # Fichier principal pour gérer le projet
└── requirements.txt            # Liste des dépendances du projet

```

