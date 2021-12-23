import asyncio
import audioread
import discord
import config_file


# Function to play tutturu
async def playtutturu(voice_channel):
    path = config_file.tutturu_path
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(source=path))
    with audioread.audio_open(path) as f:
        await asyncio.sleep(f.duration)
    await vc.disconnect()


async def tutturu(ctx):
    voice_state = ctx.author.voice
    if ctx.voice_client is None:
        if voice_state:
            voice_channel = ctx.author.voice.channel
            await playtutturu(voice_channel)
        elif voice_state is None:
            await ctx.send(str(ctx.author.name) + " is not in a channel.")
    elif voice_state is None:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")
    elif ctx.author.voice.channel == ctx.voice_client.channel:
        await ctx.send('Bot is already playing something else.')
    else:
        await ctx.send('Bot is already in another channel.')
