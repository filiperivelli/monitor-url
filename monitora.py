import json
from time import sleep
import requests 
import asyncio

from telegram_monitora import enviar_mensagem

def status(url):
    try:
        response = requests.get('https://'+url)

        # Consider any status other than 2xx an error
        if not response.status_code // 100 == 2:
            return 'offline'

        #json_obj = response.json()
        return 'online'
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        return 'offline'

def main():
    urls_status = {}

    #Opening JSON file
    f = open('urls.json')
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    while 1:
        for url in data['urls']:
            
            if url in urls_status:
                old_status = urls_status[url] 
            else:      
                old_status = 'online'
            
            new_status = status(url) 
            
            if old_status != new_status:
                msg = 'A url {} está {}.'.format(url,new_status)
                print(msg)
                asyncio.run(enviar_mensagem(msg))
        sleep(300)      

    # Closing file
    f.close()

if __name__ == '__main__':    
    main()