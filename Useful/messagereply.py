import asyncio
import datetime
import random
import audioread
import discord
import config_file
from SQL import turnonoff


# Function to check how the bot should respond
async def checkwordreaction(splitter, reactionemoji, messagestring, message, filename, reactionmessage):
    messagestring = messagestring.split(splitter)
    spacepos1 = messagestring[0].find(' ', len(messagestring[0])-1)
    spacepos2 = messagestring[1].find(' ')
    if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (messagestring[1] == '' or spacepos2 == 0):
        if reactionemoji != 'None':
            await message.add_reaction(reactionemoji)
        if reactionmessage != 'None' and filename != 'None':
            await message.reply(reactionmessage, file=discord.File(filename))
        elif reactionmessage != 'None':
            await message.reply(reactionmessage)
        elif filename != 'None':
            await message.reply(file=discord.File(filename))


async def checksoundreaction(splitter, messagestring, message, path, variable):
    messagestring = messagestring.split(splitter)
    spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
    spacepos2 = messagestring[1].find(' ')
    if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (messagestring[1] == '' or spacepos2 == 0):
        voice_state = message.author.voice
        if message.guild.voice_client is None and variable == 1:  # Checks if the bot is not already in a channel
            if voice_state:  # Checks if the user is in a channel
                vc = await message.author.voice.channel.connect()
                vc.play(discord.FFmpegPCMAudio(source=path))
                with audioread.audio_open(path) as f:
                    await asyncio.sleep(f.duration)
                await vc.disconnect()


async def messagereply(message, messagestring):
    dad = await turnonoff.read(message.guild.id, "dad")
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
    elif "im " in messagestring and dad == 1:
        messagestring = messagestring.split('im')
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
        spacepos2 = messagestring[1].find(' ')
        if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and spacepos2 == 0:
            await message.channel.send('Hello' + messagestring[1] + ", I'm dad")
    elif 'hello there' in messagestring:
        variable = await turnonoff.read(message.guild.id, "hellothere")
        await checkwordreaction('hello there', 'None', messagestring, message, config_file.general_kenobi_path, 'General Kenobi')
        await checksoundreaction('hello there', messagestring, message, config_file.hello_there_path, variable)
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
        variable = await turnonoff.read(message.guild.id, "hekkie")
        await checkwordreaction('hekkie', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
        await checksoundreaction('hekkie', messagestring, message, config_file.hekkie_mp3_path, variable)
    elif '#' in messagestring:
        variable = await turnonoff.read(message.guild.id, "hekkie")
        await checkwordreaction('#', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
        await checksoundreaction('#', messagestring, message, config_file.hekkie_mp3_path, variable)
    elif 'brain' in messagestring:
        variable = await turnonoff.read(message.guild.id, "brain")
        await checkwordreaction('brain', 'None', messagestring, message, config_file.brain_aneurysm_mp4_path, 'None')
        await checksoundreaction('brain', messagestring, message, config_file.brain_aneurysm_mp3_path, variable)
    elif 'john cena' in messagestring:
        variable = await turnonoff.read(message.guild.id, "johncena")
        await checksoundreaction('john cena', messagestring, message, config_file.john_cena_path, variable)
    elif 'buffalo' in messagestring:
        variable = await turnonoff.read(message.guild.id, "buffalo")
        await checksoundreaction('buffalo', messagestring, message, config_file.buffalo_path, variable)
    elif 'afsluiten' in messagestring:
        variable = await turnonoff.read(message.guild.id, "afsluiten")
        await checksoundreaction('afsluiten', messagestring, message, config_file.afsluiten_path, variable)
    elif 'child' in messagestring:
        variable = await turnonoff.read(message.guild.id, "child")
        await checkwordreaction('child', 'None', messagestring, message, config_file.child_mp4_path, 'None')
        await checksoundreaction('child', messagestring, message, config_file.child_mp3_path, variable)
    elif 'cola' in messagestring:
        variable = await turnonoff.read(message.guild.id, "cola")
        await checksoundreaction('cola', messagestring, message, config_file.cola_path, variable)
    elif 'torture' in messagestring:
        variable = await turnonoff.read(message.guild.id, "torture")
        await checksoundreaction('torture', messagestring, message, config_file.torture_path, variable)
    elif 'gorp' in messagestring:
        variable = await turnonoff.read(message.guild.id, "gorp")
        await checksoundreaction('gorp', messagestring, message, config_file.gorp_path, variable)
    elif 'hehe' in messagestring:
        variable = await turnonoff.read(message.guild.id, "hehe")
        await checksoundreaction('hehe', messagestring, message, config_file.hehe_path, variable)
    elif 'helicopter' in messagestring:
        variable = await turnonoff.read(message.guild.id, "helicopter")
        await checksoundreaction('helicopter', messagestring, message, config_file.helicopter_path, variable)
    elif 'boss' in messagestring:
        variable = await turnonoff.read(message.guild.id, "boss")
        await checksoundreaction('boss', messagestring, message, config_file.hey_boss_path, variable)
    elif 'home' in messagestring:
        variable = await turnonoff.read(message.guild.id, "home")
        await checkwordreaction('home', 'None', messagestring, message, config_file.indiehome_mp4_path, 'None')
        await checksoundreaction('home', messagestring, message, config_file.indiehome_mp3_path, variable)
    elif 'lach' in messagestring:
        variable = await turnonoff.read(message.guild.id, "lachje")
        await checksoundreaction('lach', messagestring, message, config_file.lachje_path, variable)
    elif 'lemons' in messagestring:
        variable = await turnonoff.read(message.guild.id, "lemons")
        await checksoundreaction('lemons', messagestring, message, config_file.lemons_path, variable)
    elif 'mcdonalds' in messagestring:
        variable = await turnonoff.read(message.guild.id, "mcdonalds")
        await checksoundreaction('mcdonalds', messagestring, message, config_file.mcdonalds_path, variable)
    elif 'misinput' in messagestring:
        variable = await turnonoff.read(message.guild.id, "misinput")
        await checksoundreaction('misinput', messagestring, message, config_file.misinput_path, variable)
    elif 'omgekeerd' in messagestring:
        variable = await turnonoff.read(message.guild.id, "omgekeerd")
        await checksoundreaction('omgekeerd', messagestring, message, config_file.omgekeerd_path, variable)
    elif 'raid' in messagestring:
        variable = await turnonoff.read(message.guild.id, "raid")
        await checksoundreaction('raid', messagestring, message, config_file.raid_path, variable)
    elif 'sausage' in messagestring:
        variable = await turnonoff.read(message.guild.id, "sausage")
        await checksoundreaction('sausage', messagestring, message, config_file.sausage_path, variable)
    elif 'raining' in messagestring:
        variable = await turnonoff.read(message.guild.id, "raining")
        await checksoundreaction('raining', messagestring, message, config_file.raining_path, variable)
    elif 'uvu' in messagestring:
        variable = await turnonoff.read(message.guild.id, "uvu")
        await checksoundreaction('uvu', messagestring, message, config_file.uvu_path, variable)
    elif 'vietnamese' in messagestring:
        variable = await turnonoff.read(message.guild.id, "vietnamese")
        await checksoundreaction('vietnamese', messagestring, message, config_file.vietnamese_path, variable)
    elif 'voicemail' in messagestring:
        variable = await turnonoff.read(message.guild.id, "voicemail")
        await checksoundreaction('voicemail', messagestring, message, config_file.voicemail_path, variable)
    elif 'burgir' in messagestring:
        variable = await turnonoff.read(message.guild.id, "burgir")
        await checksoundreaction('burgir', messagestring, message, config_file.burgir_mp3_path, variable)
        if message.guild.id == config_file.yorbenguildid:
            await checkwordreaction('burgir', 'None', messagestring, message, config_file.burgir_mp4_path, 'None')
    else:
        return