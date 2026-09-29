# Podcast du matin — réglages

État : **essai validé par Thibaut** (contenu OK), pas encore programmé. Horaire à fixer.

## Format

- Vocal Telegram en français (voix fr-FR-DeniseNeural), 5 min maximum, avec le texte en dessous.
- Jours et heure : à confirmer par Thibaut.
- Ton direct, sans remplissage. Une rubrique vide est sautée.

## Contenu, dans cet ordre

1. **Perso** : anniversaires et fêtes du jour (`dates.md`), puis ceux des 7 prochains jours avec une idée cadeau tirée de la fiche ; agenda famille du jour ; **rappels de la maison** (voir ci-dessous).
2. **Pro** : agenda Localia du jour ; tâches dues ou en retard (`taches.md`).
3. **Sport** (version de Thibaut, 2026-09-29) : F1 ; football : équipe de France, Olympique de Marseille, Stade Malherbe de Caen (résultats de la veille, prochain match, actu importante).
4. **Actus** : 3 titres généraux, puis 3 infos tech et IA.

## Rappels de la maison (hebdomadaires)

Source : `maison/menage.md`.

- **Mercredi** : "Ce soir, rangement de la maison : la femme de ménage passe demain."
- **Jeudi** : "La femme de ménage passe cet après-midi, de 14 h à 17 h 30."
- Si une absence ou un jour férié est noté dans `dates.md`, ne pas faire le rappel de cette semaine-là.

## Sources

- Ce dépôt : `dates.md`, `taches.md`, `personnes/`, `maison/menage.md`.
- Agendas : liens iCal privés, gardés dans la configuration de Hermès, **jamais dans ce dépôt**.
- Actus et sport : flux RSS à choisir et tester.

## Règles

- Ne rien inventer. Si une source ne répond pas, le dire en une phrase et continuer.
- En cas d'échec complet : envoyer un message texte « podcast indisponible » avec la cause.

## Arrêt

- Dire à Hermès « mets en pause le podcast du matin » (désactive la tâche planifiée), puis passer l'état à « en pause » dans `SUIVI.md`.
