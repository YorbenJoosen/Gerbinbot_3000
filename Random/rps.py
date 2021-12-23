import random

from SQL import rockpaperscissors


async def rps(ctx, answer):
    answer = answer.lower()
    rpslist = await rockpaperscissors.read()
    rpsbot = random.choice(['Rock', 'Paper', 'Scissors'])
    await ctx.channel.send(rpsbot)
    i = 0
    while i < len(rpslist):
        if ctx.message.author.id == rpslist[i]['userid']:  # Checks if the user is already in the list
            # This part looks at who wins
            if answer == 'rock' and rpsbot.lower() == 'paper':
                rpslist[i]['botpoints'] += 1
            elif answer == 'paper' and rpsbot.lower() == 'scissors':
                rpslist[i]['botpoints'] += 1
            elif answer == 'scissors' and rpsbot.lower() == 'rock':
                rpslist[i]['botpoints'] += 1
            elif answer != rpsbot.lower():
                rpslist[i]['userpoints'] += 1
            if rpslist[i]['botpoints'] == 3 or rpslist[i]['userpoints'] == 3:  # If the user or the bot has 3 points, the winner is declared
                if rpslist[i]['botpoints'] == 3:  # Checks who won and also resets their values
                    await ctx.channel.send('Bot has won with score ' + str(rpslist[i]['botpoints']) + '-' + str(
                        rpslist[i]['userpoints']))
                    rpslist[i]['userpoints'] = 0
                    rpslist[i]['botpoints'] = 0
                else:
                    await ctx.channel.send(ctx.message.author.display_name + ' has won with score ' + str(
                        rpslist[i]['userpoints']) + '-' + str(rpslist[i]['botpoints']))
                    rpslist[i]['userpoints'] = 0
                    rpslist[i]['botpoints'] = 0
            await rockpaperscissors.update(rpslist[i]['userid'], rpslist[i]['userpoints'], rpslist[i]['botpoints'])
            i = len(rpslist)
        elif i == len(rpslist) - 1:  # If the code gets to the end of the list, it will add the user
            rpslist.append({'userid': ctx.message.author.id, 'userpoints': 0, 'botpoints': 0})
            i += 1
            if answer == 'rock' and rpsbot.lower() == 'paper':
                rpslist[i]['botpoints'] += 1
            elif answer == 'paper' and rpsbot.lower() == 'scissors':
                rpslist[i]['botpoints'] += 1
            elif answer == 'scissors' and rpsbot.lower() == 'rock':
                rpslist[i]['botpoints'] += 1
            elif answer != rpsbot.lower():
                rpslist[i]['userpoints'] += 1
            i = len(rpslist)
            await rockpaperscissors.write(rpslist)
        else:
            i += 1