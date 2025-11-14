
import sys
import argparse
from argparse import RawTextHelpFormatter
import logging

from frictionless import validate, Schema
import json

# ====================================================================================================================
# ====================================================================================================================

def load_schema(schema_path):
    """Charge le schéma depuis un fichier JSON."""
    # schema_path = 'v1.3/test.json'

    with open(schema_path, 'r', encoding='utf-8') as schema_file:
        schema_data = json.load(schema_file)
    # logging.info(f"Schéma chargé : {schema_data}")  # Impression de débogage
    return Schema(descriptor=schema_data)


def validate_csv(csv_path, schema, header_only=False):
    """Valide un fichier CSV par rapport à un schéma donné."""

    report = validate(csv_path, schema=schema, limit_rows=1 if header_only else 0)
    return report


# =====================================================================================================================

def main(csv_path, version, header_only):
    """Fonction principale pour exécuter la validation."""
    
    logging.info(f"Exécution de la validation avec la version {version}...")
    schema_path = f"v{version}/bal_schema_v{version}.json"
    schema = load_schema(schema_path)

    # Impression des premières lignes du CSV pour vérification
    # with open(csv_path, 'r') as csv_file:
    #     lines = csv_file.readlines()
    #     logging.info("Premières lignes du CSV :")
    #     for line in lines[:5]:  # Imprime les 5 premières lignes
    #         logging.info(line.strip())

    report = validate_csv(csv_path, schema, header_only)

    # Chemin du fichier d'erreurs
    error_file_path = f"{csv_path}_erreurs.txt"

    if report.valid:
        logging.info("Le fichier est valide.")
        with open(error_file_path, 'w') as error_file:
            error_file.write("Le fichier est valide. Aucune erreur trouvée.\n")
    else:
        logging.info("Le fichier contient des erreurs :")
        with open(error_file_path, 'w') as error_file:
            error_file.write("Le fichier contient les erreurs suivantes :\n")
            for table in report.tasks:
                if table.errors:
                    for error in table.errors:
                        row_position = getattr(error, 'rowPosition', 'N/A')
                        error_message = f"Erreur à la ligne {row_position}: {error.message}\n"
                        logging.info(error_message)
                        error_file.write(error_message)

if __name__ == "__main__":
    # Configuration des arguments de ligne de commande

    parser = argparse.ArgumentParser(description="""

    Ce script permet de valider un fichier Base Adresse Local (BAL)
    selon un schéma adapté à une version du format BAL.

    Exemple : validateur_bal.py --version 1.3 v1.3/bal_simple_v1.3.csv

    """, formatter_class=RawTextHelpFormatter)

    parser.add_argument('--version', type=str, required=True, help="Version du script (ex : 1.3, 1.4, 1.5)")
    parser.add_argument('bal', type=str, help="Chemin vers le fichier CSV à valider")
    parser.add_argument('--header-only', action='store_true', help="Valider uniquement la ligne d'en-tête du CSV")

    # Analyse des arguments
    args = parser.parse_args()

    if '--help' in sys.argv:
        parser.print_help()
        sys.exit(0)

    # =========================================
    # configuration du logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
    )

    # =========================================
    # Exécution de la fonction principale avec les arguments
    main(args.bal, args.version, args.header_only)
