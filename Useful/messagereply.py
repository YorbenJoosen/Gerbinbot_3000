import asyncio
import datetime
import random
import audioread
import discord
import config_file


# Function to check how the bot should respond
async def checkwordreaction(splitter, reactionemoji, messagestring, message, filename, reactionmessage):
    messagestring = messagestring.split(splitter)
    spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
    spacepos2 = messagestring[1].find(' ')
    if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (
            messagestring[1] == '' or spacepos2 == 0):
        if reactionemoji != 'None':
            await message.add_reaction(reactionemoji)
        if reactionmessage != 'None' and filename != 'None':
            await message.reply(reactionmessage, file=discord.File(filename))
        elif reactionmessage != 'None':
            await message.reply(reactionmessage)
        elif filename != 'None':
            await message.reply(file=discord.File(filename))


async def messagereply(message, messagestring):
    if 'creeper' in messagestring:
        await checkwordreaction('creeper', 'None', messagestring, message, 'None', 'OW MAN')
    elif 'ah fuck' in messagestring:
        await checkwordreaction('ah fuck', 'None', messagestring, message, 'None',
                                "I can't believe you've done this")
    elif "who didnt flush the toilet" in messagestring:
        await checkwordreaction('who didnt flush the toilet', 'None', messagestring, message,
                                config_file.disgustang_path,
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
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
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
    elif 'pauze' in messagestring:
        if random.randint(0, 10) <= 1:
            await checkwordreaction('pauze', 'None', messagestring, message, 'None',
                                    'Is het een pauze als hij niet uitloopt?')
    elif 'hekkie' in messagestring:
        await checkwordreaction('hekkie', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
        messagestring = messagestring.split('hekkie')
        # Finds the locations of the spaces
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
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
    elif '#' in messagestring:
        await checkwordreaction('#', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
        messagestring = messagestring.split('#')
        # Finds the locations of the spaces
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
        spacepos2 = messagestring[1].find(' ')
        if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (messagestring[
                                                                                       1] == '' or spacepos2 == 0):  # Checks if the words that we want are not between other letters
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
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
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
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
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
    elif 'buffalo' in messagestring:
        messagestring = messagestring.split('buffalo')
        # Finds the locations of the spaces
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
        spacepos2 = messagestring[1].find(' ')
        if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (
                messagestring[
                    1] == '' or spacepos2 == 0):  # Checks if the words that we want are not between other letters
            voice_state = message.author.voice
            if message.guild.voice_client is None:  # Checks if the bot is not already in a channel
                if voice_state:  # Checks if the user is in a channel
                    vc = await message.author.voice.channel.connect()
                    vc.play(discord.FFmpegPCMAudio(
                        source=config_file.buffalo_path))
                    with audioread.audio_open(
                            config_file.buffalo_path) as f:
                        await asyncio.sleep(f.duration)
                    await vc.disconnect()
    else:
        return