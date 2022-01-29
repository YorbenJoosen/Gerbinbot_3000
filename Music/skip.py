import discord
import audioread
import asyncio
import config_file
from SQL import loops, musicqueue, skipped, turnonoff
from Music import playvideo


async def skip(ctx, type):
    serverid = ctx.guild.id
    doeidruif = await turnonoff.read(serverid, 'doeidruif')
    musiclist = await musicqueue.read(serverid)
    song = await loops.read("song", serverid)
    queue = await loops.read("queue", serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            if len(musiclist) > 1 and song == 0:
                ctx.voice_client.stop()
                if queue == 1:
                    await musicqueue.write(musiclist[0]["url"], musiclist[0]["title"], musiclist[0]["duration"], serverid)
                    await musicqueue.delete(serverid)
                    musiclist = await musicqueue.read(serverid)
                    await musicqueue.sqlsort(musiclist, serverid)
                else:
                    await musicqueue.delete(serverid)
                await skipped.update(1, serverid)
                await playvideo.playvideo(ctx)
            if type == 'slash':
                await ctx.respond('Song has been skipped.', ephemeral=True)
            elif len(musiclist) == 1 and song == 0:
                ctx.voice_client.stop()
                await skipped.update(1, serverid)
                if doeidruif == 1:
                    ctx.voice_client.play(discord.FFmpegPCMAudio(source=config_file.doei_druif_path))
                    with audioread.audio_open(config_file.doei_druif_path) as f:
                        await asyncio.sleep(f.duration)
                await ctx.voice_client.disconnect()
                await musicqueue.delete(serverid)
            if type == 'slash':
                await ctx.respond('Song has been skipped.', ephemeral=True)
            elif len(musiclist) == 1 and song == 1:
                if type == 'normal':
                    await ctx.reply("The current song is in a loop, you can't skip this.")
                elif type == 'slash':
                    await ctx.respond("The current song is in a loop, you can't skip this.")
            else:
                if type == 'normal':
                    await ctx.reply('There is no song playing')
                elif type == 'slash':
                    await ctx.respond('There is no song playing')
        elif voice_state is None:
            if type == 'normal':
                await ctx.reply(str(ctx.author.name) + " is not in a channel.")
            elif type == 'slash':
                await ctx.respond(str(ctx.author.name) + " is not in a channel.")
        else:
            if type == 'normal':
                await ctx.reply(str(ctx.author.name) + " is not in the same channel.")
            elif type == 'slash':
                await ctx.respond(str(ctx.author.name) + " is not in the same channel.")
    else:
        if type == 'normal':
            await ctx.reply('Bot is not connected to a voice channel')
        elif type == 'slash':
            await ctx.respond('Bot is not connected to a voice channel')