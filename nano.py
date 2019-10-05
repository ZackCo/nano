import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

#This code is less messy than before! props to vince.

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.lower().startswith('/roundup'):
		pinsInMessage = {
		}
		currentChannel = message.channel
		pinList = await currentChannel.pins()

		#Remove a certain post about being sure to read the rules from the list
		for i in pinList:
			if i.id == 629845156169777153: pinList.remove(i)

		#This block puts everything in a dict for me to grab later
		for pinnedMessage in pinList:
			mesg = await currentChannel.fetch_message(pinnedMessage.id)
			listOfReactions = mesg.reactions
			listOfLines = pinnedMessage.content.split('\n')
			author = listOfLines[0]
			possibleRealAuthor = ''

			for line in listOfLines:
				if listOfLines.index(line) <= 3: #Kind of arbitrarily chosen? Not like beginning of a codeblock would be past line 4
					if "```" in line:
						strippedTitle = line.strip("```")
						if strippedTitle != "": #if line has title on it, make stripped version title
							titleOfRip = strippedTitle
						elif strippedTitle == "":
							indexToUse = listOfLines.index(line)
							titleOfRip = listOfLines[(indexToUse + 1)]

			if 'by me' in author:
				possibleRealAuthor = (' (' + str(mesg.author) + ')')

			#Back to doing things related to the dict.
			pinsInMessage[titleOfRip] = {}
			pinsInMessage[titleOfRip]['Reactions'] = listOfReactions
			pinsInMessage[titleOfRip]['Author'] = author
			pinsInMessage[titleOfRip]['possibleRealAuthor'] = possibleRealAuthor

		totes = 0
		result = ("")

		for rip in pinsInMessage.items():
			totes += 1 #This will be a count of how many rips are pinned
			listToMessWith = rip[1]
			trueAuthor = listToMessWith['Author'].replace("**", "")
			possibleTrueAuthor = listToMessWith['possibleRealAuthor']
			reactsToWorkWith = listToMessWith['Reactions']
			reactsCatalogue = []

			reacts = ''
			author = ''

			for i in range(len(reactsToWorkWith)):
				changer = reactsToWorkWith[i].emoji

				for i in range(reactsToWorkWith[i].count):
					reactsCatalogue.append(changer)

			for element in reactsCatalogue:
				reacts += (str(element) + " ") #add all of the reacts together

			trueAuthor = (" [" + trueAuthor + "]" + possibleTrueAuthor) #add the author

			formattedRipLine = ("**" + rip[0] + "**" + "  |  " + reacts + trueAuthor + "\n") #A single line, representing a rip
			result += formattedRipLine

		result += ("\n`Total: " + str(totes) + "`")
		await message.channel.send(result)

client.run('NTY0ODExNjEyNjk1ODIyMzQ4.XZgDRg.0SKQYLHEaHI2z3WIa1OYsqdV064')
