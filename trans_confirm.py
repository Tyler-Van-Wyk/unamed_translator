import os
from translate import Translator
translator=  Translator(to_lang='en',from_lang='ja')

#Function that uses the google translate api to translate a filename in string form
def translate(filename):
               filename_trans = translator.translate(filename)
               return filename_trans

print('Provide the full path of the directory that contains the file/folder names you want to translate.')

path = input()

#Change to directory from input
os.chdir(path)

#Translating each file and rename it to the translated string
for files in os.listdir(path):
    trans_files = translate(files)
    print('"' + files + '"\n' + ' will be translated to: \n' + '"' + trans_files + '"' + '\n proceed? (y/n)')
    answer = input()
    if answer == 'y':
        os.rename(files, trans_files)
    elif answer == 'n':
        continue
    else:
        print('Invalid input. Please answer "y" or "n"')
        continue
