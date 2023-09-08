"""
Exercise 2
Create a Python program that reads a text file and counts the occurrences of each
word using a dictionary. The program should print the words and their counts.
"""
import json, re
class CountWords:
    def __init__(self, text):
        # Se pueden combinar las 2 sustituciones en un solo regex
        self.text = re.sub(r'\n', '', text)
        self.text = re.sub(r'\t','', self.text)

    def clean_marks(self, punctuation_marks):
        # Tambien se puede usar re.sub para limpiar los signos de puntuacion
        #self.list_words = list(self.text)
        words = self.text
        words = words.split(" ")  # O simplemente "words = self.text.split()"
        self.list_words = []
        for word in words:
            if word != "":
                w = word
                for letter in word:
                    if letter in punctuation_marks:
                        w = w.replace(letter, '')
                self.list_words.append(w)
        return self.list_words

    def organize_words(self, dict_clvowels):
        dictionary = {}
        for word in dict_clvowels:
            if word.lower() in dictionary:
                dictionary[word.lower()] += 1
            else:
                dictionary[word.lower()] = 1
        return dictionary

    def clean_vowels(self, vowels, **dict_clmarks):
        # Al final las vocales en ingles se usan como palabras, no crees?
        for vowel in vowels:
            if vowel in dict_clmarks:
                del dict_clmarks[vowel]
        return dict_clmarks

with open ('text_adv_py_conc_2.txt', 'r') as file:
    text = file.read()

text_file  = CountWords(text)
punctuation_marks = ['.', ',', '-', '"', ':', '!', '?']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
list_clmarks = text_file .clean_marks(punctuation_marks)
dictionary_words = text_file.organize_words(list_clmarks)
final_dictionary = text_file.clean_vowels(vowels, **dictionary_words)
with open('final_file.json', 'w') as file:
    json.dump(dictionary_words, file, indent=4)


# OBSERVACIONES
# Seguir guia de estilos de codigo python PEP8: Espacios despues de las comas, dos lineas
# vacias antes y despues de definir una funcion, espacio despues de # en los comentarios
#  ... https://peps.python.org/pep-0008/

# Seria bueno tener bien documentado el codigo, con anotaciones de tipo, docstring, comentarios, ...
