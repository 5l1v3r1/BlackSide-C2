import os
import shutil
try:
    import pyarmor
except:
    if os.name == 'nt':
     os.system('pip install pyarmor')    
    else:
        os.system('pip3 install pyarmor') 
    if os.name == 'nt':
     os.system('cls')    
    else:
        os.system('clear') 
filename = input('Имя файла (Без .py): ')
icon = input('Добавить иконку? [д/н]: ')
if icon == 'д' or icon == 'Д':
 ico = input('Иконка (Без .ico): ')
 os.system(f'pyarmor pack -e " --onefile --noconsole --icon {ico}.ico" {filename}.py')
 if os.name == 'nt':
     os.system('cls')    
 else:
        os.system('clear') 
 shutil.rmtree('build')       
 print('В папке dist ваш EXE файл') 
else:
 os.system(f'pyarmor pack -e " --onefile --noconsole" {filename}.py') 
 if os.name == 'nt':
     os.system('cls')    
 else:
        os.system('clear') 
 shutil.rmtree('build')       
 print('В папке dist ваш EXE файл')   