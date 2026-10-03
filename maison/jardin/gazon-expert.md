# Gazon : base experte d'Hermès

Créé : 2026-10-03 (Claude). Hermès lit ce fichier AVANT chaque conseil pelouse, avec `maison/jardin/ma-pelouse.md`.
Contexte : Créances (Manche), climat océanique doux et humide, vent et embruns, sols du littoral souvent sableux (à confirmer par un test, voir § 2).

## 1. Comment répondre à une photo

1. `git pull`, lire ce fichier et `ma-pelouse.md` (profil + journal : ne pas redemander ce qui y est déjà).
2. Regarder la météo de Créances : 7 derniers jours (pluie, chaleur, gel) et 7 prochains jours.
3. Si la photo ne suffit pas, demander UNE chose à la fois : vue d'ensemble, gros plan à 30 cm, ou une touffe arrachée / la terre retournée.
4. Répondre court (lu sur téléphone), dans cet ordre :
   - **Ce que je vois** : diagnostic le plus probable + niveau de confiance (sûr / probable / à vérifier) + 1 alternative si doute.
   - **À faire maintenant** : 1 à 3 actions maximum, la plus importante d'abord.
   - **Robot Mammotion** : hauteur de coupe conseillée en mm (et s'il faut l'arrêter ou créer une zone interdite).
   - **Produit** : type, dose, quand l'appliquer (ou « aucun produit »). Jamais d'achat sans son « oui ».
   - **À éviter** : 1 erreur fréquente dans ce cas.
   - **Je te relance le** : date de revérification.
5. Écrire une ligne dans le journal de `ma-pelouse.md` (date, symptôme, diagnostic, conseil), commit + push.
6. Le jour de la relance : demander une nouvelle photo au même endroit et comparer.

Principes : la cause d'abord, le produit ensuite. La plupart des problèmes viennent de la tonte trop rase, du sol (tassé, pauvre, acide) ou de l'eau. Ne jamais conseiller un produit interdit aux particuliers (§ 7).

## 2. Connaître le terrain

- **Sol sableux** (fréquent sur la côte ouest du Cotentin) : draine vite, sèche vite l'été, retient mal l'engrais. Remède : apports de matière organique (compost fin ou terreau en couche de 0,5 à 1 cm à l'automne), engrais à libération lente, tonte plus haute.
- **pH** : à mesurer avant tout chaulage (kit de jardinerie ou analyse de sol). Idéal gazon : 6 à 7. Sous 5,5 : mousse et mauvaise pousse → amendement calcaire à l'automne. Au-dessus de 7,5 (sables coquilliers possibles) : jamais de chaux.
- **Test du tassement** : enfoncer un tournevis. S'il force dans les 10 premiers cm, le sol est tassé → aération (carottage ou fourche-bêche) en automne ou au printemps.
- **Feutre** : écarter l'herbe ; couche brune spongieuse de plus de 1 cm → scarification.
- **Ombre, vent, sel** : noter les zones dans `ma-pelouse.md`.

## 3. Hauteurs de coupe (robot Mammotion)

Le robot coupe souvent et peu (mulching) : c'est très bon pour le gazon, à condition de ne pas couper trop ras. Vérifier la plage de hauteurs du modèle dans l'appli Mammotion.

| Période / situation | Hauteur conseillée |
|---|---|
| Mars, reprise de la pousse | 50 mm, puis descendre |
| Avril à juin, pleine pousse | 40 à 45 mm |
| Juillet-août, sec ou chaud | 55 à 65 mm (au plus haut si sécheresse) |
| Septembre-octobre | 45 à 50 mm |
| Dernières tontes (novembre) | 50 mm, puis arrêt du robot |
| Zone ombragée ou moussue | +10 mm par rapport au reste |
| Semis récent | Zone interdite au robot ; 1re coupe quand l'herbe fait 8 cm, à 60 mm |

Règles : changer la hauteur de 10 mm maximum par semaine. Pas de tonte sur sol détrempé ou gelé. Herbe déchiquetée, pointes blanches ou brunes = lames émoussées → les changer (pièces d'usure peu chères, à vérifier toutes les 4 à 6 semaines en saison). Traces ou ornières sur le même passage → varier l'angle de tonte dans l'appli et réduire les passages sur sol mouillé.

Arrêt du robot : quand la pousse s'arrête (températures sous 5 à 6 °C durablement, en général fin novembre en Manche) jusqu'à la reprise de mars.

## 4. Calendrier pour la Manche

| Mois | Ce qu'on fait |
|---|---|
| Janvier-février | Rien. Ne pas marcher sur le gazon gelé. Ramasser branches et feuilles. Entretien et lames du robot. |
| Mars | Reprise du robot en haut (50 mm) quand l'herbe repousse. Observer mousse et zones nues. |
| Avril | Anti-mousse si mousse (sulfate de fer), puis 2 à 3 semaines après : scarification si feutre > 1 cm. Engrais de printemps à libération lente. Regarnissage possible de mi-avril à fin mai. |
| Mai-juin | Pleine pousse : 40 à 45 mm. 2e engrais léger fin mai si gazon pâle. Arrachage des pissenlits et plantains. |
| Juillet-août | Remonter la coupe. Arroser seulement si nécessaire, en profondeur (10 à 15 mm, 1 à 2 fois par semaine, tôt le matin). Pas d'engrais ni de semis en pleine chaleur. Un gazon jauni par la sécheresse repart souvent avec les pluies. Fin août : test larves (§ 6). |
| Septembre à mi-octobre | **Meilleure période de l'année** : scarification, aération, regarnissage ou semis, terreau/compost en fine couche, engrais d'automne (riche en potasse). Nématodes contre les larves si besoin. |
| Fin octobre à décembre | Ramasser les feuilles (elles étouffent le gazon). Dernières tontes à 50 mm. Arrêter le robot quand la pousse s'arrête. Chaulage seulement si pH mesuré trop bas. |

## 5. Semer, regarnir (« ressemer »)

- **Quand** : septembre à mi-octobre (idéal, sol chaud et pluies) ou mi-avril à fin mai. Sol au-dessus de 10 °C.
- **Graines pour Créances** : mélange « rustique / sol sec / bord de mer » à base de **fétuque rouge** (sel, sécheresse, sol pauvre) et **fétuque élevée** (racines profondes, résiste au sec), avec un peu de **ray-grass anglais** (pousse vite, résiste au piétinement, utile avec des enfants). Éviter les mélanges « gazon anglais d'ornement » fragiles.
- **Étapes** : tondre ras (30 mm) la zone → scarifier ou griffer pour voir la terre → semer (regarnissage : 25 à 35 g/m² ; zone nue : 35 à 50 g/m²) en deux passages croisés → recouvrir de 3 à 5 mm de terreau → tasser (rouleau ou piétinement) → garder la surface humide en continu 3 semaines (petits arrosages, plusieurs fois par jour s'il ne pleut pas).
- Levée : ray-grass 7 à 10 jours, fétuques 10 à 21 jours.
- Zone interdite au robot jusqu'à la 1re coupe (herbe à 8 cm, coupe à 60 mm), puis réintégrer progressivement.
- Pas d'anti-mousse ni de désherbant 6 semaines avant ou après un semis.

## 6. Diagnostic par symptôme

| Ce qu'on voit | Causes probables | Que faire |
|---|---|---|
| Mousse | Ombre, sol tassé ou acide, humidité, tonte trop rase, sol pauvre | Sulfate de fer (la mousse noircit en quelques jours), ratisser 2 semaines après, regarnir. Traiter la cause : remonter la coupe, aérer, mesurer le pH, engrais. |
| Jaunissement général | Sécheresse (été), manque d'azote, sol détrempé | Été : remonter la coupe, arroser en profondeur ou attendre la pluie. Sinon engrais à libération lente. |
| Rond jaune ou brûlé avec bordure vert foncé | Urine de chien, ou engrais renversé | Arroser abondamment l'endroit, regarnir si mort. |
| Plaques rosées ou rouges, filaments rouges au bout des feuilles | Fil rouge (champignon, signe de manque d'azote, temps humide) | Engrais azoté à libération lente ; pas de fongicide nécessaire. Ramasser les déchets de tonte sur les zones touchées. |
| Taches rondes brun-rose, aspect gras, automne humide | Fusariose (champignon) | Pas d'azote en automne, aérer, ne pas tondre mouillé, ramasser les feuilles. |
| Poudre orange sur les chaussures, feuilles tachées | Rouille (fin d'été, pousse lente) | Engrais azoté léger, tonte régulière, arroser le matin et non le soir. |
| Champignons en cercle, anneau d'herbe plus verte | Ronds de sorcière (matière organique enfouie) | Aérer et arroser en profondeur l'anneau. Souvent sans gravité. |
| Plaques qui se soulèvent comme un tapis, oiseaux, pies, corneilles ou blaireaux qui creusent | Larves (hannetons, otiorhynques, tipules) | Test : soulever 30 × 30 cm. Plus de 5 à 10 larves → nématodes (Heterorhabditis contre hannetons, sol > 12 °C, fin août-septembre ; Steinernema feltiae contre tipules, automne), sol arrosé avant et après. |
| Trèfle | Manque d'azote, sol pauvre | Engrais azoté ; c'est aussi un allié (fixe l'azote, reste vert l'été). |
| Pâquerettes, plantain, pissenlits | Sol tassé ou pauvre, coupe trop rase | Remonter la coupe, aérer, engrais, arracher (outil arrache-pissenlit), regarnir. |
| Herbe claire, touffes plus pâles qui jaunissent vite | Pâturin annuel ou autre graminée indésirable | Densifier par regarnissage et engrais. |
| Zones nues ou clairsemées | Piétinement, ombre, sécheresse, larves, robot sur sol mouillé | Trouver la cause, puis regarnir (§ 5). |
| Pointes déchiquetées, blanches ou brunes | Lames émoussées | Changer les lames du robot. |
| Feuillage brûlé côté mer après tempête | Embruns salés | Arroser abondamment pour lessiver, regarnir en fétuque rouge. |

## 7. Produits : règles

- **En France, depuis 2019, les particuliers ne peuvent plus acheter ni utiliser de pesticides chimiques de synthèse** (désherbants sélectifs pour gazon, fongicides, insecticides). Seuls les produits de biocontrôle, à faible risque ou utilisables en agriculture biologique sont autorisés (mention « emploi autorisé au jardin »). Hermès ne conseille jamais de produit interdit et l'indique si Thibaut en cite un.
- Autorisés et utiles : **sulfate de fer** (anti-mousse ; tache le carrelage et le béton, éloigner enfants et animaux pendant l'application, suivre l'étiquette, ordre de grandeur 30 à 40 g/m²), **engrais organiques ou organo-minéraux à libération lente**, **amendement calcaire** (seulement si pH mesuré bas), **nématodes**, **compost / terreau**, **semences**.
- Toujours : suivre la dose de l'étiquette, appliquer sur gazon sec avant une pluie légère (ou arroser), ne pas mélanger anti-mousse et semis.
- Achat : Hermès peut proposer un produit précis et un lieu d'achat (jardinerie proche de Créances ou en ligne), mais n'achète jamais : il attend le « oui » de Thibaut, et Thibaut paie lui-même.

## 8. Ce qu'Hermès ne fait pas (encore)

- Il ne règle pas le robot lui-même : il donne la hauteur, Thibaut la règle dans l'appli Mammotion. Piste plus tard : Home Assistant (déjà prévue pour le robot et la porte de garage).
- Il ne dit jamais « c'est sûr » sur une seule photo floue ou lointaine : il demande un gros plan.
