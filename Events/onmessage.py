import json
import config_file
import discord
import aiohttp
import os
from redvid import Downloader
from SQL import text


# Downloads the reddit video
from Useful import reactcommand, messagereply


async def downloadreddit(url, channel, link):
    reddit = Downloader(max_q=True, path=config_file.tempfile_path)
    reddit.log = False
    reddit.overwrite = True
    reddit.url = url
    reddit.check()
    if reddit.size <= 5 * (1 << 20):
        reddit.download()
    else:
        await channel.send('The video was too big, this is the url: ' + link.replace('.json', ''))
        return 5


# Sends the meme from the reddit post
async def sendmeme(author, channel, link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            test = await response.read()
            data = json.loads(test)
    subreddit = "https://www.reddit.com/r/" + data[0]['data']['children'][0]['data']['subreddit']
    if 'gallery_data' in data[0]['data']['children'][0]['data']:
        await channel.send('Meme sent by ' + author.display_name + " from subbreddit: " + subreddit + '.')
        for item in data[0]['data']['children'][0]['data']['gallery_data']['items']:
            url = 'https://i.redd.it/' + str(item['media_id']) + '.png'
            await channel.send(url)
    elif 'crosspost_parent_list' in data[0]['data']['children'][0]['data']:
        link = data[0]['data']['children'][0]['data']['crosspost_parent_list'][0]['permalink']
        url = 'https://www.reddit.com' + link + '.json'
        await sendmeme(author, channel, url)
    else:
        url = data[0]['data']['children'][0]['data']['url']
        # Checks if it is a video instead of an image and gets the right url instead, so the video can be sent
        if 'v.redd.it' in url:
            filesize = await downloadreddit(url, channel, link)
            if filesize != 5:
                filename = os.listdir(config_file.tempfile_path)
                filepath = config_file.tempfile_path + filename[0]
                os.rename(filepath, config_file.tempmp4_path)
                await channel.send('Meme sent by ' + author.display_name + " from subbreddit: " + subreddit + '.')
                await channel.send(file=discord.File(config_file.tempmp4_path))
                os.remove(config_file.tempmp4_path)
        else:
            await channel.send('Meme sent by ' + author.display_name + " from subbreddit: " + subreddit + '.\n' + url)


async def onmessage(message, emojiguild):
    if message.type == discord.MessageType.reply and message.channel.type != discord.ChannelType.private and '!react' in message.content:
        await reactcommand.reactcommand(message, emojiguild)
    textlist = await text.read()
    # If the bot sees a reddit link in a message, it will try to send the image from this post
    if 'reddit.com' in message.content and not message.author.bot:
        link = message.content
        # If the link  is shared via a phone we need to change the link so we can use it
        if 'source=share' in link:
            if 'android' in link:
                link = link.replace(config_file.android_path, '.json')
            else:
                link = link.replace(config_file.ios_path, '.json')
        # Otherwise we just put.json behind it to get the link we need
        else:
            link += '.json'
        await sendmeme(message.author, message.channel, link)
    i = 0
    # This part is for giving the users points for sending messages
    # If the list is empty, it will add the first user
    if message.channel.type != discord.ChannelType.private:
        if len(textlist) == 0 and not message.author.bot:
            textlist.append({'userid': message.author.id, 'score': 1, 'serverid': message.channel.guild.id})
            await text.write(textlist[0]["userid"], textlist[0]["score"], textlist[0]["serverid"])
        while i < len(textlist) and not message.author.bot:
            if textlist[i]['userid'] == message.author.id and textlist[i]['serverid'] == message.channel.guild.id:  # Checks if a user is already in the bot.leaderboardtext list
                textlist[i]['score'] += 1
                await text.update(textlist[i]["userid"], textlist[i]["score"], textlist[i]["serverid"])
                i = len(textlist)
            elif i == len(
                    textlist) - 1:  # If the code gets to the end of the list without finding the user, it adds the user to the list
                textlist.append({'userid': message.author.id, 'score': 1, 'serverid': message.channel.guild.id})
                i += 1
                await text.write(textlist[i]["userid"], textlist[i]["score"], textlist[i]["serverid"])
            else:
                i += 1
    messagestring = message.content.lower()
    if message.channel.type != discord.ChannelType.private:
        if 'execute order 69' in messagestring:
            userid = messagestring.split('execute order 69 ')[1]
            userid = userid.replace('@!', '')
            userid = userid.replace('<', '')
            userid = userid.replace('>', '')
            user = message.guild.get_member(int(userid))
            if user.voice:
                await message.channel.send('Roger, roger')
                await user.move_to(None)
        messagestring = messagestring.replace("'", '')
        # This part is for responding to certain keywords found in messages
        if not message.author.bot:
            await messagereply.messagereply(message, messagestring)
        else:
            return
    else:
        return