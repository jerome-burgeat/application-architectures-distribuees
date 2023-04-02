import os
import os.path
import sys
import re
from pathlib import Path

sys.path.append(os.getcwd())

text = "Monte le son et joue-moi une musique."
listOfAction = []


def verifyDirectory(filename):
    path = Path(os.getcwd() + "\\ressources\\" + filename)
    #print(path.exists())
    if path.exists():
        return True
    return False


def FileIntoList(filename):
    """
    Search if the file exists in ressources depending on the language and the filename
    :param name:
    :param language:
    """
    path = Path(os.getcwd() + "\\ressources\\" + filename)
    lines = []
    if(verifyDirectory(filename)) :
        with open(path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    return lines


def adaptText(word):
    """
    Remove unnecessary characters : [',' , '.']
    @:param word
    @:return String
    """
    word = word.lower()
    if word.__contains__(','):
        word = word.replace(',', '')
    if word.__contains__('.'):
        word = word.replace('.', '')
    return word


def searchWordInListRegex(word, array):
    """
    Search if a word is in a array
    :param word:
    :param array:
    :return: boolean
    """
    word = word.replace('\n', '')
    combined = "(" + ")|(".join(array) + ")"
    if re.search(combined, word.lower()):
        return True
    return False


def regexActionAndObjet():
    wordArray = []
    categoryArray = []
    for word in FileIntoList("objet"):
        if word:
            wordArray.append(word.split(" @@ ")[0])
            categoryArray.append(word.split(" @@ ")[1])
    return wordArray, categoryArray


def findWord(mot, phrase) :
    if re.search(r'\b' + mot + r'\b', phrase):
        #print(f'Le mot "{mot}" a été trouvé dans la phrase.')
        return True
    else:
        #print(f'Le mot "{mot}" n\'a pas été trouvé dans la phrase.')
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(adaptText(text))
    wordArray, categoryArray = regexActionAndObjet()
    compteur = 0
    for word in wordArray:
        #print(word)
        if findWord(word, adaptText(text)):
            #print(categoryArray[compteur])
            listOfAction.append(categoryArray[compteur])
        compteur += 1

    for category in listOfAction:
        print(category)