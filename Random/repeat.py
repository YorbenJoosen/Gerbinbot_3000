async def repeat(ctx, message):
    await ctx.message.delete()
    await ctx.channel.send(message)
