# Agent vocal (appels passés à la place de Thibaut)

Objectif : un agent qui téléphone pour Thibaut, en perso (rendez-vous médical, restaurant, pizza) puis en pro (prospection Localia). Il n'aime pas téléphoner.

Statut au 2026-09-30 : compte ElevenLabs créé (offre gratuite). Agent de test « Assistant de Thibaut - test » créé et testé au micro : concluant. Compte Twilio passé en payant (solde de 20 $, recharge automatique désactivée), mobile de Thibaut vérifié comme numéro appelant et importé dans ElevenLabs (numéro « Perso Tib », appels sortants seulement). Premier appel de test vers le numéro pro de Thibaut : échec, erreur Twilio « Primary compliance profile is not approved » (vérification d'identité Trust Hub requise). Étape 3 bloquée en attendant l'approbation.

## Règles

- Accord de Thibaut avant toute dépense ou ajout de carte bancaire.
- Jamais de clé secrète, mot de passe ni pièce d'identité dans le chat ou Telegram : saisie par Thibaut lui-même, en local.
- L'agent ne donne jamais de numéro de carte bancaire par téléphone.
- Rendez-vous médical : uniquement nom, téléphone et disponibilités, aucun détail de santé.
- L'agent se présente comme l'assistant qui appelle pour le compte de Thibaut.
- Une seule étape à la fois. Ne passer à la suivante que quand la précédente est validée par Thibaut.
- L'agent Chrome ne touche jamais aux identifiants Twilio ni au dossier d'identité Trust Hub.

## Coûts (relevés le 2026-09-30, à revérifier avant de payer)

- Offre gratuite ElevenLabs : 15 minutes d'appels d'agent par mois, sans carte bancaire.
- Offre payante Starter : 6 $ par mois, 75 minutes d'appels. Pas nécessaire à ce jour.
- Sur les offres payantes, le tarif d'appel annoncé est d'environ 0,08 $ la minute, plus le modèle de langage et la téléphonie facturés à part (téléphonie sortante France : environ 0,013 à 0,022 $ la minute chez Twilio).
- Twilio : solde prépayé de 20 $ (plafond réel), recharge automatique désactivée. Vérifier qu'un seul débit de 20 $ apparaît sur le relevé bancaire.
- Ordre de grandeur : quelques euros par mois en usage perso. Prospection : 100 appels de 2 minutes, environ 20 à 60 €.
- Vapi et Retell écartés : trop techniques.

## Numéro d'appel

- Retenu : le mobile de Thibaut vérifié dans Twilio (« Verified Caller ID »), appels sortants seulement. Le destinataire voit ce numéro. Ne pas appeler ce même numéro pour les tests.
- Option B (plus tard) : acheter un numéro français chez Twilio, avec un « Regulatory Bundle » (pièce d'identité + justificatif de domicile local, pas de boîte postale, validation jusqu'à 2 jours ouvrés).

## Blocage en cours : Trust Hub (Twilio)

- Erreur reçue : « Primary compliance profile is not approved... complete the KYC process in Trust Hub ».
- Cause : Twilio exige un profil de conformité principal approuvé pour appeler des numéros non vérifiés.
- À faire par Thibaut lui-même : Twilio, Trust Hub, Profiles, créer le profil principal (Individual pour un entrepreneur individuel, ou Business si Localia le permet). Pièce d'identité et adresse à donner à Twilio uniquement. Examen jusqu'à 48 h.
- Tant que non approuvé : possible d'appeler seulement des numéros ajoutés comme « Verified Caller IDs » dans Twilio (test).

## Étapes

- [x] 1. Créer un compte ElevenLabs (offre gratuite).
- [x] 2. Agent de test créé et essayé au micro dans le navigateur : concluant.
- [ ] 3. Twilio relié (fait) + profil Trust Hub approuvé (en attente) + appel de test vers le numéro pro de Thibaut, puis premier vrai usage : réserver une table au restaurant.
- [ ] 4. Rendez-vous médical (informations minimales).
- [ ] 5. Lien avec Hermès : Thibaut demande, Hermès lance l'appel.
- [ ] 6. Prospection Localia, en dernier, après vérification juridique.

## Point juridique à vérifier avant l'étape 6

- Depuis le 11 août 2026, le démarchage téléphonique de consommateurs est interdit sans consentement préalable.
- Entre professionnels, pas de consentement préalable, mais un droit d'opposition et une offre en rapport avec l'activité de la personne appelée.
- Un agent vocal IA pourrait être traité comme un « automate d'appel », régime plus strict. La fiche CNIL trouvée exclut ce cas : question non tranchée, à vérifier auprès de la CNIL avant tout appel de prospection.
