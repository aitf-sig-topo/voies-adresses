# Format Base Adresse Locale version 1.4

## Explication du fichier d'exemple `BAL simple`


Les lignes 2 à 18 décrivent des **adresses sur un toponyme adressé**, en l'occurence, une rue.

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

Les lignes 11 et 12 décrivent une **adresse multiposition** soit une seule adresse avec des identifiants identiques et une clé d'interopérabilité également indetique mais 2 positions différentes.

```
3656a1f3-8909-4aee-b7a4-ed1a8598302f | c082ad89-cf14-4944-8f6f-e1d0947b92c8 | 09bcecd7-7f4f-4653-84d6-d2552c089b90 | 10 Rue de Chanteloup | parcelle
3656a1f3-8909-4aee-b7a4-ed1a8598302f | c082ad89-cf14-4944-8f6f-e1d0947b92c8 | 09bcecd7-7f4f-4653-84d6-d2552c089b90 | 10 Rue de Chanteloup | entrée
```

Les lignes 19 à 21 décrivent des **toponymes sans adresse**. Ici, des ronds-points dénommés. Le numéro de l'adresse est donc forcé à '99999'. On aura donc un identifiant BAN de commune, de toponyme mais PAS d'identifiant d'adresse.

```
3664a1f3-8909-4aee-b7a4-ed1a8598302f | 82ba4dfc-e936-4336-9559-5d8254d104b1 | {NULL} | 99999 | Rond-point de la Lande du Feu
3664a1f3-8909-4aee-b7a4-ed1a8598302f | 16fb1a8c-4c23-40a2-95af-14a4612f8d89 | {NULL} | 99999 | Rond-point de Radeux
3664a1f3-8909-4aee-b7a4-ed1a8598302f | c2831d7d-5fff-4688-aa71-906092e3065d | {NULL} | 99999 | Rond-point des Grands Sillons
```

Les lignes 22 à 25 décrivent un **toponyme adressé**, en l'occurence un  lieu-dit.

```
3667a1f3-8909-4aee-b7a4-ed1a8598302f | cb155c1b-b1af-47ca-8984-e134b580200e | cbd13dc0-cb0f-4c26-a3d0-6716d8e82151 | 10 | la Chênaie
3668a1f3-8909-4aee-b7a4-ed1a8598302f | cb155c1b-b1af-47ca-8984-e134b580200e | 8c695b66-6baf-4ad7-acd5-16fd6e02b25f | 12 | la Chênaie
3669a1f3-8909-4aee-b7a4-ed1a8598302f | cb155c1b-b1af-47ca-8984-e134b580200e | a9ba1d58-035c-44c4-a9ee-15e752aaba95 | 14 | la Chênaie
3670a1f3-8909-4aee-b7a4-ed1a8598302f | cb155c1b-b1af-47ca-8984-e134b580200e | 626a7e75-8178-4e82-bd86-966f5027fdb1 | 16 | la Chênaie

```

La ligne 26 décrit un **toponyme sans adresse**. Ici, un lieu-dit. Le numéro de l'adresse est donc forcé à '99999'.

```
3664a1f3-8909-4aee-b7a4-ed1a8598302f | 1c62879e-9b47-4364-af13-5b8d1105c1f1| {NULL} | 99999 | Chêne Hervé
```


## Explication du fichier d'exemple `BAL multilingue`

TODO

