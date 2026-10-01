# Planning famille : horaires d'Aline, garde et activités des filles

Source pour le podcast du matin. Informations données par Thibaut le 2026-09-29, **corrigées le 2026-10-01** : le cycle d'Aline est le suivant.

- **Semaine A** (lundi 2026-09-28, 2026-10-12…) : repos le **lundi**, travaille les autres jours de semaine jusqu'à 19 h 15, finit à **18 h le samedi**. Le jeudi, elle finit à 19 h 15.
- **Semaine B** (lundi 2026-10-05, 2026-10-19…) : repos le **mercredi**, travaille le lundi, finit à **18 h le jeudi**, finit à 19 h 15 le samedi.

Surnoms : **Mamour** = Aline ; **Mamou** = Agnès, la maman d'Aline ; **Papé** = Daniel, le papa d'Aline. Dans le podcast, dire « Aline » ou « Mamou » selon la personne, sans confusion.

**Le podcast n'utilise plus ce tableau directement** : les horaires sont dans `scripts/briefing_du_jour.py` (tables ALINE, APOLLINE, VACANCES, SANS_CLASSE). Ce fichier reste la version lisible. **Si le planning change, modifier le script ET ce fichier.**

## Méthode en 3 étapes (ne rien deviner)

1. **Trouver la semaine** de la date du jour dans le calendrier A/B ci-dessous (lundi de la semaine → A ou B).
2. **Lire la ligne** « semaine A » ou « semaine B » du tableau de la semaine, au jour de la semaine voulu.
3. **Vérifier les exceptions** : vacances scolaires, jours sans classe, congés d'Aline dans `dates.md`. Elles priment sur le tableau.

## Calendrier des semaines A/B

Le lundi de chaque semaine : la semaine alterne A, B, A, B…

| Lundi de la semaine | Semaine |
|---|---|
| 2026-09-28 | A |
| 2026-10-05 | B |
| 2026-10-12 | A |
| 2026-10-19 | B |
| 2026-10-26 | A |
| 2026-11-02 | B |
| 2026-11-09 | A |
| 2026-11-16 | B |
| 2026-11-23 | A |
| 2026-11-30 | B |
| 2026-12-07 | A |
| 2026-12-14 | B |
| 2026-12-21 | A |
| 2026-12-28 | B |
| 2027-01-04 | A |

Au-delà : continuer l'alternance (A les semaines dont le lundi est un nombre pair de semaines après le 2026-09-28).

## Semaine A : jour par jour (hors vacances et jours sans classe)

| Jour | Aline | Apolline | Faustine |
|---|---|---|---|
| Lundi | **En repos** | À la maison | École 8 h 30–12 h, 13 h 30–16 h 30 |
| Mardi | Travaille 9 h–19 h 15 ; badminton à 20 h | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30 |
| Mercredi | Travaille 9 h–19 h 15 | Chez Séverine | **Pas d'école.** Natation le matin, **accompagnée par Mamou** |
| Jeudi | Travaille 9 h–19 h 15 | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30. Ménage : passage de 14 h à 17 h 30 |
| Vendredi | Travaille 9 h–19 h 15 | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30, puis **hand 17 h 15–18 h 15** (Thibaut emmène aussi Emma et Soline) |
| Samedi | Travaille 9 h–**18 h** | À la maison avec Thibaut | Pas d'école |
| Dimanche | Pas de travail | À la maison | Pas d'école |

## Semaine B : jour par jour (hors vacances et jours sans classe)

| Jour | Aline | Apolline | Faustine |
|---|---|---|---|
| Lundi | Travaille 9 h–19 h 15 | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30 |
| Mardi | Travaille 9 h–19 h 15 ; badminton à 20 h | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30 |
| Mercredi | **En repos** | À la maison | **Pas d'école.** Natation le matin, **accompagnée par Aline** |
| Jeudi | Travaille 9 h–**18 h** | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30. Ménage : passage de 14 h à 17 h 30 |
| Vendredi | Travaille 9 h–19 h 15 | Chez Séverine | École 8 h 30–12 h, 13 h 30–16 h 30, puis **hand 17 h 15–18 h 15** (Thibaut emmène aussi Emma et Soline) |
| Samedi | Travaille 9 h–19 h 15 | À la maison avec Thibaut | Pas d'école |
| Dimanche | Pas de travail | À la maison | Pas d'école |

Le badminton du mardi n'a pas lieu pendant les vacances scolaires.

## Faustine : détails

**École** : lundi, mardi, jeudi et vendredi uniquement. Jamais le mercredi.

**Handball** : uniquement hors vacances scolaires (pas de hand pendant les vacances). Thibaut l'emmène, ainsi que ses copines **Emma** et **Soline**.

**Pendant les vacances** : en alternance au centre de loisirs et chez sa grand-mère Agnès (« Mamou »). Le détail des jours n'est pas encore connu : Thibaut le donnera au fur et à mesure.

## Vacances scolaires 2026-2027 (zone B, académie de Caen)

Source : calendrier officiel de l'Éducation nationale (via Onisep), consulté le 2026-09-29.

| Vacances | Dernier jour d'école | Reprise |
|---|---|---|
| Toussaint | vendredi 2026-10-16 | lundi 2026-11-02 |
| Noël | vendredi 2026-12-18 | lundi 2027-01-04 |
| Hiver | vendredi 2027-02-19 | lundi 2027-03-08 |
| Printemps | vendredi 2027-04-16 | lundi 2027-05-03 |
| Été | vendredi 2027-07-02 | rentrée de septembre 2027 |

Jours sans classe hors vacances : lundi 2027-03-29 (lundi de Pâques), jeudi 2027-05-06 (Ascension), vendredi 2027-05-07 (pas de classe), lundi 2027-05-17 (Pentecôte). Le mercredi 2026-11-11 est férié (jour sans école de toute façon).

À revérifier si l'école annonce d'autres fermetures (journée pédagogique, grève…).

## Ce que le podcast dit chaque matin

Une ou deux phrases courtes, tirées du tableau du jour. Exemples :

> Aline travaille aujourd'hui de 9 h à 19 h 15. Apolline est chez Séverine, Faustine à l'école de 8 h 30 à 16 h 30.

> Aline est en repos. Apolline est à la maison. (jour de repos)

> Faustine n'a pas école, elle a natation ce matin avec Mamou. (mercredi, semaine A)

Règles :
- Dire la personne exacte inscrite dans le tableau du jour (Aline ou Mamou pour la natation). Ne jamais écrire « Aline ou Mamou ».
- Vendredi hors vacances : « Hand de Faustine à 17 h 15, tu emmènes aussi Emma et Soline. »
- Jeudi : rappeler le passage de la femme de ménage l'après-midi.
- Jour de vacances ou sans classe : dire que Faustine n'a pas école, ne pas parler du hand. Si le détail du jour est inconnu : « centre de loisirs ou chez Mamou ». La veille de la reprise, la rappeler.
- Si une info manque : ne pas la dire (règle du silence du podcast), ne pas deviner.

## À confirmer par Thibaut

- Pendant les vacances, quels jours Faustine est au centre de loisirs ou chez Mamou, et qui la garde quand Aline travaille.
