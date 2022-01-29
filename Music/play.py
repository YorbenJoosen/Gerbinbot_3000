from SQL import loops
from Music import playlist, playsingleurl, playquery


async def whichkind(ctx, query, song, queue, type):
    if queue == 1:
        if type == 'normal':
            await ctx.reply("You can't add songs when the queue is looped.")
        elif type == 'slash':
            await ctx.respond("You can't add songs when the queue is looped.")
    elif song == 1:
        if type == 'normal':
            await ctx.reply("You can't add songs when a song is looped.")
        elif type == 'slash':
            await ctx.respond("You can't add songs when a song is looped.")
    else:
        if 'playlist?' in query:
            await playlist.playlist(ctx, query, type)
        elif 'watch?' in query:
            await playsingleurl.playsingleurl(ctx, query, type)
        elif 'youtu.be' in query:
            await playsingleurl.playsingleurl(ctx, query, type)
        else:
            await playquery.playquery(ctx, query, type)


async def play(ctx, query, type):
    serverid = ctx.guild.id
    song = await loops.read("song", serverid)
    queue = await loops.read("queue", serverid)
    voice_state = ctx.author.voice
    if ctx.voice_client:
        if voice_state and ctx.author.voice.channel == ctx.voice_client.channel:
            await whichkind(ctx, query, song, queue, type)
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
    elif voice_state:
        await whichkind(ctx, query, song, queue, type)
    else:
        if type == 'normal':
            await ctx.reply(str(ctx.author.name) + " is not in a channel.")
        elif type == 'slash':
            await ctx.respond(str(ctx.author.name) + " is not in a channel.")
