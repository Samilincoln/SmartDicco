from collections.abc import MutableMapping
import asyncio
import telepot
import telepot.aio
from telepot.aio.loop import MessageLoop
from pprint import pprint
from bs4 import BeautifulSoup
import requests

#modification
async def handle(msg):
    global chat_id
    #useful variables
    content_type, chat_type ,chat_id = telepot.glance(msg)
    #Log variables
    print(content_type, chat_type, chat_id)
    #print(msg)
    #username = text['chat']['first_name']
    #checking taht the content type is text and not the starting
    if content_type == 'text':

        text = msg['text']
    #stripping and lower the input
        text= text.strip()
        await getMeaning(text.lower())

async def getMeaning(text):
#creating the url
    url = 'https://www.dictionary.com/browse/' + text
#defining my headers
    headers = {'User-Agent': 'Generic user agent'}
#get page request
    r = requests.get(url, headers=headers )
#to parse the html ...this is the code
    soup = BeautifulSoup(r.content, 'html.parser')

    print(soup.prettify())

    

    try:

        try:
        #finding the required content.....
            s = soup.find('div', class_='css-1avshm7 e16867sm0')
            lines = s.find('span', class_='one-click-content css-nnyc96 e1q3nk1v1')

            for  line in lines:
                await bot.sendMessage(chat_id , line.text)
                print(line) 

        except:
            await bot.sendMessage(chat_id, '....\n',text ,'not found\n please check spelling.')
   
    except:
        await bot.sendMessage(chat_id, 'Something went wrong...\n Word not found or spelling not corect.')
    
    #send our JSON msg as variable ass replly message
    #await bot.sendMessage(chat_id,msg)


#startup
TOKEN = '5492548133:AAGfDi_Q-Lh6XO5pVFOsJbZ5Zbk5VKcrjQE'
bot = telepot.aio.Bot(TOKEN)
loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot, handle).run_forever())

print('Listening .....')

#keep the prog running
loop.run_forever()
