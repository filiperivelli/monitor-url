import json
from time import sleep
import requests 
import asyncio

from telegram_monitora import enviar_mensagem

def return_json(url):
    try:
        response = requests.get('https://'+url)

        # Consider any status other than 2xx an error
        if not response.status_code // 100 == 2:
            return "Error: Unexpected response {}".format(response)

        #json_obj = response.json()
        return 'Ok'
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        return "Error: {}".format(e)

def main():
    #Opening JSON file
    f = open('urls.json')
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    while 1:
        for url in data['urls']:
            print("\nFetching URL {}".format(url))
            print(return_json(url))
            asyncio.run(enviar_mensagem(return_json(url)))
        sleep(300)      

    # Closing file
    f.close()

if __name__ == '__main__':    
    main()