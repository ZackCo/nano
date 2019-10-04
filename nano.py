import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

pinsInMessage = {
}

#This code is so messy. Let me just remind myself what I'm doing.

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Executing the command, getting everything in the pin list.
    if message.content.startswith('/roundup'):
      currentChannel = message.channel
      pinList = await currentChannel.pins()

      #If the message ID is equal to Matsu's post, remove it from the pin list.
      for i in pinList:
        if i.id == 302481260188532736:
          pinList.remove(i)
      
      #This block puts everything in a dict for me to grab later.
      for i in pinList:
        mesg = await currentChannel.fetch_message(i.id)
        listOfReactions = mesg.reactions
        listOfLines = i.content.split('\n')
        author = listOfLines[0]
  
        for i in listOfLines:
          if "Music:" in i:
            indexToSubtractFrom = listOfLines.index(i) - 1
        
        titleOfRip = listOfLines[indexToSubtractFrom].replace("```", "")

      #Sometimes there's one space between the title and "Music:" descriptor.
        if listOfLines[indexToSubtractFrom] == "":
          titleOfRip = listOfLines[indexToSubtractFrom - 1]
      
      #Back to doing things related to the dict.
        pinsInMessage[titleOfRip] = {}
        pinsInMessage[titleOfRip]['Reactions'] = listOfReactions
        pinsInMessage[titleOfRip]['Author'] = author
      totes = 0
      trueMessage = ("")

      #Getting everything sorted out for putting into the message.
      for x in pinsInMessage.items():
        totes += 1
        listToMessWith = x[1]
        trueAuthor = listToMessWith['Author'].replace("**", "")

        reactsToWorkWith = listToMessWith['Reactions']
        reactsCatalogue = []
        nettle = ''

        for i in range(len(reactsToWorkWith)):
          changer = reactsToWorkWith[i].emoji

          for i in range(reactsToWorkWith[i].count):
            reactsCatalogue.append(changer)

        for element in reactsCatalogue:
          nettle += (str(element) + " ")

        nettle += (" [" + trueAuthor + "]")
        msgLine = ("**" + x[0] + "**" + "  |  " + nettle + "\n" + "\n")
        trueMessage += msgLine

      trueMessage += ("`Total: " + str(totes) + "`")
      await message.channel.send(trueMessage)
client.run('insert_token_here')
