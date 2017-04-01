import discord
import time
import random
import sys
import config
client = discord.Client()

@client.event
async def on_ready():
	await send()



async def send():
	kanaal =  client.get_channel(config.channel)
	message = config.message
	aantal = config.count
	count = 0
	while (count < aantal):
		number = str(random.randint(1, 9)) #Every message ends with a random number. You can get banned for sending the same message over and over. So this way all the messages are slightly different
		await client.send_message(kanaal, (message + " " + number))
		count = count + 1
	opnieuw = input("# Wanna spam again? (Y/n)")
	if opnieuw == 'Y' or 'y':
		await send()
	else:
		print("! OK. You can close this window now.")

client.run("token", bot=False)
