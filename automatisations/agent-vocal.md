# Agent vocal (appels passés à la place de Thibaut)

Objectif : un agent qui téléphone pour Thibaut, en perso (rendez-vous médical, restaurant, pizza) puis en pro (prospection Localia). Il n'aime pas téléphoner.

Statut : plan validé le 2026-09-30. Compte ElevenLabs créé le 2026-09-30 (offre gratuite, sans carte bancaire).

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
- Pour appeler de vrais numéros : il faut un compte Twilio (avec carte bancaire) et un numéro, relié à ElevenLabs. Un numéro « vérifié » peut servir à appeler seulement (pas à recevoir).
- Ordre de grandeur : quelques euros par mois en usage perso. Prospection : 100 appels de 2 minutes, environ 20 à 60 €.
- Vapi et Retell écartés : trop techniques.

## Étapes

- [x] 1. Créer un compte ElevenLabs (offre gratuite, pas de carte bancaire pour l'instant).
- [ ] 2. Créer un agent de test et lui parler depuis le navigateur (sans numéro de téléphone), en français.
- [ ] 3. Compte Twilio + numéro, puis premier vrai usage : réserver une table au restaurant (plafond de dépense, recharge automatique désactivée).
- [ ] 4. Rendez-vous médical (informations minimales).
- [ ] 5. Lien avec Hermès : Thibaut demande, Hermès lance l'appel.
- [ ] 6. Prospection Localia, en dernier, après vérification juridique.

## Point juridique à vérifier avant l'étape 6

- Depuis le 11 août 2026, le démarchage téléphonique de consommateurs est interdit sans consentement préalable.
- Entre professionnels, pas de consentement préalable, mais un droit d'opposition et une offre en rapport avec l'activité de la personne appelée.
- Un agent vocal IA pourrait être traité comme un « automate d'appel », régime plus strict. La fiche CNIL trouvée exclut ce cas : question non tranchée, à vérifier auprès de la CNIL avant tout appel de prospection.
