async def invite(ctx):
    await ctx.message.delete()
    link = await ctx.channel.create_invite()
    channel = await ctx.author.create_dm()
    await channel.send(link)