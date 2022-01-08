import json
import config_file
import discord
import audioread
import asyncio
import aiohttp
import datetime
import os
from redvid import Downloader
from SQL import text


# Downloads the reddit video
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


# Function to check how the bot should respond
async def checkwordreaction(splitter, reactionemoji, messagestring, message, filename, reactionmessage):
    messagestring = messagestring.split(splitter)
    spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
    spacepos2 = messagestring[1].find(' ')
    if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (
            messagestring[1] == '' or spacepos2 == 0):
        if reactionemoji != 'None':
            await message.add_reaction(reactionemoji)
        if reactionmessage != 'None':
            await message.channel.send(reactionmessage)
        if filename != 'None':
            await message.channel.send(file=discord.File(filename))


async def onmessage(message):
    if discord.MessageType.reply and '!react' in message.content:
        channel = message.channel
        content = message.content.split(' ')
        if len(content) > 1:
            try:
                referenceid = message.reference.message_id
                reference = await channel.fetch_message(referenceid)
                await message.delete()
                content = content[1]
                content = content.lower()
                if len(content) > 20:
                    length = 20
                else:
                    length = len(content)
                a = 0
                b = 0
                c = 0
                i = 0
                m = 0
                o = 0
                p = 0
                r = 0
                t = 0
                x = 0
                for iterator in range(0, length):
                    character = content[iterator]
                    if character == 'a':
                        if a == 0:
                            await reference.add_reaction('🇦')
                            a += 1
                        elif a == 1:
                            await reference.add_reaction('🅰️')
                            a += 1
                    elif character == 'b':
                        if b == 0:
                            await reference.add_reaction('🇧')
                            b += 1
                        elif b == 1:
                            await reference.add_reaction('🅱️')
                            b += 1
                    elif character == 'c':
                        if c == 0:
                            await reference.add_reaction('🇨')
                            c += 1
                        elif c == 1:
                            await reference.add_reaction('©️')
                            c += 1
                    elif character == 'd':
                        await reference.add_reaction('🇩')
                    elif character == 'e':
                        await reference.add_reaction('🇪')
                    elif character == 'f':
                        await reference.add_reaction('🇫')
                    elif character == 'g':
                        await reference.add_reaction('🇬')
                    elif character == 'h':
                        await reference.add_reaction('🇭')
                    elif character == 'i':
                        if i == 0:
                            await reference.add_reaction('🇮')
                            i += 1
                        elif i == 1:
                            await reference.add_reaction('ℹ️')
                            i += 1
                    elif character == 'j':
                        await reference.add_reaction('🇯')
                    elif character == 'k':
                        await reference.add_reaction('🇰')
                    elif character == 'l':
                        await reference.add_reaction('🇱')
                    elif character == 'm':
                        if m == 0:
                            await reference.add_reaction('🇲')
                            m += 1
                        elif m == 1:
                            await reference.add_reaction('Ⓜ️')
                            m += 1
                        elif m == 2:
                            await reference.add_reaction('〽️')
                            m += 1
                    elif character == 'n':
                        await reference.add_reaction('🇳')
                    elif character == 'o':
                        if o == 0:
                            await reference.add_reaction('🇴')
                            o += 1
                        elif o == 1:
                            await reference.add_reaction('🅾️')
                            o += 1
                        elif o == 2:
                            await reference.add_reaction('⭕')
                            o += 1
                    elif character == 'p':
                        if p == 0:
                            await reference.add_reaction('🇵')
                            p += 1
                        elif p == 1:
                            await reference.add_reaction('🅿️')
                            p += 1
                    elif character == 'q':
                        await reference.add_reaction('🇶')
                    elif character == 'r':
                        if r == 0:
                            await reference.add_reaction('🇷')
                            r += 1
                        elif r == 1:
                            await reference.add_reaction('®️')
                            r += 1
                    elif character == 's':
                        await reference.add_reaction('🇸')
                    elif character == 't':
                        if t == 0:
                            await reference.add_reaction('🇹')
                            t += 1
                        elif t == 1:
                            await reference.add_reaction('✝️')
                            t += 1
                    elif character == 'u':
                        await reference.add_reaction('🇺')
                    elif character == 'v':
                        await reference.add_reaction('🇻')
                    elif character == 'w':
                        await reference.add_reaction('🇼')
                    elif character == 'x':
                        if x == 0:
                            await reference.add_reaction('🇽')
                            x += 1
                        elif x == 1:
                            await reference.add_reaction('✖️')
                            x += 1
                        elif x == 2:
                            await reference.add_reaction('❎')
                            x += 1
                        elif x == 3:
                            await reference.add_reaction('❌')
                            x += 1
                    elif character == 'y':
                        await reference.add_reaction('🇾')
                    elif character == 'z':
                        await reference.add_reaction('🇿')
            except AttributeError:
                return
    textlist = await text.read()
    # If the bot sees a reddit link in a message, it will try to send the image from this post
    if 'reddit.com' in message.content and not message.author.bot:
        link = message.content
        await message.delete()
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
        if 'creeper' in messagestring:
            await checkwordreaction('creeper', 'None', messagestring, message, 'None', 'OW MAN')
        elif 'ah fuck' in messagestring:
            await checkwordreaction('ah fuck', 'None', messagestring, message, 'None',
                                    "I can't believe you've done this")
        elif "who didnt flush the toilet" in messagestring:
            await checkwordreaction('who didnt flush the toilet', 'None', messagestring, message, config_file.disgustang_path,
                                    'DISGUUUSTAAAN!!!!!')
        elif 'disgusting' in messagestring:
            await checkwordreaction('disgusting', 'None', messagestring, message,
                                    config_file.disgustang_path,
                                    'DISGUUUSTAAAN!!!!!')
        elif 'disgustang' in messagestring:
            await checkwordreaction('disgustang', 'None', messagestring, message,
                                    config_file.disgustang_path,
                                    'DISGUUUSTAAAN!!!!!')
        elif "didnt expect" in messagestring:
            await checkwordreaction('didnt expect', 'None', messagestring, message,
                                    config_file.spanish_inquisition_path,
                                    'Boom Spanish Inquisition.')
        elif 'catoe' in messagestring:
            await checkwordreaction('catoe', 'None', messagestring, message, 'None', 'Catoe moet pottoe!')
        elif 'cato' in messagestring:
            await checkwordreaction('cato', 'None', messagestring, message, 'None', 'Catoe moet pottoe!')
        elif "did not expect" in messagestring:
            await checkwordreaction('did not expect', 'None', messagestring, message,
                                    config_file.spanish_inquisition_path,
                                    'Boom Spanish Inquisition.')
        elif 'unexpected' in messagestring:
            await checkwordreaction('unexpected', 'None', messagestring, message,
                                    config_file.spanish_inquisition_path,
                                    'Boom Spanish Inquisition.')
        elif 'speed' in messagestring:
            await checkwordreaction('speed', 'None', messagestring, message,
                                    config_file.lightning_path, 'I am speed')
        elif 'fml' in messagestring:
            await checkwordreaction('fml', 'None', messagestring, message,
                                    config_file.fml_path, 'None')
        elif 'high' in messagestring:
            await checkwordreaction('high', 'None', messagestring, message,
                                    config_file.high_path, 'None')
        elif 'drunk' in messagestring:
            await checkwordreaction('drunk', 'None', messagestring, message,
                                    config_file.high_path, 'None')
        elif 'barrelroll' in messagestring:
            await checkwordreaction('barrelroll', 'None', messagestring, message,
                                    config_file.barrelroll_path, 'None')
        elif 'barrel roll' in messagestring:
            await checkwordreaction('barrel roll', 'None', messagestring, message,
                                    config_file.barrelroll_path, 'None')
        elif '<3' in messagestring:
            await checkwordreaction('<3', '❤', messagestring, message, 'None', 'None')
            await checkwordreaction('<3', '🍉', messagestring, message, 'None', 'None')
        elif '❤' in messagestring:
            await checkwordreaction('❤', '❤', messagestring, message, 'None', 'None')
            await checkwordreaction('❤', '🍉', messagestring, message, 'None', 'None')
        elif messagestring == 'koekoek':
            await message.channel.send(datetime.datetime.now())
        elif 'fire' in messagestring:
            await checkwordreaction('fire', '🔥', messagestring, message, 'None', 'None')
        elif 'lit' in messagestring:
            await checkwordreaction('lit', '🔥', messagestring, message, 'None', 'None')
        elif 'geil' in messagestring:
            await checkwordreaction('geil', '🥵', messagestring, message, 'None', 'None')
        elif 'lekker' in messagestring:
            await checkwordreaction('lekker', '🥵', messagestring, message, 'None', 'None')
        elif 'cute' in messagestring:
            await checkwordreaction('cute', 'None', messagestring, message,
                                    config_file.but_path, 'None')
        elif "im " in messagestring:
            messagestring = messagestring.split('im')
            spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
            spacepos2 = messagestring[1].find(' ')
            if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and spacepos2 == 0:
                await message.channel.send('Hello' + messagestring[1] + ", I'm dad")
        elif 'hello there' in messagestring:
            await checkwordreaction('hello there', 'None', messagestring, message,
                                    config_file.general_kenobi_path,
                                    'General Kenobi')
        elif 'idk' in messagestring:
            await checkwordreaction('idk', 'None', messagestring, message, 'None', '¯\_(ツ)_/¯')
        elif 'i dont know' in messagestring:
            await checkwordreaction('i dont know', 'None', messagestring, message, 'None', '¯\_(ツ)_/¯')
        elif 'vive la resistance' in messagestring:
            await checkwordreaction('vive la resistance', 'None', messagestring, message,
                                    config_file.vive_la_resistance_path,
                                    'None')
        elif 'rtx' in messagestring:
            await checkwordreaction('rtx', 'None', messagestring, message,
                                    config_file.rtx_path, 'None')
        elif 'doe het niet' in messagestring:
            await checkwordreaction('doe het niet', 'None', messagestring, message, 'None', 'Hij deed het toch')
        elif 'elektrocutie' in messagestring:
            await checkwordreaction('elektrocutie', 'None', messagestring, message,
                                    config_file.pikachu_path, 'None')
        elif 'hekkie' in messagestring:
            await checkwordreaction('hekkie', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
            messagestring = messagestring.split('hekkie')
            # Finds the locations of the spaces
            spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
            spacepos2 = messagestring[1].find(' ')
            if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (messagestring[1] == '' or spacepos2 == 0):  # Checks if the words that we want are not between other letters
                voice_state = message.author.voice
                if message.guild.voice_client is None:  # Checks if the bot is not already in a channel
                    if voice_state:  # Checks if the user is in a channel
                        vc = await message.author.voice.channel.connect()
                        vc.play(discord.FFmpegPCMAudio(
                            source=config_file.hekkie_mp3_path))
                        with audioread.audio_open(
                                config_file.hekkie_mp3_path) as f:
                            await asyncio.sleep(f.duration)
                        await vc.disconnect()
        elif 'brain' in messagestring:
            await checkwordreaction('brain', 'None', messagestring, message, config_file.brain_aneurysm_mp4_path, 'None')
            messagestring = messagestring.split('brain')
            # Finds the locations of the spaces
            spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
            spacepos2 = messagestring[1].find(' ')
            if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (
                    messagestring[
                        1] == '' or spacepos2 == 0):  # Checks if the words that we want are not between other letters
                voice_state = message.author.voice
                if message.guild.voice_client is None:  # Checks if the bot is not already in a channel
                    if voice_state:  # Checks if the user is in a channel
                        vc = await message.author.voice.channel.connect()
                        vc.play(discord.FFmpegPCMAudio(
                            source=config_file.brain_aneurysm_mp3_path))
                        with audioread.audio_open(
                                config_file.brain_aneurysm_mp3_path) as f:
                            await asyncio.sleep(f.duration)
                        await vc.disconnect()
        elif 'john cena' in messagestring:
            messagestring = messagestring.split('john cena')
            # Finds the locations of the spaces
            spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
            spacepos2 = messagestring[1].find(' ')
            if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (
                    messagestring[
                        1] == '' or spacepos2 == 0):  # Checks if the words that we want are not between other letters
                voice_state = message.author.voice
                if message.guild.voice_client is None:  # Checks if the bot is not already in a channel
                    if voice_state:  # Checks if the user is in a channel
                        vc = await message.author.voice.channel.connect()
                        vc.play(discord.FFmpegPCMAudio(
                            source=config_file.john_cena_path))
                        with audioread.audio_open(
                                config_file.john_cena_path) as f:
                            await asyncio.sleep(f.duration)
                        await vc.disconnect()
    else:
        return
