import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

pinsInMessage = {
}

#This code is less messy than before! props to vince.

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Execute the command, gather all of the pins into a list
    if message.content.lower().startswith('/roundup'):
      currentChannel = message.channel
      pinList = await currentChannel.pins()

      #Remove Matsu's post about being sure to read the rules from the list
      for i in pinList:
        if i.id == 302481260188532736: pinList.remove(i)
      
      #This block puts everything in a dict for me to grab later
      for pinnedMessage in pinList:
        mesg = await currentChannel.fetch_message(pinnedMessage.id)
        listOfReactions = mesg.reactions
        listOfLines = pinnedMessage.content.split('\n')
        author = listOfLines[0]
  
        for line in listOfLines:
          if "Music:" in line:
            indexToSubtractFrom = listOfLines.index(line) - 1
        
        titleOfRip = listOfLines[indexToSubtractFrom].replace("```", "")

      #Sometimes there's one space between the title and "Music:" descriptor.
        if not listOfLines[indexToSubtractFrom].strip(): #Check if the line is empty or whitespace
          titleOfRip = listOfLines[indexToSubtractFrom - 1] #And remove it
      
      #Back to doing things related to the dict.
        pinsInMessage[titleOfRip] = {}
        pinsInMessage[titleOfRip]['Reactions'] = listOfReactions
        pinsInMessage[titleOfRip]['Author'] = author
      totes = 0
      result = ("")

      #Getting everything sorted out for putting into the message.
      for rip in pinsInMessage.items():
        totes += 1 #This will be a count of how many rips are pinned
        listToMessWith = rip[1]
        trueAuthor = listToMessWith['Author'].replace("**", "")

        reactsToWorkWith = listToMessWith['Reactions']
        reactsCatalogue = []
        
        reacts = ''
        author = ''

        for i in range(len(reactsToWorkWith)):
          changer = reactsToWorkWith[i].emoji

          for i in range(reactsToWorkWith[i].count):
            reactsCatalogue.append(changer)

        for element in reactsCatalogue:
          reacts += (str(element) + " ") #add all of the reacts

        trueAuthor = (" [" + trueAuthor + "]") #add the author
        
        formattedRipLine = ("**" + rip[0] + "**" + "  |  " + reacts + trueAuthor + "\n") #A single line, representing a rip
        result += formattedRipLine

      result += ("\n`Total: " + str(totes) + "`")
      await message.channel.send(result)
client.run('insert_token_here')
