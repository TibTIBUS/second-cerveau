# Agent vocal (appels passés à la place de Thibaut)

Objectif : un agent qui téléphone pour Thibaut, en perso (rendez-vous médical, restaurant, pizza) puis en pro (prospection Localia). Il n'aime pas téléphoner.

Statut au 2026-09-30 (soir) : compte ElevenLabs (offre gratuite), agents « Assistant de Thibaut - test » et « Assistant de Thibaut - réservations » (voix Clément, français), compte Twilio payant (solde de 20 $, recharge automatique désactivée), mobile de Thibaut vérifié comme numéro appelant (numéro « Perso Tib », appels sortants seulement), profil de conformité Twilio (Trust Hub) approuvé. Appels de test vers le numéro pro de Thibaut réussis (Thibaut jouait le restaurant) : voix très bien, aucun délai gênant, comprend les interruptions. Hermès est connecté : clé ElevenLabs dans son fichier privé, script d'appel créé et testé en simulation (aucun appel réel), consigne permanente enregistrée.

## Règles

- Accord de Thibaut avant toute dépense ou ajout de carte bancaire.
- Jamais de clé secrète, mot de passe ni pièce d'identité dans le chat ou Telegram : saisie par Thibaut lui-même, en local.
- L'agent ne donne jamais de numéro de carte bancaire par téléphone.
- Seule donnée personnelle transmise : le nom de réservation, confirmé par Thibaut pour chaque appel. Jamais d'adresse, e-mail, date de naissance, carte, identité ni donnée de santé.
- Rendez-vous médical : pas encore autorisé (à valider plus tard ; uniquement nom, téléphone, disponibilités).
- L'agent se présente comme l'assistant IA qui appelle pour le compte de Thibaut, et répond honnêtement s'il est interrogé.
- Une seule étape à la fois. Ne passer à la suivante que quand la précédente est validée par Thibaut.
- Chaque appel réel est confirmé par Thibaut (« oui » ou « go » dans la conversation en cours) avant de partir : restaurant, numéro, jour, heure, nombre de personnes, nom de réservation.
- Aucun nouvel essai automatique après un échec : Hermès rapporte l'erreur exacte.
- L'agent Chrome ne touche jamais aux identifiants Twilio ni aux données d'identité.
- Répartition : les agents (Chrome, Hermès) font tout ; Thibaut ne saisit que ce qui touche à un numéro, une identité ou une donnée personnelle.

## Garde-fous codés dans le script d'Hermès

- Script : ~/.hermes/scripts/elevenlabs_call.py (commandes list, call, status). « call » est en simulation par défaut ; appel réel seulement avec l'option --confirm.
- Numéros +33 valides uniquement ; refus des numéros d'urgence, courts, surtaxés ou spéciaux.
- Aucun appel entre 21 h et 9 h (heure de Paris).
- Maximum 3 appels réels par jour.
- Agent utilisé : uniquement « Assistant de Thibaut - réservations ». Enregistrement audio désactivé.
- Journal local minimal (date, 4 derniers chiffres, statut).
- Consigne permanente : ~/.hermes/skills/productivity/elevenlabs-reservation-calls/SKILL.md.

## Coûts (relevés le 2026-09-30, à revérifier avant de payer)

- Offre gratuite ElevenLabs : 15 minutes d'appels d'agent par mois, sans carte bancaire.
- Offre payante Starter : 6 $ par mois, 75 minutes d'appels. Pas nécessaire à ce jour.
- Sur les offres payantes, le tarif d'appel annoncé est d'environ 0,08 $ la minute, plus le modèle de langage et la téléphonie facturés à part (téléphonie sortante France : environ 0,013 à 0,022 $ la minute chez Twilio).
- Twilio : solde prépayé de 20 $ (plafond réel), recharge automatique désactivée. Vérifier qu'un seul débit de 20 $ apparaît sur le relevé bancaire.
- Ordre de grandeur : quelques euros par mois en usage perso. Prospection : 100 appels de 2 minutes, environ 20 à 60 €.
- Vapi et Retell écartés : trop techniques.

## Numéro d'appel

- Retenu : le mobile de Thibaut vérifié dans Twilio (« Verified Caller ID »), appels sortants seulement. Le destinataire voit ce numéro et rappelle Thibaut. Ne pas appeler ce même numéro pour les tests.
- Twilio exige un profil de conformité approuvé pour tout appel sortant : fait.
- Option B (plus tard) : acheter un numéro français chez Twilio, avec un « Regulatory Bundle ».

## Point à vérifier

- Hermès a signalé une incohérence d'affichage dans l'API ElevenLabs : la branche Main montre 100 % du trafic dans la liste des branches et 0 % dans le détail. Les nouvelles instructions sont bien présentes. À confirmer par le premier appel de test de bout en bout (vérifier que l'agent suit bien les consignes à jour).

## Étapes

- [x] 1. Créer un compte ElevenLabs (offre gratuite).
- [x] 2. Agent de test créé et essayé au micro dans le navigateur : concluant.
- [x] 3. Twilio relié, profil Trust Hub approuvé, appels de test réussis (simulation de restaurant sur le numéro pro de Thibaut).
- [ ] 4. Rendez-vous médical : repoussé après Hermès.
- [ ] 5. Hermès : clé et script faits ; reste le test de bout en bout (Telegram, confirmation, appel vers le numéro pro de Thibaut jouant le restaurant, compte rendu) à faire après 9 h, puis premier vrai restaurant.
- [ ] 6. Prospection Localia, en dernier, après vérification juridique.

## Point juridique à vérifier avant l'étape 6

- Depuis le 11 août 2026, le démarchage téléphonique de consommateurs est interdit sans consentement préalable.
- Entre professionnels, pas de consentement préalable, mais un droit d'opposition et une offre en rapport avec l'activité de la personne appelée.
- Un agent vocal IA pourrait être traité comme un « automate d'appel », régime plus strict. La fiche CNIL trouvée exclut ce cas : question non tranchée, à vérifier auprès de la CNIL avant tout appel de prospection.
