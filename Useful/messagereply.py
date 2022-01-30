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


async def checksoundreaction(splitter, messagestring, message, path):
    messagestring = messagestring.split(splitter)
    spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
    spacepos2 = messagestring[1].find(' ')
    if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and (messagestring[1] == '' or spacepos2 == 0):
        voice_state = message.author.voice
        if message.guild.voice_client is None:  # Checks if the bot is not already in a channel
            if voice_state:  # Checks if the user is in a channel
                vc = await message.author.voice.channel.connect()
                vc.play(discord.FFmpegPCMAudio(source=path))
                with audioread.audio_open(path) as f:
                    await asyncio.sleep(f.duration)
                await vc.disconnect()


async def messagereply(message, messagestring):
    dad = await turnonoff.read(message.guild.id, "dad")
    sounds = await turnonoff.read(message.guild.id, "sounds")
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
        await checkwordreaction('cute', 'None', messagestring, message, config_file.but_path, 'None')
    elif "im " in messagestring and dad == 1:
        messagestring = messagestring.split('im')
        spacepos1 = messagestring[0].find(' ', len(messagestring[0]) - 1)
        spacepos2 = messagestring[1].find(' ')
        if (messagestring[0] == '' or spacepos1 == len(messagestring[0]) - 1) and spacepos2 == 0:
            await message.channel.send('Hello' + messagestring[1] + ", I'm dad")
    elif 'hello there' in messagestring:
        if sounds == 1:
            await checksoundreaction('hello there', messagestring, message, config_file.hello_there_path)
        await checkwordreaction('hello there', 'None', messagestring, message, config_file.general_kenobi_path, 'General Kenobi')
    elif 'idk' in messagestring:
        await checkwordreaction('idk', 'None', messagestring, message, 'None', '¯\_(ツ)_/¯')
    elif 'i dont know' in messagestring:
        await checkwordreaction('i dont know', 'None', messagestring, message, 'None', '¯\_(ツ)_/¯')
    elif 'vive la resistance' in messagestring:
        await checkwordreaction('vive la resistance', 'None', messagestring, message, config_file.vive_la_resistance_path, 'None')
    elif 'rtx' in messagestring:
        await checkwordreaction('rtx', 'None', messagestring, message, config_file.rtx_path, 'None')
    elif 'doe het niet' in messagestring:
        await checkwordreaction('doe het niet', 'None', messagestring, message, 'None', 'Hij deed het toch')
    elif 'elektrocutie' in messagestring:
        await checkwordreaction('elektrocutie', 'None', messagestring, message, config_file.pikachu_path, 'None')
    elif 'pauze' in messagestring:
        if random.randint(0, 10) <= 1:
            await checkwordreaction('pauze', 'None', messagestring, message, 'None', 'Is het een pauze als hij niet uitloopt?')
    elif 'hekkie' in messagestring:
        if sounds == 1:
            await checksoundreaction('hekkie', messagestring, message, config_file.hekkie_mp3_path)
        await checkwordreaction('hekkie', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
    elif '#' in messagestring:
        if sounds == 1:
            await checksoundreaction('#', messagestring, message, config_file.hekkie_mp3_path)
        await checkwordreaction('#', 'None', messagestring, message, config_file.hekkie_gif_path, 'None')
    elif 'brain' in messagestring:
        if sounds == 1:
            await checksoundreaction('brain', messagestring, message, config_file.brain_aneurysm_mp3_path)
        await checkwordreaction('brain', 'None', messagestring, message, config_file.brain_aneurysm_mp4_path, 'None')
    elif 'john cena' in messagestring:
        if sounds == 1:
            await checksoundreaction('john cena', messagestring, message, config_file.john_cena_path)
    elif 'buffalo' in messagestring:
        if sounds == 1:
            await checksoundreaction('buffalo', messagestring, message, config_file.buffalo_path)
    elif 'afsluiten' in messagestring:
        if sounds == 1:
            await checksoundreaction('afsluiten', messagestring, message, config_file.afsluiten_path)
    elif 'child' in messagestring:
        if sounds == 1:
            await checksoundreaction('child', messagestring, message, config_file.child_mp3_path)
        await checkwordreaction('child', 'None', messagestring, message, config_file.child_mp4_path, 'None')
    elif 'cola' in messagestring:
        if sounds == 1:
            await checksoundreaction('cola', messagestring, message, config_file.cola_path)
    elif 'torture' in messagestring:
        if sounds == 1:
            await checksoundreaction('torture', messagestring, message, config_file.torture_path)
    elif 'gorp' in messagestring:
        if sounds == 1:
            await checksoundreaction('gorp', messagestring, message, config_file.gorp_path)
    elif 'hehe' in messagestring:
        if sounds == 1:
            await checksoundreaction('hehe', messagestring, message, config_file.hehe_path)
    elif 'helicopter' in messagestring:
        if sounds == 1:
            await checksoundreaction('helicopter', messagestring, message, config_file.helicopter_path)
    elif 'boss' in messagestring:
        if sounds == 1:
            await checksoundreaction('boss', messagestring, message, config_file.hey_boss_path)
    elif 'home' in messagestring:
        if sounds == 1:
            await checksoundreaction('home', messagestring, message, config_file.indiehome_mp3_path)
        await checkwordreaction('home', 'None', messagestring, message, config_file.indiehome_mp4_path, 'None')
    elif 'lach' in messagestring:
        if sounds == 1:
            await checksoundreaction('lach', messagestring, message, config_file.lachje_path)
    elif 'lemons' in messagestring:
        if sounds == 1:
            await checksoundreaction('lemons', messagestring, message, config_file.lemons_path)
    elif 'mcdonalds' in messagestring:
        if sounds == 1:
            await checksoundreaction('mcdonalds', messagestring, message, config_file.mcdonalds_path)
    elif 'misinput' in messagestring:
        if sounds == 1:
            await checksoundreaction('misinput', messagestring, message, config_file.misinput_path)
    elif 'omgekeerd' in messagestring:
        if sounds == 1:
            await checksoundreaction('omgekeerd', messagestring, message, config_file.omgekeerd_path)
    elif 'raid' in messagestring:
        if sounds == 1:
            await checksoundreaction('raid', messagestring, message, config_file.raid_path)
    elif 'sausage' in messagestring:
        if sounds == 1:
            await checksoundreaction('sausage', messagestring, message, config_file.sausage_path)
    elif 'raining' in messagestring:
        if sounds == 1:
            await checksoundreaction('raining', messagestring, message, config_file.raining_path)
    elif 'uvu' in messagestring:
        if sounds == 1:
            await checksoundreaction('uvu', messagestring, message, config_file.uvu_path)
    elif 'vietnamese' in messagestring:
        if sounds == 1:
            await checksoundreaction('vietnamese', messagestring, message, config_file.vietnamese_path)
    elif 'voicemail' in messagestring:
        if sounds == 1:
            await checksoundreaction('voicemail', messagestring, message, config_file.voicemail_path)
    elif 'burgir' in messagestring:
        if sounds == 1:
            await checksoundreaction('burgir', messagestring, message, config_file.burgir_mp3_path)
        if message.guild.id == config_file.yorbenguildid:
            await checkwordreaction('burgir', 'None', messagestring, message, config_file.burgir_mp4_path, 'None')
    elif 'r2d2' in messagestring:
        if sounds == 1:
            await checksoundreaction('r2d2', messagestring, message, config_file.r2d2_path)
    elif 'bruh' in messagestring:
        if sounds == 1:
            await checksoundreaction('bruh', messagestring, message, config_file.bruh_path)
    elif 'focus' in messagestring:
        if sounds == 1:
            await checksoundreaction('focus', messagestring, message, config_file.focus_path)
    elif 'pizza' in messagestring:
        if sounds == 1:
            await checksoundreaction('pizza', messagestring, message, config_file.focus_path)
    elif 'bark' in messagestring:
        if sounds == 1:
            await checksoundreaction('bark', messagestring, message, config_file.bark_mp3_path)
        await checkwordreaction('bark', 'None', messagestring, message, config_file.bark_mp4_path, 'None')
    else:
        return