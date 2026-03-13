# SQL more queries

Collection de scripts SQL pour pratiquer la gestion d'utilisateurs, privileges,
contraintes, bases relationnelles et requetes avec sous-requetes et jointures.

## Prerequis

- MySQL 8.x (ou version compatible)
- Un utilisateur MySQL avec les droits suffisants (souvent root en local)

## Execution

Depuis le dossier du projet :

```bash
cat <fichier.sql> | mysql -hlocalhost -uroot -p
```

Exemple :

```bash
cat 6-states.sql | mysql -hlocalhost -uroot -p
```

## Contenu des fichiers

- 0-privileges.sql : affiche les privileges de user_0d_1 et user_0d_2.
- 1-create_user.sql : cree user_0d_1 avec tous les privileges.
- 2-create_read_user.sql : cree la base hbtn_0d_2, cree user_0d_2 et lui donne
	le droit SELECT sur cette base.
- 3-force_name.sql : cree force_name avec name obligatoire.
- 4-never_empty.sql : cree id_not_null avec id par defaut a 1.
- 5-unique_id.sql : cree unique_id avec id unique (par defaut 1).
- 6-states.sql : cree la base hbtn_0d_usa et la table states.
- 7-cities.sql : cree la base hbtn_0d_usa et la table cities liee a states.
- 8-cities_of_california_subquery.sql : liste les villes de California via
	sous-requete.
- 9-cities_by_state_join.sql : liste les villes avec leur etat via JOIN.
- 10-genre_id_by_show.sql : liste les shows ayant au moins un genre.
- 11-genre_id_all_shows.sql : liste tous les shows, meme sans genre.
- 12-no_genre.sql : liste les shows sans genre.
- 13-count_shows_by_genre.sql : compte les shows par genre.

## Notes

- Certains scripts supposent que les bases/tables de l'exercice precedent
	existent deja.
- L'ordre d'execution recommande est numerique (0 a 13).
