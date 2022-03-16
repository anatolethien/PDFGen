import os
import sys
from pychromepdf import ChromePDF

CHROME_PATH = '/opt/google/chrome/chrome' # linux

# input
# dict = {
#     'first_name': 'Jean',
#     'last_name': 'Martin',
#     'sex': 'm'
#     'rank': sex.to_rank(),
#     'address': '14 rue de la Paix',
#     'postal_code': '31000',
#     'city': 'Toulouse',
#     'siren': '123 456 789',
#     'activity': 'Graphisme',
#     'jobs': [
#         'Publicité papier',
#         'Réalisation publicité audiovisuelle'
#     ],
#     'skills': [
#         'Réalisation d\'affiche',
#         'Montage vidéo'
#     ]
# }

def to_rank(sex):
    if sex.lower() == 'm':
        return 'Monsieur'
    else if sex.lower() == 'f':
        return 'Madame'
    else:
        return ''

def get_document(path: str) -> str:
    document = open(path, 'r')
    return document.read()

if __name__ == '__main__':
    cpdf = ChromePDF(CHROME_PATH)
    document = get_document('templates/contract.html')
    with open('contrat.pdf', 'w') as output:
        if cpdf.html_to_pdf(document, output):
            print('PDFGen : Success!')
        else:
            print('PDFGen : Error!')
