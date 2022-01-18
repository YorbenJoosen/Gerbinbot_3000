import config_file
from SQL import turnonoff


async def turnoff(ctx, option):
    serverid = ctx.guild.id
    if option == 'all':
        for what in config_file.functions:
            await turnonoff.update(0, serverid, what)
        await ctx.reply("All functioffs have been turned off.")
    elif option == 'doeidruif':
        variable = await turnonoff.read(serverid, "doeidruif")
        if variable == 1:
            await turnonoff.update(0, serverid, 'doeidruif')
            await ctx.reply("Doeidruif has been turned off.")
        else:
            await ctx.reply("Doeidruif was already turned off.")
    elif option == 'dad':
        variable = await turnonoff.read(serverid, "dad")
        if variable == 1:
            await turnonoff.update(0, serverid, 'dad')
            await ctx.reply("Dad has been turned off.")
        else:
            await ctx.reply("Dad was already turned off.")
    elif option == 'john cena':
        variable = await turnonoff.read(serverid, "johncena")
        if variable == 1:
            await turnonoff.update(0, serverid, 'johncena')
            await ctx.reply("John cena has been turned off.")
        else:
            await ctx.reply("John cena was already turned off.")
    elif option == 'brain':
        variable = await turnonoff.read(serverid, "brain")
        if variable == 1:
            await turnonoff.update(0, serverid, 'brain')
            await ctx.reply("Brain has been turned off.")
        else:
            await ctx.reply("Brain was already turned off.")
    elif option == 'hekkie':
        variable = await turnonoff.read(serverid, "hekkie")
        if variable == 1:
            await turnonoff.update(0, serverid, 'hekkie')
            await ctx.reply("Hekkie has been turned off.")
        else:
            await ctx.reply("Hekkie was already turned off.")
    elif option == 'buffalo':
        variable = await turnonoff.read(serverid, "buffalo")
        if variable == 1:
            await turnonoff.update(1, serverid, 'buffalo')
            await ctx.reply("Buffalo has been turned off.")
        else:
            await ctx.reply("Buffalo was already turned off.")
    elif option == 'afsluiten':
        variable = await turnonoff.read(serverid, "afsluiten")
        if variable == 1:
            await turnonoff.update(1, serverid, 'afsluiten')
            await ctx.reply("Afsluiten has been turned off.")
        else:
            await ctx.reply("Afsluiten was already turned off.")
    elif option == 'child':
        variable = await turnonoff.read(serverid, "child")
        if variable == 1:
            await turnonoff.update(1, serverid, 'child')
            await ctx.reply("Child has been turned off.")
        else:
            await ctx.reply("Child was already turned off.")
    elif option == 'cola':
        variable = await turnonoff.read(serverid, "cola")
        if variable == 1:
            await turnonoff.update(1, serverid, 'cola')
            await ctx.reply("Cola has been turned off.")
        else:
            await ctx.reply("Cola was already turned off.")
    elif option == 'torture':
        variable = await turnonoff.read(serverid, "torture")
        if variable == 1:
            await turnonoff.update(1, serverid, 'torture')
            await ctx.reply("Torture has been turned off.")
        else:
            await ctx.reply("Torture was already turned off.")
    elif option == 'gorp':
        variable = await turnonoff.read(serverid, "gorp")
        if variable == 1:
            await turnonoff.update(1, serverid, 'gorp')
            await ctx.reply("Gorp has been turned off.")
        else:
            await ctx.reply("Gorp was already turned off.")
    elif option == 'hehe':
        variable = await turnonoff.read(serverid, "hehe")
        if variable == 1:
            await turnonoff.update(1, serverid, 'hehe')
            await ctx.reply("Hehe has been turned off.")
        else:
            await ctx.reply("Hehe was already turned off.")
    elif option == 'helicopter':
        variable = await turnonoff.read(serverid, "helicopter")
        if variable == 1:
            await turnonoff.update(1, serverid, 'helicopter')
            await ctx.reply("Helicopter has been turned off.")
        else:
            await ctx.reply("Helicopter was already turned off.")
    elif option == 'hello there':
        variable = await turnonoff.read(serverid, "hellothere")
        if variable == 1:
            await turnonoff.update(1, serverid, 'hellothere')
            await ctx.reply("Hello there has been turned off.")
        else:
            await ctx.reply("Hello there was already turned off.")
    elif option == 'boss':
        variable = await turnonoff.read(serverid, "boss")
        if variable == 1:
            await turnonoff.update(1, serverid, 'boss')
            await ctx.reply("Boss there has been turned off.")
        else:
            await ctx.reply("Boss there was already turned off.")
    elif option == 'indie home':
        variable = await turnonoff.read(serverid, "home")
        if variable == 1:
            await turnonoff.update(1, serverid, 'home')
            await ctx.reply("Indie home there has been turned off.")
        else:
            await ctx.reply("Indie home there was already turned off.")
    elif option == 'lachje':
        variable = await turnonoff.read(serverid, "lachje")
        if variable == 1:
            await turnonoff.update(1, serverid, 'lachje')
            await ctx.reply("Lachje has been turned off.")
        else:
            await ctx.reply("Lachje there was already turned off.")
    elif option == 'lemoffs':
        variable = await turnonoff.read(serverid, "lemoffs")
        if variable == 1:
            await turnonoff.update(1, serverid, 'lemoffs')
            await ctx.reply("Lemoffs has been turned off.")
        else:
            await ctx.reply("Lemoffs there was already turned off.")
    elif option == 'mcdoffalds':
        variable = await turnonoff.read(serverid, "mcdoffalds")
        if variable == 1:
            await turnonoff.update(1, serverid, 'mcdoffalds')
            await ctx.reply("McDoffalds has been turned off.")
        else:
            await ctx.reply("McDoffalds there was already turned off.")
    elif option == 'misinput':
        variable = await turnonoff.read(serverid, "misinput")
        if variable == 1:
            await turnonoff.update(1, serverid, 'misinput')
            await ctx.reply("Misinput has been turned off.")
        else:
            await ctx.reply("Misinput there was already turned off.")
    elif option == 'omgekeerd':
        variable = await turnonoff.read(serverid, "offgekeerd")
        if variable == 1:
            await turnonoff.update(1, serverid, 'omgekeerd')
            await ctx.reply("Omgekeerd has been turned off.")
        else:
            await ctx.reply("Omgekeerd there was already turned off.")
    elif option == 'raid':
        variable = await turnonoff.read(serverid, "raid")
        if variable == 1:
            await turnonoff.update(1, serverid, 'raid')
            await ctx.reply("Raid has been turned off.")
        else:
            await ctx.reply("Raid there was already turned off.")
    elif option == 'sausage':
        variable = await turnonoff.read(serverid, "sausage")
        if variable == 1:
            await turnonoff.update(1, serverid, 'sausage')
            await ctx.reply("Sausage has been turned off.")
        else:
            await ctx.reply("Sausage there was already turned off.")
    elif option == 'raining':
        variable = await turnonoff.read(serverid, "raining")
        if variable == 1:
            await turnonoff.update(1, serverid, 'raining')
            await ctx.reply("Raining has been turned off.")
        else:
            await ctx.reply("Raining there was already turned off.")
    elif option == 'uvu':
        variable = await turnonoff.read(serverid, "uvu")
        if variable == 1:
            await turnonoff.update(1, serverid, 'uvu')
            await ctx.reply("Uvu has been turned off.")
        else:
            await ctx.reply("Uvu there was already turned off.")
    elif option == 'vietnamese':
        variable = await turnonoff.read(serverid, "vietnamese")
        if variable == 1:
            await turnonoff.update(1, serverid, 'vietnamese')
            await ctx.reply("Vietnamese has been turned off.")
        else:
            await ctx.reply("Vietnamese there was already turned off.")
    elif option == 'voicemail':
        variable = await turnonoff.read(serverid, "voicemail")
        if variable == 1:
            await turnonoff.update(1, serverid, 'voicemail')
            await ctx.reply("Voicemail has been turned off.")
        else:
            await ctx.reply("Voicemail there was already turned off.")