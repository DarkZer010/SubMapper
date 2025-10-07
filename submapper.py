import requests
from colorama import init, Fore
import os
from datetime import datetime

from threading import Thread
import pyfiglet
import sys 
import time

init()

os.system("cls" if sys.platform == "win32" else "clear")

def banner():
    print(Fore.CYAN+pyfiglet.figlet_format("SubMapper"))
    
    print(Fore.RED+"Press CTRL'C OR 'sair' TO EXIT\n")
    print(Fore.YELLOW+"Author:", Fore.WHITE+"DarkZer0")
    print(Fore.YELLOW+"Github:", Fore.WHITE+"https://github.com/DarkZer0")
    print(Fore.YELLOW+"Source:", Fore.WHITE+"https://github.com/DarkZer0/SubMapper\n")
    time.sleep(1)
    
banner()

def submapper():
    try:
        subdominios = ["blog", "loja", "admin", "suporte", "dev", "pt", "en", "info", "music", "es", "help", "js", "login", "business", "docs", "support", "news", "media", "shop", "checkout", "staging", "test", "projeto", "project", "fr", "api", "app", "forum", "community", "dashboard", "panel"]
        
        url_base = input(Fore.BLUE+"Digite a url (sem https/http): ")
        
        if url_base == "sair":
            print(Fore.RED+"você saiu")
            time.sleep(2)
            exit()
            
        print("\n")
        
        tempo_comeco = time.time()

        for subdom in subdominios:
            url = f"http://{subdom}.{url_base}"
        
            try:
                response = requests.get(url, timeout=3)
               
                if response.status_code == 200:
                    print(Fore.GREEN+f"\nsubdominio disponivel: {url}\n")
            
            except requests.exceptions.RequestException as e:
                print(Fore.RED+f"erro ao acessar: {url}")

    
    except Exception as e:
        print(Fore.RED+f"erro: {e}")
        time.sleep(2)
        exit()
        
    print(Fore.CYAN+"data:", datetime.now())

    tempo_fim = time.time()
    
    total_tempo = int(tempo_fim -tempo_comeco)
    h, remainder = divmod(total_tempo, 3600)
    m, s = divmod(remainder, 60)

    print(Fore.CYAN+f"tempo de execução: {h}h {m}m {s}s\n")

if __name__=="__main__":
    Thread(target=submapper).start() 
    
