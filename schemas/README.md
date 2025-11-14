
# Schémas de données du format Base Adresse Locale (BAL)

## Description

Le travail réalisé ici par les ingénieurs territoriaux de France vise à alimenter le [Référentiel des schémas de données publiques](https://schema.data.gouv.fr/).

Chaque schéma de données utilise le formalisme "[Table Schema](https://specs.frictionlessdata.io/table-schema/)" qui est réclamé par le référentiel des schémas de données publiques.


## Organisation

Ce répertoire contient un sous-répertoire par version du format Base Adresse Locale (BAL).

Chaque répertoire d'une version comporte :

* un fichier JSON "Table Schema"
* un fichier CSV exemple pour une BAL simple
* un fichier CSV exemple pour une BAL multilingue


Le fichier JSON qui décrit la structure d'un fichier BAL dans le formalisme "Table Schema".
Le fichier de schéma contient également un certain nombre de contrôle sur les données, exprimés sous la forme d'[expressions régulières](explication_des_regex.md).


## Validateur

Un validateur écrit en Python est disponible pour tester un fichier BAL selon le formalisme Table Schema.

Lancer le script `install.sh` pour configurer un environnement Python adéquat puis lancer le script comme ceci :

```bash
python validateur_bal.py --version {version} {chemin_vers_une_bal.csv}
```

Si le fichier contient des erreurs, celles-ci apparaîtront dans la console, en plus d'un fichier d'erreurs qui sera créé à côté du fichier CSV.


## Limites

La spécification BAL contient es subtilités qui ne peuvent être décrites dans le formalisme Table Schema.
Le validateur peut donc laisser passer beaucoup d'erreurs réelles mais pas de conformité à la spécification.

Le suffixe n'est pas testé.


## Ressources

https://guides.data.gouv.fr/guides-open-data/guide-qualite/maitriser-les-schemas-de-donnees

https://specs.frictionlessdata.io/table-schema/

