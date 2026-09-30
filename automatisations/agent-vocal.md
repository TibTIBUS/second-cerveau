# Agent vocal (appels passés à la place de Thibaut)

Objectif : un agent qui téléphone pour Thibaut, en perso (rendez-vous médical, restaurant, pizza) puis en pro (prospection Localia). Il n'aime pas téléphoner.

Statut : plan validé le 2026-09-30, aucune étape commencée.

## Règles

- Accord de Thibaut avant toute dépense. Plafond : 10 € de crédit au départ, recharge automatique désactivée.
- Jamais de clé secrète ni de mot de passe dans le chat ou Telegram : saisie en local sur le PC (script), comme pour Tavily.
- L'agent ne donne jamais de numéro de carte bancaire par téléphone.
- Rendez-vous médical : uniquement nom, téléphone et disponibilités, aucun détail de santé.
- L'agent se présente comme l'assistant qui appelle pour le compte de Thibaut.
- Une seule étape à la fois. Ne passer à la suivante que quand la précédente est validée par Thibaut.

## Coûts (prix relevés le 2026-09-30, à revérifier avant de payer)

- Paiement à la minute, pas d'abonnement fixe obligatoire.
- Plateforme visée : ElevenLabs Agents (offre tout-en-un, environ 0,08 à 0,24 $ la minute selon une comparaison) + téléphonie sortante France (environ 0,013 à 0,022 $ la minute).
- Ordre de grandeur : un appel de 2 minutes coûte environ 0,20 à 0,60 €. Dix appels perso par mois : 2 à 6 €.
- Prospection : 100 appels de 2 minutes, environ 20 à 60 €.
- Vapi et Retell écartés : trop techniques (assemblage de plusieurs services).

## Étapes

- [ ] 1. Créer un compte ElevenLabs, mettre 10 € de crédit maximum, recharge automatique désactivée.
- [ ] 2. Agent de test qui appelle le propre téléphone de Thibaut et dit bonjour en français.
- [ ] 3. Premier vrai usage : réserver une table au restaurant.
- [ ] 4. Rendez-vous médical (informations minimales).
- [ ] 5. Lien avec Hermès : Thibaut demande, Hermès lance l'appel.
- [ ] 6. Prospection Localia, en dernier, après vérification juridique.

## Point juridique à vérifier avant l'étape 6

- Depuis le 11 août 2026, le démarchage téléphonique de consommateurs est interdit sans consentement préalable.
- Entre professionnels, pas de consentement préalable, mais un droit d'opposition et une offre en rapport avec l'activité de la personne appelée.
- Un agent vocal IA pourrait être traité comme un « automate d'appel », régime plus strict. La fiche CNIL trouvée exclut ce cas : question non tranchée, à vérifier auprès de la CNIL avant tout appel de prospection.
