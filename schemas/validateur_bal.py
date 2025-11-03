import argparse
import json
import sys
from frictionless import validate, Schema

def load_schema(schema_path):
    """Charge le schéma depuis un fichier JSON."""
    with open(schema_path, 'r') as schema_file:
        schema_data = json.load(schema_file)
    print(f"Schéma chargé : {schema_data}")  # Impression de débogage
    return Schema(descriptor=schema_data)

def validate_csv(csv_path, schema, header_only=False):
    """Valide un fichier CSV par rapport à un schéma donné."""
    report = validate(csv_path, schema=schema, limit_rows=1 if header_only else 0)
    return report

def main(csv_path, version, header_only):
    """Fonction principale pour exécuter la validation."""
    print(f"Exécution de la validation avec la version {version}...")
    schema_path = f"v{version}/bal_schema_v{version}.json"
    schema = load_schema(schema_path)

    # Impression des premières lignes du CSV pour vérification
    with open(csv_path, 'r') as csv_file:
        lines = csv_file.readlines()
        print("Premières lignes du CSV :")
        for line in lines[:5]:  # Imprime les 5 premières lignes
            print(line.strip())

    report = validate_csv(csv_path, schema, header_only)

    # Chemin du fichier d'erreurs
    error_file_path = f"{csv_path}_erreurs.txt"

    if report.valid:
        print("Le fichier est valide.")
        with open(error_file_path, 'w') as error_file:
            error_file.write("Le fichier est valide. Aucune erreur trouvée.\n")
    else:
        print("Le fichier contient des erreurs :")
        with open(error_file_path, 'w') as error_file:
            error_file.write("Le fichier contient les erreurs suivantes :\n")
            for table in report.tasks:
                if table.errors:
                    for error in table.errors:
                        row_position = getattr(error, 'rowPosition', 'N/A')
                        error_message = f"Erreur à la ligne {row_position}: {error.message}\n"
                        print(error_message)
                        error_file.write(error_message)

if __name__ == "__main__":
    # Configuration des arguments de ligne de commande
    parser = argparse.ArgumentParser(description="Valider un fichier CSV avec un schéma.")
    parser.add_argument('--version', type=str, required=True, help="Version du script (e.g., 1.3, 1.4, 1.5)")
    parser.add_argument('bal', type=str, help="Chemin vers le fichier CSV à valider")
    parser.add_argument('--header-only', action='store_true', help="Valider uniquement la ligne d'en-tête du CSV")

    # Analyse des arguments
    args = parser.parse_args()

    # Exécution de la fonction principale avec les arguments
    main(args.bal, args.version, args.header_only)
