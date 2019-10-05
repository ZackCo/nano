import discord
from roundup import roundup

client = discord.Client()

bindings = [
	{"name": "roundup", "channel": "qoc", "function": roundup}
]

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

#This code is less messy than before! props to vince.

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	for binding in bindings:
		if message.content.lower().startswith('/' + binding["name"]) and str(message.channel) == binding["channel"]:
			await message.channel.send(binding["function"](message, await message.channel.pins()))

#Requires a file "token" with a Discord OAuth2 token
with open('token') as token:
	client.run(token.readline())