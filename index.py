from telethon import TelegramClient, events

api_id = 
api_hash = ''

print('')

client = TelegramClient('session_name', api_id, api_hash)

print('')
channelFrom = input("Masukan username channel yang akan diforward ex. @airdropermaniax,@airdroper : ")
channelTo = input("Masukan username channel tujuan ex @etlbsc_info_bot : ")


if channelFrom.find(',') != -1:
    channelFrom = channelFrom.split(',')
else:
    channelFrom = [channelFrom]

client.start()

@client.on(events.NewMessage(chats=channelFrom))
async def my_event_handler(event):
   await client.send_message(channelTo, event.message)


client.run_until_disconnected()
    