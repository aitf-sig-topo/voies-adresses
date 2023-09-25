# Générer de l'UUID v4

## Contexte

La Base Adresse Nationale a retenu le format UUID v4 pour le format de ses identifiants.

Ci-dessous quelques aides pour comprendre et générer des UUID v4.


## Bases de données

### PostgreSQL

Il s'agit d'une librairie native mais il faut installer l'extension `uuid-ossp`dans sa base de données.

```sql
DROP EXTENSION "uuid-ossp";
CREATE EXTENSION "uuid-ossp";

-- test
SELECT uuid_generate_v4();
```


## Logiciels

### QGIS

Le ministère de la Transition Écologique [a produit une note](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjFu8SXhdT_AhXfVqQEHf4KBk0QFnoECAsQAQ&url=https%3A%2F%2Fwww.occitanie.developpement-durable.gouv.fr%2FIMG%2Fpdf%2Fgenerer_uuid_via_qgis_v0.pdf&usg=AOvVaw2TSOSho9XFdo2EpLGGxENV&opi=89978449) expliquant comment générer un UUID dans un attribut avec la calculatrice. Mais cela n'indique pas si c'est de l'UUID v4.