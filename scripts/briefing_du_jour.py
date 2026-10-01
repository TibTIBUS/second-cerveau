#!/usr/bin/env python3
"""Briefing du jour pour le podcast du matin : calcule tout ce qui est calculable.

Le script décide (semaine A/B, jour, vacances, anniversaires, rappels) pour que
le modèle n'ait plus qu'à lire les phrases produites, sans rien déduire.

Usage : python3 briefing_du_jour.py [--date AAAA-MM-JJ]
Sortie : JSON sur la sortie standard. Lecture seule. Aucun secret.
Les anniversaires sont lus dans ../dates.md (racine du dépôt).
"""
import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

REF_LUNDI_A = date(2026, 10, 5)  # lundi d'une semaine A (la semaine du 28 sept 2026 est donc B) ; on alterne A, B, A, B...

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]

# Vacances scolaires zone B, académie de Caen, 2026-2027 (premier et dernier jour sans école).
VACANCES = [
    ("Toussaint", date(2026, 10, 17), date(2026, 11, 1)),
    ("Noël", date(2026, 12, 19), date(2027, 1, 3)),
    ("hiver", date(2027, 2, 20), date(2027, 3, 7)),
    ("printemps", date(2027, 4, 17), date(2027, 5, 2)),
    ("été", date(2027, 7, 3), date(2027, 8, 31)),
]
# Jours sans classe hors vacances (jours de semaine où il y aurait école).
SANS_CLASSE = {
    date(2026, 11, 11): "jour férié",
    date(2027, 3, 29): "lundi de Pâques",
    date(2027, 5, 6): "Ascension",
    date(2027, 5, 7): "pas de classe",
    date(2027, 5, 17): "lundi de Pentecôte",
}

ECOLE = "à l'école de 8 h 30 à 12 h et de 13 h 30 à 16 h 30"
SEVERINE = "chez Séverine"
MAISON = "à la maison"

# Planning d'Aline par semaine et par jour (0 = lundi). None = ne rien annoncer.
ALINE = {
    "A": {0: "est en repos", 1: "travaille de 9 h à 19 h 15", 2: "travaille de 9 h à 19 h 15",
          3: "travaille de 9 h à 18 h", 4: "travaille de 9 h à 19 h 15", 5: None,
          6: "ne travaille pas"},
    "B": {0: "travaille de 9 h à 19 h 15", 1: "travaille de 9 h à 19 h 15", 2: "est en repos",
          3: "travaille de 9 h à 19 h 15", 4: "travaille de 9 h à 19 h 15",
          5: "travaille de 9 h à 18 h", 6: "ne travaille pas"},
}
# Apolline : chez Séverine les jours où Aline travaille en semaine, sinon à la maison.
APOLLINE = {
    "A": {0: MAISON, 1: SEVERINE, 2: SEVERINE, 3: SEVERINE, 4: SEVERINE,
          5: "à la maison avec Thibaut", 6: MAISON},
    "B": {0: SEVERINE, 1: SEVERINE, 2: MAISON, 3: SEVERINE, 4: SEVERINE,
          5: "à la maison avec Thibaut", 6: MAISON},
}
NATATION = {"A": "Mamou", "B": "Aline"}  # accompagnatrice du mercredi


def semaine_ab(d):
    lundi = d - timedelta(days=d.weekday())
    n = (lundi - REF_LUNDI_A).days // 7
    return ("A" if n % 2 == 0 else "B"), lundi


def vacances_du_jour(d):
    for nom, debut, fin in VACANCES:
        if debut <= d <= fin:
            return nom
    return None


def lire_dates(chemin):
    lignes = []
    try:
        texte = chemin.read_text(encoding="utf-8")
    except OSError:
        return None
    for ligne in texte.splitlines():
        m = re.match(r"^\|\s*(\d{2})-(\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$", ligne)
        if not m:
            continue
        mois, jour, typ, qui, detail = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4), m.group(5)
        moi = "moi/thibaut" in qui
        qui_propre = re.sub(r"\s*\([^)]*\.md\)", "", qui).strip()
        annee = re.search(r"n[ée]{1,2}e? en (\d{4})", detail)
        lignes.append({"mois": mois, "jour": jour, "type": typ.lower(), "qui": qui_propre,
                       "moi": moi, "annee": int(annee.group(1)) if annee else None})
    return lignes


def date_dans_annee(mois, jour, annee):
    try:
        return date(annee, mois, jour)
    except ValueError:
        return None  # 29 février les années non bissextiles


def phrase_evenement(e, d_event):
    if e["type"].startswith("anniversaire") and e["type"] == "anniversaire":
        age = ""
        if e["annee"]:
            n = d_event.year - e["annee"]
            age = f" ({n} an{'s' if n > 1 else ''})"
        if e["moi"]:
            return f"ton anniversaire{age}"
        return f"anniversaire de {e['qui']}{age}"
    if e["type"] == "fête":
        return f"fête : {e['qui']}"
    return f"{e['type']} : {e['qui']}"


def anniversaires(d, evenements):
    aujourdhui, prochains = [], []
    for e in evenements:
        for delta in range(0, 8):
            cible = d + timedelta(days=delta)
            if (cible.month, cible.day) == (e["mois"], e["jour"]):
                texte = phrase_evenement(e, cible)
                if delta == 0:
                    aujourdhui.append(texte)
                else:
                    jour_sem = JOURS[cible.weekday()]
                    quand = "demain" if delta == 1 else f"dans {delta} jours, {jour_sem} {cible.day} {MOIS[cible.month - 1]}"
                    prochains.append({"dans_jours": delta, "quand": quand, "evenement": texte})
    prochains.sort(key=lambda x: x["dans_jours"])
    return aujourdhui, prochains


def menage_suspendu(d, lundi, evenements):
    fin = lundi + timedelta(days=6)
    for e in evenements:
        if e["type"] == "échéance" and "ménage" in e["qui"].lower():
            for annee in (lundi.year, fin.year):
                cible = date_dans_annee(e["mois"], e["jour"], annee)
                if cible and lundi <= cible <= fin:
                    return True
    return False


def planning(d):
    sem, lundi = semaine_ab(d)
    jr = d.weekday()
    vac = vacances_du_jour(d)
    sans_classe = SANS_CLASSE.get(d)
    ecole_ce_jour = jr in (0, 1, 3, 4) and not vac and not sans_classe

    phrases = []
    aline = ALINE[sem][jr]
    if aline:
        phrases.append(f"Aline {aline}.")
    phrases.append(f"Apolline est {APOLLINE[sem][jr]}.")

    if ecole_ce_jour:
        phrases.append(f"Faustine est {ECOLE}.")
        if jr == 4:
            phrases.append("Hand de Faustine de 17 h 15 à 18 h 15 : tu emmènes aussi Emma et Soline.")
    elif jr == 2 and not vac:
        phrases.append(f"Faustine n'a pas école, elle a natation ce matin avec {NATATION[sem]}.")
    elif vac and jr < 5:
        phrases.append(f"Vacances de {vac} : Faustine n'a pas école, centre de loisirs ou chez Mamou.")
    elif sans_classe and jr < 5:
        phrases.append(f"Faustine n'a pas école aujourd'hui ({sans_classe}).")
    elif jr >= 5:
        phrases.append("Faustine n'a pas école.")

    if jr == 1 and not vac and aline and aline.startswith("travaille"):
        phrases.append("Badminton d'Aline à 20 h.")

    # Veille de rentrée
    demain = d + timedelta(days=1)
    if vacances_du_jour(d) and not vacances_du_jour(demain) and demain.weekday() < 5:
        phrases.append("Demain, c'est la rentrée : Faustine reprend l'école.")

    return {"semaine": sem, "lundi_de_la_semaine": lundi.isoformat(),
            "vacances": vac, "jour_sans_classe": sans_classe, "phrases": phrases}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="AAAA-MM-JJ (test)")
    args = ap.parse_args()
    if args.date:
        try:
            d = datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            print(json.dumps({"statut": "ÉCHEC", "erreur": "date invalide"}))
            return 1
    else:
        d = datetime.now(ZoneInfo("Europe/Paris")).date()

    racine = Path(__file__).resolve().parent.parent
    evenements = lire_dates(racine / "dates.md")
    p = planning(d)
    sortie = {
        "statut": "OK",
        "date": d.isoformat(),
        "jour": JOURS[d.weekday()],
        "date_lisible": f"{JOURS[d.weekday()]} {d.day} {MOIS[d.month - 1]} {d.year}",
        "planning_famille": p,
        "rappels_maison": [],
        "anniversaires_aujourdhui": [],
        "anniversaires_prochains_7_jours": [],
    }
    if evenements is None:
        sortie["note_technique"] = "dates.md illisible"
    else:
        today, prochains = anniversaires(d, evenements)
        sortie["anniversaires_aujourdhui"] = today
        sortie["anniversaires_prochains_7_jours"] = prochains
        suspendu = menage_suspendu(d, d - timedelta(days=d.weekday()), evenements)
    if evenements is None:
        suspendu = False
    if not suspendu:
        if d.weekday() == 2:
            sortie["rappels_maison"].append("Ce soir, rangement de la maison : la femme de ménage passe demain.")
        elif d.weekday() == 3:
            sortie["rappels_maison"].append("La femme de ménage passe cet après-midi, de 14 h à 17 h 30.")
    print(json.dumps(sortie, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
