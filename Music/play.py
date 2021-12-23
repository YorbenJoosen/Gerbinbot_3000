from SQL import loops
from Music import playlist, playsingleurl, playquery


async def whichkind(ctx, query, song, queue):
    if queue == 1:
        await ctx.send("You can't add songs when the queue is looped.")
    elif song == 1:
        await ctx.send("You can't add songs when a song is looped.")
    else:
        if 'playlist?' in query:
            await playlist.playlist(ctx, query)
        elif 'watch?' in query:
            await playsingleurl.playsingleurl(ctx, query)
        elif 'youtu.be' in query:
            await playsingleurl.playsingleurl(ctx, query)
        else:
            await playquery.playquery(ctx, query)


async def play(ctx, query):
    serverid = ctx.guild.id
    song = await loops.read("song", serverid)
    queue = await loops.read("queue", serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            await whichkind(ctx, query, song, queue)
        elif voice_state is None:
            await ctx.send(str(ctx.author.name) + " is not in a channel.")
        else:
            await ctx.send(str(ctx.author.name) + " is not in the same channel.")
    elif voice_state:
        await whichkind(ctx, query, song, queue)
    else:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")
