
# Explication des expressions régulières utilisées pour les contraintes

## uid_adresse

* un identifiant d'adresse '@a:' suivi d'un UUIDv4
* un identifiant de voie / toponyme '@v:' précédé 'un espace et suivi d'un UUIDv4
* un identifiant de commune '@c:' précédé 'un espace et suivi d'un UUIDv4

Exemple de valeur :
`@a:fe09df05-3da5-4799-9e3a-0a5709657e4a @v:c082ad89-cf14-4944-8f6f-e1d0947b92c8 @c:3647a1f3-8909-4aee-b7a4-ed1a8598302f`

Ce qui donne : 
`((@a:(\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12})) )?(@v:(\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12})) (@c:(\\w{8}-\\w{4}-\\w{4}-\\w{4}-\\w{12}))`


## cle_interop

Concaténation des éléments suivants, séparés par un "_", en minuscules

* code INSEE
* code de voie FANTOIR
* numéro
* suffixe

Exemple de valeur :
`35250_1658_00021_bis_a`

Ce qui donne : 
`([0-9]{5})_(([aA-zZ]{1}|[0-9]{1})[0-9]{3})_([0-9]{5})(_([a-z0-9]*))?(_[a-z0-9]*)?`


## commune_insee, commune_deleguee_insee

Code INSEE de la commune : 5 chiffres.

Ce qui donne : 
`[0-9]{5}`


## commune_nom, commune_deleguee_nom

Un nom supportant les signes diacritiques et certains caractères séparateurs.

### Cas général

`^([A-Za-zÀ-ÖØ-öø-ÿœŒâ' \-\(\)]+)$`

Exemples de valeur :

Ambléon
Château
Bidule (ville)
Bédeaây
Château-Fort
Château-Chinon (Ville)
Petit-Cœur
Rennes

### PLM à cause des numéros d'arrondissement

`((Paris|Lyon|Marseille) [1-9][0-9]?er? Arrondissement)`

Marseille 1er Arrondissement
Paris 19e Arrondissement
Lyon 4e Arrondissement


### Combinaison

`((Paris|Lyon|Marseille) [1-9][0-9]?er? Arrondissement)|(([A-Za-zÀ-ÖØ-öø-ÿœŒâ' \-\(\)]+))`


## voie_nom, lieudit_complement_nom

Un nom supportant les signes diacritiques et certains caractères (cas à recenser).


## Coordonnées X et Y

Coordonnées métriques du RGF93. 2 Décimales maximum.

Exemple de valeur :
`6775712.50`

Ce qui donne : 
`-?[0-9]{1,7}.[0-9]{1,2}`

Note : il est compliqué de rejeté des "0" terminaux"


## Coordonnées long et lat

Exemple de valeur :
`47.9929891`

Ce qui donne : 
`-?[0-9]{1,2}.[0-9]{1,7}`


## cad_parcelles

Une liste de parcelles au format complet (y compris le code de direction). Chaque code de parcelle est séparé par un pipe. Ler dernier motif est donc optionnel et peut se répéter.

Exemple de valeur : 
`350088000AB0137|350088000AB0138`

Ce qui donne : 
`([0-9]{9}[0-9A-Z]{2}[0-9]{4})(?:\\|([0-9]{9}[0-9A-Z]{2}[0-9]{4}))*`



