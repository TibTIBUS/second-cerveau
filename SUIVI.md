# Suivi du chantier « second cerveau & automatisations »

Mise à jour : 2026-10-01 (Claude)

## Objectif

Retrouver facilement les infos, ne plus rien oublier de ce qui concerne les proches, transformer idées et messages en actions, automatiser le répétitif et réduire la charge mentale. Système simple, fiable, facile à maintenir.

## Décisions

- 2026-09-29 — Source unique : ce dépôt GitHub privé (fichiers Markdown), lu et modifié par Thibaut, Hermès (git sur le PC) et Claude (connecteur GitHub).
- 2026-09-29 — Les automatisations tournent sur Hermès : PC allumé en permanence, modèle actuel GPT 6 Luna. Pas de budget supplémentaire, sauf quelques euros acceptés pour un agent vocal d'appels.
- 2026-09-29 — Ordre : 1) second cerveau + capture vocale, 2) podcast du matin, 3) courses, 4) prospection, 5) réservations, puis agent vocal.
- 2026-09-29 — Écarté : confier les appels de prospection à une IA (image de proximité, cadre juridique des appels automatisés, transparence IA).
- 2026-09-29 — Données des clients Localia : hors de ce dépôt.
- 2026-09-29 — Écriture directe sur `main` autorisée ici (exception à la règle du site Localia). Aucune suppression sans accord de Thibaut.
- 2026-09-29 — Podcast du matin : tous les jours à 6 h ; contenu = perso (dates, planning famille, ménage), pro, sport (F1, équipe de France, OM, SM Caen), espace (seulement si important), actus et tech/IA. Voir `automatisations/podcast-du-matin.md`.
- 2026-09-30 — Règle du silence : quand il n'y a rien à dire sur un sujet, le podcast ne dit rien.
- 2026-10-01 — Recherche web du podcast : Tavily en priorité (offre gratuite, 1 000 recherches par mois, plafond réglé à 1 000 chez Tavily), Bing via le navigateur en repli, jamais Google (bloqué).
- 2026-10-01 — Agenda famille : lien iCal FamilyWall lu par Hermès en lecture seule (titre, heure, lieu). Le lien ne va jamais dans ce dépôt.

## Outils retenus

- Dépôt GitHub privé : stockage.
- Hermès via Telegram : capture vocale, rappels, tâches planifiées.
- Synthèse vocale : Edge TTS, gratuite (voix fr-FR-DeniseNeural indisponible dans la tâche planifiée ; une voix Edge compatible est utilisée à la place) ; ffmpeg installé pour les bulles vocales Telegram.
- Recherche web : Tavily (clé dans la configuration privée de Hermès).
- Claude : conception, rédaction des fichiers, vérifications.

## Automatisations

États : proposée · en préparation · en test · active · en pause · bloquée

| Automatisation | Déclencheur | Où elle tourne | État | Pour l'arrêter |
|---|---|---|---|---|
| Capture vocale → rangement dans le dépôt | Message ou vocal Telegram à Hermès | Hermès (PC) | en test (OK sur 3 proches) | Dire à Hermès d'arrêter et retirer la consigne de sa mémoire |
| Podcast du matin | Tous les jours à 6 h (Europe/Paris) ; test en cours, 9 exécutions au total dans le compteur | Hermès (PC) → Telegram (Thibaut seul) | en test (dernier essai OK, 2026-10-01) | `hermes cron pause 8a70e39d3e7d` |
| Agenda famille (FamilyWall) dans le podcast | Chaque exécution du podcast | Hermès (PC), lecture seule | en préparation | Retirer la variable dans la configuration de Hermès |
| Courses : liste type + rappel | Chaque semaine | Hermès | proposée | Idem |
| Prospection : fiche d'appel + relance préparée | Jours ouvrés | Hermès + Gmail pro | proposée | Idem |
| Réservations préparées en ligne | À la demande | Hermès | proposée | — |
| Agent vocal qui appelle (resto, pizza) | À la demande | À définir | plus tard | — |

Déjà en place, hors chantier : routine blog Localia (brouillons en semaine), routine réseaux sociaux (brouillons validés par mail), pipeline de prospection audit-preuve (Hermès).

## Priorisation détaillée

Les gains sont des hypothèses, à comparer au temps de maintenance après un mois d'usage.

| # | Besoin | Fréquence | Gain estimé | Difficulté · coût | Accès nécessaires | Dépend de | Catégorie |
|---|---|---|---|---|---|---|---|
| 1 | Second cerveau : moi, famille, dates | Au fil de l'eau | Plus d'anniversaires ni de fêtes oubliés ; tailles et idées cadeaux en 10 s | Faible (1 à 2 h de dictée) · 0 € | Dépôt GitHub, git sur le PC | — | Fondation |
| 2 | Capture vocale via Telegram | Plusieurs fois par jour | Plus d'infos perdues dans la tête ou les notes | Faible · 0 € ou presque | Telegram (déjà en place) | 1 | Gain rapide |
| 3 | Podcast du matin | Chaque jour | ~10 min/jour de consultation en moins | Moyen (1 à 2 séances) · 0 € | Agendas (liens iCal privés), recherche web (Tavily), dépôt | 1, 2 | Gain rapide |
| 4 | Courses | Chaque semaine | ~20 à 30 min/semaine | Faible · 0 € | Drive du magasin (à préciser) | 1 | Gain rapide |
| 5 | Prospection : fiche d'appel, compte rendu vocal, relance préparée | Jours ouvrés | Plus d'appels passés | Moyen · 0 € | Gmail pro, tableur clients, pipeline audit-preuve | 1, 3 | Fondation pro |
| 6 | Réservations préparées en ligne | Quelques fois par mois | ~10 min par appel évité | Faible · 0 € | Sites de réservation | — | Gain rapide |
| 7 | Agent vocal qui appelle | Quelques fois par mois | Idem, pour les lieux sans réservation en ligne | Élevé · quelques €/mois + numéro dédié | Fournisseur voix, numéro de téléphone | 6 | Plus tard |

## Tests

- 2026-09-29 — Squelette du dépôt déposé par Claude.
- 2026-09-29 — Capture vocale : OK (Aline, Faustine, Apolline).
- 2026-09-29 — Podcast d'essai : envoyé.
- 2026-09-29 — Podcast du matin programmé pour un test de 7 jours.
- 2026-09-30 — Envoi automatique de 6 h : échec (pas de voix). Ne compte pas dans le test.
- 2026-09-30 — Exécution manuelle : OK, mais erreurs de planning (mercredi) et recherche web bloquée par Google. Corrigés ensuite : tableaux jour par jour, règle du silence, Bing en repli.
- 2026-10-01 — Exécution manuelle avec Tavily : OK, 1 min 53 s, 16 recherches Tavily, aucun repli Bing, aucune erreur de contenu signalée par Thibaut. Limites relevées : 5 échecs d'extraction d'articles (Failed to fetch url), voix fr-FR-DeniseNeural indisponible (voix Edge équivalente utilisée), et la note technique annonçait 19 recherches au lieu de 16 (le décompte de la note n'est pas fiable).

## Blocages

- Aucun. À faire ce soir par Thibaut sur son PC : remplacer la clé Tavily (passée par Telegram), puis `hermes gateway restart`.

## Prochaine action

- Thibaut : (ce soir) remplacer la clé Tavily et redémarrer la passerelle Hermès ; puis valider le résumé des rendez-vous lu depuis FamilyWall.
- Claude : suivre le podcast quotidien pendant la période de test ; vérifier la consommation Tavily après une semaine (objectif : rester sous 1 000 par mois) ; choisir ensuite la prochaine automatisation (courses ou prospection).
- À compléter par Thibaut au fil de l'eau : planning des vacances de Faustine (centre de loisirs, Mamou), autres proches, tailles et goûts.
