from SQL import turnonoff


async def turnon(ctx, option):
    serverid = ctx.guild.id
    johncena = await turnonoff.read(serverid, "johncena")
    brain = await turnonoff.read(serverid, "brain")
    hekkie = await turnonoff.read(serverid, "hekkie")
    buffalo = await turnonoff.read(serverid, "buffalo")
    dad = await turnonoff.read(serverid, "dad")
    doeidruif = await turnonoff.read(serverid, "doeidruif")
    if option == 'doeidruif':
        if doeidruif == 0:
            await turnonoff.update(1, serverid, 'doeidruif')
            await ctx.reply("Doeidruif has been turned on.")
        else:
            await ctx.reply("Doeidruif was already turned on.")
    elif option == 'dad':
        if dad == 0:
            await turnonoff.update(1, serverid, 'dad')
            await ctx.reply("Dad has been turned on.")
        else:
            await ctx.reply("Dad was already turned on.")
    elif option == 'john cena':
        if johncena == 0:
            await turnonoff.update(1, serverid, 'johncena')
            await ctx.reply("John cena has been turned on.")
        else:
            await ctx.reply("John cena was already turned on.")
    elif option == 'brain':
        if brain == 0:
            await turnonoff.update(1, serverid, 'brain')
            await ctx.reply("Brain has been turned on.")
        else:
            await ctx.reply("Brain was already turned on.")
    elif option == 'hekkie':
        if hekkie == 0:
            await turnonoff.update(1, serverid, 'hekkie')
            await ctx.reply("Hekkie has been turned on.")
        else:
            await ctx.reply("Hekkie was already turned on.")
    elif option == 'buffalo':
        if buffalo == 0:
            await turnonoff.update(1, serverid, 'buffalo')
            await ctx.reply("Buffalo has been turned on.")
        else:
            await ctx.reply("Buffalo was already turned on.")