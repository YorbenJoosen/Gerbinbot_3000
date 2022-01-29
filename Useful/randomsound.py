import asyncio
import random
import audioread
import discord
import config_file


async def randomsound(ctx, type):
    if not ctx.guild.voice_client:
        voice_state = ctx.author.voice
        if voice_state:
            path = random.choice(config_file.paths)
            sound = path.replace(r"C:\Users\yorbe\PycharmProjects\Gerbinbot_3000\Files", '')
            sound = sound.replace("\\", '')
            sound = sound.split('.')[0]
            if type == 'normal':
                await ctx.reply('The sound was ' + sound)
            elif type == 'slash':
                await ctx.respond('The sound was ' + sound)
            vc = await ctx.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source=path))
            with audioread.audio_open(path) as f:
                await asyncio.sleep(f.duration)
            await vc.disconnect()
        else:
            if type == 'normal':
                await ctx.send(str(ctx.author.name) + " is not in a channel.")
            elif type == 'slash':
                await ctx.respond(str(ctx.author.name) + " is not in a channel.")
    else:
        if type == 'normal':
            await ctx.reply('Bot is already in a channel.')
        elif type == 'slash':
            await ctx.respond('Bot is already in a channel.')
