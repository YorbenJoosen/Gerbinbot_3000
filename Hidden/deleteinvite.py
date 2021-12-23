async def deleteinvite(ctx):
    await ctx.message.delete()
    invites = await ctx.guild.invites()
    i = 0
    while i < len(invites):
        if invites[i].inviter.name == "Gerbinbot 3000":
            await invites[i].delete()
            i = len(invites)
        else:
            i += 1
