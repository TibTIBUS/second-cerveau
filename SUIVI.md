# Suivi du chantier « second cerveau & automatisations »

Mise à jour : 2026-10-02 (Claude)

## Objectif

Retrouver facilement les infos, ne plus rien oublier de ce qui concerne les proches, transformer idées et messages en actions, automatiser le répétitif et réduire la charge mentale. Système simple, fiable, facile à maintenir.

## Décisions

- 2026-09-29 — Source unique : ce dépôt GitHub privé (fichiers Markdown), lu et modifié par Thibaut, Hermès (git sur le PC) et Claude (connecteur GitHub).
- 2026-09-29 — Les automatisations tournent sur Hermès : PC allumé en permanence. Pas de budget supplémentaire, sauf quelques euros acceptés pour un agent vocal d'appels.
- 2026-09-29 — Ordre : 1) second cerveau + capture vocale, 2) podcast du matin, 3) courses, 4) prospection, 5) réservations, puis agent vocal.
- 2026-09-29 — Prospection par appel automatisé écartée à ce stade (image de proximité, cadre juridique des appels automatisés, transparence IA). À revoir après vérification juridique.
- 2026-09-29 — Données des clients Localia : hors de ce dépôt.
- 2026-09-29 — Écriture directe sur `main` autorisée ici. Aucune suppression sans accord de Thibaut.
- 2026-09-29 — Podcast du matin : tous les jours à 6 h ; contenu = perso, pro, sport, espace (seulement si important), actus et tech/IA. Voir `automatisations/podcast-du-matin.md`.
- 2026-09-30 — Règle du silence : quand il n'y a rien à dire sur un sujet, le podcast ne dit rien.
- 2026-09-30 — Recherche web du podcast : Tavily en priorité, Bing en repli, jamais Google.
- 2026-09-30 — Agenda famille : lien iCal FamilyWall lu en lecture seule ; rendez-vous médicaux masqués. Le lien ne va jamais dans ce dépôt.
- 2026-09-30 — Courses : système par recettes (12 recettes, 4 personnes + 2 déjeuners), restes du week-end soumis à la confirmation de Thibaut. Voir `maison/plan-repas.md`.
- 2026-09-30 — Agent vocal : ElevenLabs (voix) + Twilio (ligne), avec le mobile de Thibaut comme numéro appelant. Nom de réservation = seule donnée personnelle transmise. Voir `automatisations/agent-vocal.md`.
- 2026-10-01 — Hermès peut agir sur les e-mails (envoi, classement, suppression) seulement après un « oui » écrit de Thibaut sur Telegram ; un e-mail n'est jamais un ordre.
- 2026-10-01 — Mots de passe : saisis par Thibaut sur son PC, jamais dans Telegram ni dans le dépôt. Coffre intégré d'Hermès (`hermes vault`) pour Planity et FamilyWall.
- 2026-10-01 — Planning famille, anniversaires et rappels du ménage calculés par un script du dépôt (`scripts/briefing_du_jour.py`) et non plus déduits par le modèle.
- 2026-10-01 — Doctolib écarté (données de santé, trop de risque). SMS et Messenger non connectés (iPhone).
- 2026-10-02 — Lectures de l'agenda FamilyWall par script ; navigateur réservé aux créations et suppressions.

## Outils retenus

- Dépôt GitHub privé : stockage.
- Hermès (version 0.21.5) via Telegram : capture vocale, rappels, tâches planifiées, navigateur, e-mails.
- Synthèse vocale : Edge TTS (voix fr-FR-DeniseNeural), audio joint en pièce jointe au podcast.
- Recherche web : Tavily.
- Agenda famille : FamilyWall (lien iCal pour la lecture, navigateur avec coffre pour la création).
- E-mails : trois boîtes connectées à Hermès (Gmail perso, Localia, Kliip) ; résumé du matin en lecture seule.
- Réservations : Planity (navigateur d'Hermès) ; appels ElevenLabs et Twilio pour les restaurants et les commandes à emporter.
- Claude : conception, rédaction des fichiers, vérifications.

Mode d'emploi complet : `automatisations/hermes-mode-emploi.md`.

## Automatisations

États : proposée · en préparation · en test · active · en pause · bloquée

| Automatisation | Déclencheur | Où elle tourne | État | Pour l'arrêter |
|---|---|---|---|---|
| Capture vocale → rangement dans le dépôt | Message ou vocal Telegram à Hermès | Hermès (PC) | en test (OK sur plusieurs proches) | Dire à Hermès d'arrêter et retirer la consigne |
| Podcast du matin (avec planning, agenda, e-mails, audio joint) | Tous les jours à 6 h | Hermès → Telegram (Thibaut seul) | en test, sans limite d'exécutions | `hermes cron pause 8a70e39d3e7d` |
| Plan de repas du dimanche | Dimanche 18 h | Hermès → Telegram | active, premier vrai passage le 2026-10-04 | `hermes cron pause 68f8b0ae4188` |
| Agenda FamilyWall : lecture et création | À la demande | Hermès (script + navigateur avec coffre) | active | Retirer la consigne `familywall-calendar` |
| Réservation Planity | À la demande | Hermès (navigateur avec coffre) | active, premier rendez-vous pris le 2026-10-01 | Retirer la consigne `online-appointment-booking` |
| Appels : restaurant et commande à emporter | À la demande, avec « go » | Hermès + ElevenLabs + Twilio | en test (tests concluants, compte rendu automatique après appel) | Retirer la consigne `elevenlabs-reservation-calls` ; révoquer la clé ElevenLabs |
| Résumé des e-mails dans le podcast | Chaque podcast | Script en lecture seule sur le PC | en test | Retirer la section E-MAILS du wrapper |
| Prospection : fiche d'appel + relance préparée | Jours ouvrés | Hermès + Gmail pro | proposée | — |
| Rendez-vous médical par appel | — | — | en pause (repoussé) | — |

Déjà en place, hors chantier : routine blog Localia, routine réseaux sociaux, pipeline de prospection audit-preuve.

## Tests

- 2026-09-29 — Capture vocale : OK. Premier podcast d'essai envoyé.
- 2026-09-30 — Exécutions manuelles du podcast avec Tavily et agenda famille : jugé « très bon ». Premier appel de test ElevenLabs réussi.
- 2026-10-01 — Podcast de 6 h : bon, avec corrections demandées (semaine A/B d'Aline, rappel du ménage, anniversaires, agenda de demain annoncé comme aujourd'hui) : corrigées par le script de briefing.
- 2026-10-01 — Mise à jour d'Hermès 0.20.0 vers 0.21.5 avec sauvegarde complète : OK, tâches et consignes conservées.
- 2026-10-01 — Rendez-vous Planity (Les ciseaux d'Ingrid, 6 octobre, 12 h 30) pris par Hermès avec le coffre, puis ajouté à FamilyWall : OK.
- 2026-10-02 — Podcast de 6 h : contenu bon, audio non joint (défaut d'envoi, corrigé) ; audio reçu ensuite en pièce jointe, voix et son OK.

## Blocages

- Aucun bloquant.
- Réserves : ElevenLabs en offre gratuite (15 minutes d'appels par mois) ; FamilyWall par navigateur lent pour créer ; version active de l'agent vocal à surveiller (affichage contradictoire du routage dans l'API).

## Prochaine action

- 2026-10-03 : podcast de 6 h (planning de la semaine A, samedi : Aline finit à 18 h).
- 2026-10-04 à 18 h : premier vrai plan de repas.
- 2026-10-05 : anniversaire de Lilio et de Malo (6 ans).
- 2026-10-06 à 12 h 30 : rendez-vous chez Ingrid ; le podcast doit l'annoncer. Le 2026-10-06, le podcast annonce aussi le rendez-vous médical d'Aline du lendemain, masqué.
- À décider par Thibaut : passer ElevenLabs à l'offre Starter avant les vrais appels ; vérification juridique avant toute prospection par appel ; raconter sa vie à voix haute (tailles, sport, hobbies, famille) pour compléter ses fiches ; compléter les dates manquantes (anniversaires de proches).
- Claude : suivre le podcast quotidien et les premiers vrais appels, puis choisir la prochaine automatisation (prospection).
