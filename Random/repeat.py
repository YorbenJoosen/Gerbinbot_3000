async def repeat(ctx, message, type):
    if type == 'normal':
        await ctx.message.delete()
        await ctx.channel.send(message)
    elif type == 'slash':
        await ctx.respond('The message has been repeated.',ephemeral=True)
        await ctx.channel.send(message)
