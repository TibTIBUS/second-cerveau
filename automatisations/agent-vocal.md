# Agent vocal (appels passés à la place de Thibaut)

Objectif : un agent qui téléphone pour Thibaut, en perso (rendez-vous médical, restaurant, pizza) puis en pro (prospection Localia). Il n'aime pas téléphoner.

Statut au 2026-09-30 : compte ElevenLabs (offre gratuite), agent de test « Assistant de Thibaut - test » (voix Clément, français), compte Twilio payant (solde de 20 $, recharge automatique désactivée), mobile de Thibaut vérifié comme numéro appelant (numéro « Perso Tib », appels sortants seulement), profil de conformité Twilio (Trust Hub) approuvé. Appel de test vers le numéro pro de Thibaut réussi : voix très bien au téléphone, aucun délai gênant, comprend bien les interruptions, se présente comme l'assistant de Thibaut.

## Règles

- Accord de Thibaut avant toute dépense ou ajout de carte bancaire.
- Jamais de clé secrète, mot de passe ni pièce d'identité dans le chat ou Telegram : saisie par Thibaut lui-même, en local.
- L'agent ne donne jamais de numéro de carte bancaire par téléphone.
- Rendez-vous médical : uniquement nom, téléphone et disponibilités, aucun détail de santé.
- L'agent se présente comme l'assistant IA qui appelle pour le compte de Thibaut, et répond honnêtement s'il est interrogé.
- Une seule étape à la fois. Ne passer à la suivante que quand la précédente est validée par Thibaut.
- Chaque appel réel est confirmé par Thibaut avant de partir (restaurant, date, heure, nombre de personnes).
- L'agent Chrome ne touche jamais aux identifiants Twilio ni aux données d'identité.
- Répartition : les agents (Chrome, Hermès) font tout ; Thibaut ne saisit que ce qui touche à un numéro, une identité ou une donnée personnelle.

## Coûts (relevés le 2026-09-30, à revérifier avant de payer)

- Offre gratuite ElevenLabs : 15 minutes d'appels d'agent par mois, sans carte bancaire.
- Offre payante Starter : 6 $ par mois, 75 minutes d'appels. Pas nécessaire à ce jour.
- Sur les offres payantes, le tarif d'appel annoncé est d'environ 0,08 $ la minute, plus le modèle de langage et la téléphonie facturés à part (téléphonie sortante France : environ 0,013 à 0,022 $ la minute chez Twilio).
- Twilio : solde prépayé de 20 $ (plafond réel), recharge automatique désactivée. Vérifier qu'un seul débit de 20 $ apparaît sur le relevé bancaire.
- Ordre de grandeur : quelques euros par mois en usage perso. Prospection : 100 appels de 2 minutes, environ 20 à 60 €.
- Vapi et Retell écartés : trop techniques.

## Numéro d'appel

- Retenu : le mobile de Thibaut vérifié dans Twilio (« Verified Caller ID »), appels sortants seulement. Le destinataire voit ce numéro et rappelle Thibaut. Ne pas appeler ce même numéro pour les tests.
- Twilio exige un profil de conformité approuvé pour tout appel sortant (même vers un numéro vérifié) : fait.
- Option B (plus tard) : acheter un numéro français chez Twilio, avec un « Regulatory Bundle ».

## Étapes

- [x] 1. Créer un compte ElevenLabs (offre gratuite).
- [x] 2. Agent de test créé et essayé au micro dans le navigateur : concluant.
- [x] 3a. Twilio relié, profil Trust Hub approuvé, appel de test réussi vers le numéro pro de Thibaut.
- [ ] 3b. Premier vrai usage : réserver une table au restaurant (agent « réservations » à créer, mission donnée à chaque appel, confirmation de Thibaut avant l'appel).
- [ ] 4. Rendez-vous médical (informations minimales).
- [ ] 5. Lien avec Hermès : Thibaut demande sur Telegram, Hermès confirme puis lance l'appel, et renvoie le résultat. Clé ElevenLabs saisie par Thibaut en local uniquement.
- [ ] 6. Prospection Localia, en dernier, après vérification juridique.

## Point juridique à vérifier avant l'étape 6

- Depuis le 11 août 2026, le démarchage téléphonique de consommateurs est interdit sans consentement préalable.
- Entre professionnels, pas de consentement préalable, mais un droit d'opposition et une offre en rapport avec l'activité de la personne appelée.
- Un agent vocal IA pourrait être traité comme un « automate d'appel », régime plus strict. La fiche CNIL trouvée exclut ce cas : question non tranchée, à vérifier auprès de la CNIL avant tout appel de prospection.
