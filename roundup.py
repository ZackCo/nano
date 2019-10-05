import re


def roundup(message, pins):
    pinsInMessage = {}
    currentChannel = message.channel

    # Remove a certain post about being sure to read the rules from the list
    for i in pins:
        if i.id == 629845156169777153: pins.remove(i)

    # This block puts everything in a dict for me to grab later
    for pinnedMessage in pins:
        listOfReactions = pinnedMessage.reactions
        listOfLines = pinnedMessage.content.split('\n')
        author = listOfLines[0]
        possibleRealAuthor = ''

        for line in listOfLines:
            if listOfLines.index(
                    line) <= 3:  # Kind of arbitrarily chosen? Not like beginning of a codeblock would be past line 4
                if "```" in line:
                    strippedTitle = line.strip("```")
                    if strippedTitle != "":  # if line has title on it, make stripped version title
                        titleOfRip = strippedTitle
                    elif strippedTitle == "":
                        indexToUse = listOfLines.index(line)
                        titleOfRip = listOfLines[(indexToUse + 1)]

        if re.match('[bB][yY]\s+[mM][eE]\W', author):
            possibleRealAuthor = (' (' + str(pinnedMessage.author) + ')')

        # Back to doing things related to the dict.
        pinsInMessage[titleOfRip] = {}
        pinsInMessage[titleOfRip]['Reactions'] = listOfReactions
        pinsInMessage[titleOfRip]['Author'] = author
        pinsInMessage[titleOfRip]['possibleRealAuthor'] = possibleRealAuthor

    result = ""

    for rip in pinsInMessage.items():
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
            reacts += (str(element) + " ")  # add all of the reacts together

        trueAuthor = (" [" + trueAuthor + "]" + possibleTrueAuthor)  # add the author

        formattedRipLine = (
                    "**" + rip[0] + "**" + "  |  " + reacts + trueAuthor + "\n")  # A single line, representing a rip
        result += formattedRipLine

    result += "\n`Total: " + str(len(pinsInMessage.items())) + "`"

    return result
