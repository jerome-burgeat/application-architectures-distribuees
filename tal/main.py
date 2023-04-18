import os
import os.path
import sys
import re
from pathlib import Path
from flask import Flask, jsonify, request

app = Flask(__name__)
sys.path.append(os.getcwd())

#text = "Monte le son et joue-moi une musique."
listeDesActions = []


def isDossierExiste(fichier):
    chemin_access = Path(os.getcwd() + "\\ressources\\" + fichier)
    #print(chemin_access.exists())
    if chemin_access.exists():
        return True
    return False


def FichierAListe(fichier):
    """
    Search if the file exists in ressources depending on the language and the filename
    :param name:
    :param language:
    """
    chemin_access = Path(os.getcwd() + "\\ressources\\" + fichier)
    lignes = []
    if isDossierExiste(fichier) :
        with open(chemin_access, 'r') as file:
            for ligne in file:
                lignes.append(ligne.strip())
    return lignes


def adaptationDuTexte(phrase):
    """
    Remove unnecessary characters : [',' , '.']
    @:param word
    @:return String
    """
    phrase = phrase.lower()
    if phrase.__contains__(','):
        phrase = phrase.replace(',', '')
    if phrase.__contains__('.'):
        phrase = phrase.replace('.', '')
    return phrase


def searchWordInListRegex(mot, liste):
    """
    Search if a word is in a array
    :param mot:
    :param liste:
    :return: boolean
    """
    mot = mot.replace('\n', '')
    combined = "(" + ")|(".join(liste) + ")"
    if re.search(combined, mot.lower()):
        return True
    return False


def regexActionAndObjet():
    liste_objet = []
    liste_action = []
    for mot in FichierAListe("objet"):
        if mot:
            liste_objet.append(mot.split(" @@ ")[0])
            liste_action.append(mot.split(" @@ ")[1])
    return liste_objet, liste_action


def trouverUnMot(mot, phrase) :
    if re.search(r'\b' + mot + r'\b', phrase):
        #print(f'Le mot "{mot}" a été trouvé dans la phrase.')
        return True
    else:
        #print(f'Le mot "{mot}" n\'a pas été trouvé dans la phrase.')
        return False

@app.route('/api/tal', methods=['GET'])
def tal():
    listeDesActions.clear()
    texte = request.args.get('requete')
    print(adaptationDuTexte(texte))
    liste_objets, liste_actions = regexActionAndObjet()
    compteur = 0
    for mot in liste_objets:
        # print(mot)
        if trouverUnMot(mot, adaptationDuTexte(texte)):
            # print(liste_actions[compteur])
            listeDesActions.append(liste_actions[compteur])
        compteur += 1

    #for category in listOfAction:
    #    print(category)
    return jsonify({'Action': listeDesActions})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')