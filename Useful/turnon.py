import config_file
from SQL import turnonoff


async def turnon(ctx, option):
    serverid = ctx.guild.id
    if option == 'all':
        for what in config_file.functions:
            await turnonoff.update(1, serverid, what)
        await ctx.reply("All functions have been turned on.")
    elif option == 'doeidruif':
        variable = await turnonoff.read(serverid, "doeidruif")
        if variable == 0:
            await turnonoff.update(1, serverid, 'doeidruif')
            await ctx.reply("Doeidruif has been turned on.")
        else:
            await ctx.reply("Doeidruif was already turned on.")
    elif option == 'dad':
        variable = await turnonoff.read(serverid, "dad")
        if variable == 0:
            await turnonoff.update(1, serverid, 'dad')
            await ctx.reply("Dad has been turned on.")
        else:
            await ctx.reply("Dad was already turned on.")
    elif option == 'john cena':
        variable = await turnonoff.read(serverid, "johncena")
        if variable == 0:
            await turnonoff.update(1, serverid, 'johncena')
            await ctx.reply("John cena has been turned on.")
        else:
            await ctx.reply("John cena was already turned on.")
    elif option == 'brain':
        variable = await turnonoff.read(serverid, "brain")
        if variable == 0:
            await turnonoff.update(1, serverid, 'brain')
            await ctx.reply("Brain has been turned on.")
        else:
            await ctx.reply("Brain was already turned on.")
    elif option == 'hekkie':
        variable = await turnonoff.read(serverid, "hekkie")
        if variable == 0:
            await turnonoff.update(1, serverid, 'hekkie')
            await ctx.reply("Hekkie has been turned on.")
        else:
            await ctx.reply("Hekkie was already turned on.")
    elif option == 'buffalo':
        variable = await turnonoff.read(serverid, "buffalo")
        if variable == 0:
            await turnonoff.update(1, serverid, 'buffalo')
            await ctx.reply("Buffalo has been turned on.")
        else:
            await ctx.reply("Buffalo was already turned on.")
    elif option == 'afsluiten':
        variable = await turnonoff.read(serverid, "afsluiten")
        if variable == 0:
            await turnonoff.update(1, serverid, 'afsluiten')
            await ctx.reply("Afsluiten has been turned on.")
        else:
            await ctx.reply("Afsluiten was already turned on.")
    elif option == 'child':
        variable = await turnonoff.read(serverid, "child")
        if variable == 0:
            await turnonoff.update(1, serverid, 'child')
            await ctx.reply("Child has been turned on.")
        else:
            await ctx.reply("Child was already turned on.")
    elif option == 'cola':
        variable = await turnonoff.read(serverid, "cola")
        if variable == 0:
            await turnonoff.update(1, serverid, 'cola')
            await ctx.reply("Cola has been turned on.")
        else:
            await ctx.reply("Cola was already turned on.")
    elif option == 'torture':
        variable = await turnonoff.read(serverid, "torture")
        if variable == 0:
            await turnonoff.update(1, serverid, 'torture')
            await ctx.reply("Torture has been turned on.")
        else:
            await ctx.reply("Torture was already turned on.")
    elif option == 'gorp':
        variable = await turnonoff.read(serverid, "gorp")
        if variable == 0:
            await turnonoff.update(1, serverid, 'gorp')
            await ctx.reply("Gorp has been turned on.")
        else:
            await ctx.reply("Gorp was already turned on.")
    elif option == 'hehe':
        variable = await turnonoff.read(serverid, "hehe")
        if variable == 0:
            await turnonoff.update(1, serverid, 'hehe')
            await ctx.reply("Hehe has been turned on.")
        else:
            await ctx.reply("Hehe was already turned on.")
    elif option == 'helicopter':
        variable = await turnonoff.read(serverid, "helicopter")
        if variable == 0:
            await turnonoff.update(1, serverid, 'helicopter')
            await ctx.reply("Helicopter has been turned on.")
        else:
            await ctx.reply("Helicopter was already turned on.")
    elif option == 'hello there':
        variable = await turnonoff.read(serverid, "hellothere")
        if variable == 0:
            await turnonoff.update(1, serverid, 'hellothere')
            await ctx.reply("Hello there has been turned on.")
        else:
            await ctx.reply("Hello there was already turned on.")
    elif option == 'boss':
        variable = await turnonoff.read(serverid, "boss")
        if variable == 0:
            await turnonoff.update(1, serverid, 'boss')
            await ctx.reply("Boss there has been turned on.")
        else:
            await ctx.reply("Boss there was already turned on.")
    elif option == 'indie home':
        variable = await turnonoff.read(serverid, "home")
        if variable == 0:
            await turnonoff.update(1, serverid, 'home')
            await ctx.reply("Indie home there has been turned on.")
        else:
            await ctx.reply("Indie home there was already turned on.")
    elif option == 'lachje':
        variable = await turnonoff.read(serverid, "lachje")
        if variable == 0:
            await turnonoff.update(1, serverid, 'lachje')
            await ctx.reply("Lachje has been turned on.")
        else:
            await ctx.reply("Lachje there was already turned on.")
    elif option == 'lemons':
        variable = await turnonoff.read(serverid, "lemons")
        if variable == 0:
            await turnonoff.update(1, serverid, 'lemons')
            await ctx.reply("Lemons has been turned on.")
        else:
            await ctx.reply("Lemons there was already turned on.")
    elif option == 'mcdonalds':
        variable = await turnonoff.read(serverid, "mcdonalds")
        if variable == 0:
            await turnonoff.update(1, serverid, 'mcdonalds')
            await ctx.reply("McDonalds has been turned on.")
        else:
            await ctx.reply("McDonalds there was already turned on.")
    elif option == 'misinput':
        variable = await turnonoff.read(serverid, "misinput")
        if variable == 0:
            await turnonoff.update(1, serverid, 'misinput')
            await ctx.reply("Misinput has been turned on.")
        else:
            await ctx.reply("Misinput there was already turned on.")
    elif option == 'omgekeerd':
        variable = await turnonoff.read(serverid, "ongekeerd")
        if variable == 0:
            await turnonoff.update(1, serverid, 'omgekeerd')
            await ctx.reply("Omgekeerd has been turned on.")
        else:
            await ctx.reply("Omgekeerd there was already turned on.")
    elif option == 'raid':
        variable = await turnonoff.read(serverid, "raid")
        if variable == 0:
            await turnonoff.update(1, serverid, 'raid')
            await ctx.reply("Raid has been turned on.")
        else:
            await ctx.reply("Raid there was already turned on.")
    elif option == 'sausage':
        variable = await turnonoff.read(serverid, "sausage")
        if variable == 0:
            await turnonoff.update(1, serverid, 'sausage')
            await ctx.reply("Sausage has been turned on.")
        else:
            await ctx.reply("Sausage there was already turned on.")
    elif option == 'raining':
        variable = await turnonoff.read(serverid, "raining")
        if variable == 0:
            await turnonoff.update(1, serverid, 'raining')
            await ctx.reply("Raining has been turned on.")
        else:
            await ctx.reply("Raining there was already turned on.")
    elif option == 'uvu':
        variable = await turnonoff.read(serverid, "uvu")
        if variable == 0:
            await turnonoff.update(1, serverid, 'uvu')
            await ctx.reply("Uvu has been turned on.")
        else:
            await ctx.reply("Uvu there was already turned on.")
    elif option == 'vietnamese':
        variable = await turnonoff.read(serverid, "vietnamese")
        if variable == 0:
            await turnonoff.update(1, serverid, 'vietnamese')
            await ctx.reply("Vietnamese has been turned on.")
        else:
            await ctx.reply("Vietnamese there was already turned on.")
    elif option == 'voicemail':
        variable = await turnonoff.read(serverid, "voicemail")
        if variable == 0:
            await turnonoff.update(1, serverid, 'voicemail')
            await ctx.reply("Voicemail has been turned on.")
        else:
            await ctx.reply("Voicemail there was already turned on.")