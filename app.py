import os
import sys
from pychromepdf import ChromePDF

CHROME_PATH = '/opt/google/chrome/chrome'
# CHROME_PATH = os.path.expandvars(r'%ProgramFiles%\Google\Chrome\Application\chrome.exe')

# def get_chrome_path() -> str:
#     if sys.platfrom == "linux":
#         return "/opt"

def get_document(path: str) -> str:
    document = open(path, 'r')
    return document.read()

if __name__ == '__main__':
    cpdf = ChromePDF(CHROME_PATH)
    document = get_document('templates/contract.html')
    with open('contrat.pdf', 'w') as output:
        if cpdf.html_to_pdf(document, output):
            print('Success!')
        else:
            print('Error!')
