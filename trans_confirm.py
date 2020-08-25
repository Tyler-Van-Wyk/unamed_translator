import os
from googletrans import Translator
translator = Translator()

#Function that takes in a filepath as an argument and returns it translated into english
def translate(filename):
               filename_trans = translator.translate(filename)
               return filename_trans.text
#Initial input prompt
print('Provide the full path of the directory that contains the file/folder names you want to translate.')

path = input()

#Change to directory from input
os.chdir(path)

#Translating each file and rename it to the translated string
for files in os.listdir(path):
    trans_files = translate(files)
    print('"' + files + '"\n' + ' will be translated to: \n' + '"' + trans_files + '"' + '\n proceed? (y/n)')
    while True:   #UI logic
        answer = input()
        if answer.lower() == 'y' or answer.lower() == 'yes':
            os.rename(files, trans_files)
            break
        elif answer.lower() == 'n' or answer.lower() == 'no':
            break
        else:
            print('Invalid input. Please answer "y" or "n"')
            continue
