import asyncio
import random
import audioread
import discord
import config_file


async def randomsound(ctx):
    path = random.choice(config_file.paths)
    voice_state = ctx.author.voice
    if not ctx.guild.voice_client:
        if voice_state:
            vc = await ctx.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(source=path))
            with audioread.audio_open(path) as f:
                await asyncio.sleep(f.duration)
            await vc.disconnect()
        else:
            await ctx.send("You're not in a voice channel.")
