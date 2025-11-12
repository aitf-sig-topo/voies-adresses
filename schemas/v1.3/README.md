# Format Base Adresse Locale version 1.3

## Explication du fichier d'exemple `BAL simple`


Les lignes 2 à 18 décrivent des **adresses sur un toponyme dénommé**, en l'occurence, une rue.

```
1 Rue de Chanteloup
2 Rue de Chanteloup
3 Rue de Chanteloup
...
```

La ligne 6 est une **adresse simple avec un suffixe d'adresse**.

```
5 bis Rue de Chanteloup
```

Les lignes 14 15 et 16 sont également des adresses simples avec des suffixes :

```
12 A Rue de Chanteloup
12 B Rue de Chanteloup
12 C Rue de Chanteloup
```

Les lignes 11 et 12 décrivent une **adresse multiposition** soit une seule adresse avec une seule clé d'interopérabilité mais 2 positions différentes.

```
35088_0010_00010 | 10 Rue de Chanteloup | parcelle
35088_0010_00010 | 10 Rue de Chanteloup | bâtiment
```

Les lignes 19 à 21 décrivent des **toponymes sans adresse**. Ici, des ronds-ponts dénommés. Le numéro de l'adresse est donc forcé à '99999'.

```
99999 | Rond-point de la Lande du Feu
99999 | Rond-point de Radeux
99999 | Rond-point des Grands Sillons
```

Les lignes 22 à 25 décrivent un **toponyme adressé**, en l'occurence un  lieu-dit.

```
10 la Chênaie
12 la Chênaie
14 la Chênaie
12 la Chênaie
```

La ligne 26 décrit un **toponyme sans adresse**. Ici, un lieu-dit. Le numéro de l'adresse est donc forcé à '99999'.

```
99999 | le Chêne Hervé
```


## Explication du fichier d'exemple `BAL multilingue`

TODO

