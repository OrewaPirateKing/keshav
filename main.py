from telethon.sync import events , TelegramClient
from telethon.sessions import StringSession
from asyncio import sleep as zzz
from random import randint
from re import match

session = '1BVtsOHsBuz1mgtoylZvuy8yn_Iuo7HZU-QygomFe_0ZvtXoiazESuxln-AXVPPmdrZvsubFy53VXwooaoTTg8m7-iitt5Oyf8KdbHWbIB5C7uuOrIL7PTTLIQyv15FYsEgQfcpWESVzUEjLwRgubxpnd9xJb1Ae57bqrYt4lNwuTJNxFy_lERf0e-If5k_izTJAR44EfUVX1NeX2U2MTJZm3FmSWluYmf6NbgdpR2jQN0hjdCcKbdk2Fu5wM48K7gjO95ya8E9sSTTm_Zny9l8RdmiChhQ7_krBBzvADZpy9jhSTfdiuz7B3SsjRZntD3K3NsYB1EVpzbbsQzCMean4jSWUXQHY='  # Replace with your actual session string
api_id = 28368399
api_hash = 'dabc0305143936096274b38833384c3d'

# Initialize the TelegramClient with the StringSession
bot = TelegramClient(StringSession(session), api_id, api_hash)
chat = 572621020

#edit the list
list = ["Venusaur", "Charizard", "Blastoise", "Beedrill", "Pidgeot", "Alakazam", "Slowbro", "Gengar", "Kangaskhan", "Pinsir", "Gyarados", "Aerodactyl", "Mewtwo", "Ampharos", "Steelix", "Scizor", "Heracross", "Houndoom", "Tyranitar", "Sceptile", "Blaziken", "Swampert", "Gardevoir", "Sableye", "Mawile", "Aggron", "Medicham", "Manectric", "Sharpedo", "Camerupt", "Altaria", "Banette", "Absol", "Glalie", "Salamence", "Metagross", "Latias", "Latios", "Rayquaza", "Lopunny", "Garchomp", "Lucario", "Abomasnow", "Gallade", "Audino", "Diancie", "Eternatus", "Zacian", "Dialga", "Palkia", "Mewtwo", "Arceus", "Zamazenta", "Glastrier", "Kyurem", "Lunala", "Necrozma", "Cosmoem", "Yveltal", "Kyogre", "Xerneas", "Cosmog", "Groudon", "Giratina", "Zeraora", "Marshadow", "Buzzwole", "Solgaleo"]
@bot.on(events.NewMessage(outgoing=True,pattern='/go'))
async def begin(event):
    global hunt
    hunt = True
    x = await bot.send_message(chat , "/hunt")
    try:  
     async with bot.conversation('@Hexamonbot') as conv:
       await conv.get_response(x.id)
    except:
       await zzz(3,5)
       await bot.send_message(chat , "/hunt")
    for i in range(5,10000):
      await zzz(randint(5000, 6020))
      await bot.send_message(chat , "/hunt")

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
    if hunt == True:
     text = event.message.text
     hun = True
     message = await bot.get_messages(chat, ids=event.message.id)
     if ("Shiny" in text):
        bot.disconnect()
     elif("TM" in text):
        print(event.message.text)
        await zzz(randint(3,5))
        x = await bot.send_message(chat , "/hunt")
        try:  
         async with bot.conversation('@Hexamonbot') as conv:
           await conv.get_response(x.id)
        except:
           await zzz(5,6)
           await bot.send_message(chat , "/hunt")
     elif any(item in text for item in list):
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
     elif("A wild" in text or "An expert" in text):
      if hun == False:
       pass
      else:
       await zzz(randint(3,5))
       x = await bot.send_message(chat , "/hunt")
       try:  
        async with bot.conversation('@Hexamonbot') as conv:
          await conv.get_response(x.id)
       except:
          await zzz(3,5)
          await bot.send_message(chat , "/hunt")
      

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
   print(event.message.text)
   if event.message.text[:13] == "Battle begins":
        message = await bot.get_messages(chat, ids=event.message.id)
        await zzz(21)
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")      


@bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
   message = await bot.get_messages(chat, ids=event.message.id)
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   if event.message.text[:4] == "Wild":
      await zzz(1)
      await message.click(text = "Regular")
      await message.click(text = "Regular")
      await message.click(text = "Regular")
   if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught']):
      await zzz(randint(3,5))
      x = await bot.send_message(chat , "/hunt")
      try:  
       async with bot.conversation('@Hexamonbot') as conv:
         await conv.get_response(x.id)
      except:
         await zzz(3,5)
         await bot.send_message(chat , "/hunt")



@bot.on(events.NewMessage(outgoing=True,pattern='/stop'))
async def stop(event):
    global hunt
    hunt = False


bot.start()
bot.run_until_disconnected()
