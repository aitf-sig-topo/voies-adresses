#!/bin/bash

# Vérifier la version de Python
python_version=$(python --version 2>&1 | awk '{print $2}')
required_major_version="3"
required_minor_version="11"

# Extraire les versions majeures et mineures
installed_major_version=$(echo $python_version | cut -d. -f1)
installed_minor_version=$(echo $python_version | cut -d. -f2)

if [ "$installed_major_version" -ne "$required_major_version" ] || [ "$installed_minor_version" -ne "$required_minor_version" ]; then
    echo "Erreur : La version de Python requise est $required_major_version.$required_minor_version.x, mais la version actuelle est $python_version."
    exit 1
else
    echo "python $required_major_version.$required_minor_version trouvé"
    echo ""
fi

# Créer un environnement virtuel
python -m venv .venv

# Vérifier si le script est exécuté sous Windows
if [ -n "$WINDIR" ] || [ -n "$MSYSTEM" ]; then
    echo "on est sous windows"
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# upgrade pip
python -m pip install --upgrade pip

# Installer les dépendances et lister les packages installés
python -m pip install -r requirements.txt
python -m pip list

# Désactiver l'environnement virtuel
deactivate
