from SQL import turnonoff


async def turnoff(ctx, option):
    serverid = ctx.guild.id
    johncena = await turnonoff.read(serverid, "johncena")
    brain = await turnonoff.read(serverid, "brain")
    hekkie = await turnonoff.read(serverid, "hekkie")
    buffalo = await turnonoff.read(serverid, "buffalo")
    dad = await turnonoff.read(serverid, "dad")
    doeidruif = await turnonoff.read(serverid, "doeidruif")
    if option == 'doeidruif':
        if doeidruif == 1:
            await turnonoff.update(0, serverid, 'doeidruif')
            await ctx.reply("Doeidruif has been turned off.")
        else:
            await ctx.reply("Doeidruif was already turned off.")
    elif option == 'dad':
        if dad == 1:
            await turnonoff.update(0, serverid, 'dad')
            await ctx.reply("Dad has been turned off.")
        else:
            await ctx.reply("Dad was already turned off.")
    elif option == 'john cena':
        if johncena == 1:
            await turnonoff.update(0, serverid, 'johncena')
            await ctx.reply("John cena has been turned off.")
        else:
            await ctx.reply("John cena was already turned off.")
    elif option == 'brain':
        if brain == 1:
            await turnonoff.update(0, serverid, 'brain')
            await ctx.reply("Brain has been turned off.")
        else:
            await ctx.reply("Brain was already turned off.")
    elif option == 'hekkie':
        if hekkie == 1:
            await turnonoff.update(0, serverid, 'hekkie')
            await ctx.reply("Hekkie has been turned off.")
        else:
            await ctx.reply("Hekkie was already turned off.")
    elif option == 'buffalo':
        if buffalo == 1:
            await turnonoff.update(1, serverid, 'buffalo')
            await ctx.reply("Buffalo has been turned off.")
        else:
            await ctx.reply("Buffalo was already turned off.")