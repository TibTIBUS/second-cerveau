# Agent vocal (appels passés à la place de Thibaut)

Objectif : un agent qui téléphone pour Thibaut, en perso (rendez-vous médical, restaurant, pizza) puis en pro (prospection Localia). Il n'aime pas téléphoner.

Statut : plan validé le 2026-09-30. Compte ElevenLabs créé (offre gratuite, sans carte bancaire). Agent de test « Assistant de Thibaut - test » créé via l'agent Claude dans Chrome (voix Clément, français) et testé au micro par Thibaut le 2026-09-30 : test concluant.

## Règles

- Accord de Thibaut avant toute dépense ou ajout de carte bancaire.
- Jamais de clé secrète ni de mot de passe dans le chat ou Telegram : saisie en local sur le PC (script), comme pour Tavily.
- L'agent ne donne jamais de numéro de carte bancaire par téléphone.
- Rendez-vous médical : uniquement nom, téléphone et disponibilités, aucun détail de santé.
- L'agent se présente comme l'assistant qui appelle pour le compte de Thibaut.
- Une seule étape à la fois. Ne passer à la suivante que quand la précédente est validée par Thibaut.

## Coûts (relevés le 2026-09-30, à revérifier avant de payer)

- Offre gratuite ElevenLabs : 15 minutes d'appels d'agent par mois, sans carte bancaire. Suffit pour les étapes 1 et 2.
- Offre payante Starter : 6 $ par mois, 75 minutes d'appels. À envisager seulement à partir de l'étape 3.
- Sur les offres payantes, le tarif d'appel annoncé est d'environ 0,08 $ la minute, plus le modèle de langage et la téléphonie facturés à part (téléphonie sortante France : environ 0,013 à 0,022 $ la minute chez Twilio).
- Pour appeler de vrais numéros : compte Twilio (avec carte bancaire) relié à ElevenLabs. Un compte d'essai Twilio ne peut appeler que des numéros vérifiés, donc un compte payant sera nécessaire (recharge minimale à confirmer).
- Ordre de grandeur : quelques euros par mois en usage perso. Prospection : 100 appels de 2 minutes, environ 20 à 60 €.
- Vapi et Retell écartés : trop techniques.

## Choix du numéro d'appel (étape 3)

- Option A, recommandée : faire vérifier le propre numéro mobile de Thibaut dans Twilio (« Verified Caller ID »). L'agent appelle en sortie seulement, le numéro affiché est celui de Thibaut, aucun dossier administratif.
- Option B : acheter un numéro français chez Twilio. Demande un « Regulatory Bundle » (pièce d'identité + justificatif de domicile local, pas de boîte postale, validation jusqu'à 2 jours ouvrés), et les numéros mobiles sont difficiles à obtenir. À garder pour plus tard (réception d'appels, prospection).

## Étapes

- [x] 1. Créer un compte ElevenLabs (offre gratuite, pas de carte bancaire pour l'instant).
- [x] 2. Agent de test créé et essayé au micro dans le navigateur, en français : concluant.
- [ ] 3. Compte Twilio + numéro (option A), relié à ElevenLabs, puis premier vrai usage : réserver une table au restaurant (plafond de dépense, recharge automatique désactivée).
- [ ] 4. Rendez-vous médical (informations minimales).
- [ ] 5. Lien avec Hermès : Thibaut demande, Hermès lance l'appel.
- [ ] 6. Prospection Localia, en dernier, après vérification juridique.

## Point juridique à vérifier avant l'étape 6

- Depuis le 11 août 2026, le démarchage téléphonique de consommateurs est interdit sans consentement préalable.
- Entre professionnels, pas de consentement préalable, mais un droit d'opposition et une offre en rapport avec l'activité de la personne appelée.
- Un agent vocal IA pourrait être traité comme un « automate d'appel », régime plus strict. La fiche CNIL trouvée exclut ce cas : question non tranchée, à vérifier auprès de la CNIL avant tout appel de prospection.
