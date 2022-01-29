import config_file
from SQL import turnonoff


async def turnoff(ctx, option, type):
    serverid = ctx.guild.id
    if option == 'all':
        for what in config_file.functions:
            await turnonoff.update(0, serverid, what)
        if type == 'normal':
            await ctx.reply("All functioffs have been turned off.")
        elif type == 'slash':
            await ctx.respond("All functioffs have been turned off.")
    elif option == 'doeidruif':
        variable = await turnonoff.read(serverid, "doeidruif")
        if variable == 1:
            await turnonoff.update(0, serverid, 'doeidruif')
            if type == 'normal':
                await ctx.reply("Doeidruif has been turned off.")
            elif type == 'slash':
                await ctx.respond("Doeidruif has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Doeidruif was already turned off.")
            elif type == 'slash':
                await ctx.respond("Doeidruif was already turned off.")
    elif option == 'dad':
        variable = await turnonoff.read(serverid, "dad")
        if variable == 1:
            await turnonoff.update(0, serverid, 'dad')
            if type == 'normal':
                await ctx.reply("Dad has been turned off.")
            elif type == 'slash':
                await ctx.respond("Dad has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Dad was already turned off.")
            elif type == 'slash':
                await ctx.respond("Dad was already turned off.")
    elif option == 'john cena':
        variable = await turnonoff.read(serverid, "johncena")
        if variable == 1:
            await turnonoff.update(0, serverid, 'johncena')
            if type == 'normal':
                await ctx.reply("John cena has been turned off.")
            elif type == 'slash':
                await ctx.respond("John cena has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("John cena was already turned off.")
            elif type == 'slash':
                await ctx.respond("John cena was already turned off.")
    elif option == 'brain':
        variable = await turnonoff.read(serverid, "brain")
        if variable == 1:
            await turnonoff.update(0, serverid, 'brain')
            if type == 'normal':
                await ctx.reply("Brain has been turned off.")
            elif type == 'slash':
                await ctx.respond("Brain has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Brain was already turned off.")
            elif type == 'slash':
                await ctx.respond("Brain was already turned off.")
    elif option == 'hekkie':
        variable = await turnonoff.read(serverid, "hekkie")
        if variable == 1:
            await turnonoff.update(0, serverid, 'hekkie')
            if type == 'normal':
                await ctx.reply("Hekkie has been turned off.")
            elif type == 'slash':
                await ctx.respond("Hekkie has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Hekkie was already turned off.")
            elif type == 'slash':
                await ctx.respond("Hekkie was already turned off.")
    elif option == 'buffalo':
        variable = await turnonoff.read(serverid, "buffalo")
        if variable == 1:
            await turnonoff.update(0, serverid, 'buffalo')
            if type == 'normal':
                await ctx.reply("Buffalo has been turned off.")
            elif type == 'slash':
                await ctx.respond("Buffalo has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Buffalo was already turned off.")
            elif type == 'slash':
                await ctx.respond("Buffalo was already turned off.")
    elif option == 'afsluiten':
        variable = await turnonoff.read(serverid, "afsluiten")
        if variable == 1:
            await turnonoff.update(0, serverid, 'afsluiten')
            if type == 'normal':
                await ctx.reply("Afsluiten has been turned off.")
            elif type == 'slash':
                await ctx.respond("Afsluiten has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Afsluiten was already turned off.")
            elif type == 'slash':
                await ctx.respond("Afsluiten was already turned off.")
    elif option == 'child':
        variable = await turnonoff.read(serverid, "child")
        if variable == 1:
            await turnonoff.update(0, serverid, 'child')
            if type == 'normal':
                await ctx.reply("Child has been turned off.")
            elif type == 'slash':
                await ctx.respond("Child has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Child was already turned off.")
            elif type == 'slash':
                await ctx.respond("Child was already turned off.")
    elif option == 'cola':
        variable = await turnonoff.read(serverid, "cola")
        if variable == 1:
            await turnonoff.update(0, serverid, 'cola')
            if type == 'normal':
                await ctx.reply("Cola has been turned off.")
            elif type == 'slash':
                await ctx.respond("Cola has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Cola was already turned off.")
            elif type == 'slash':
                await ctx.respond("Cola was already turned off.")
    elif option == 'torture':
        variable = await turnonoff.read(serverid, "torture")
        if variable == 1:
            await turnonoff.update(0, serverid, 'torture')
            if type == 'normal':
                await ctx.reply("Torture has been turned off.")
            if type == 'slash':
                await ctx.respond("Torture has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Torture was already turned off.")
            elif type == 'slash':
                await ctx.respond("Torture was already turned off.")
    elif option == 'gorp':
        variable = await turnonoff.read(serverid, "gorp")
        if variable == 1:
            await turnonoff.update(0, serverid, 'gorp')
            if type == 'normal':
                await ctx.reply("Gorp has been turned off.")
            elif type == 'slash':
                await ctx.respond("Gorp has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Gorp was already turned off.")
            elif type == 'slash':
                await ctx.respond("Gorp was already turned off.")
    elif option == 'hehe':
        variable = await turnonoff.read(serverid, "hehe")
        if variable == 1:
            await turnonoff.update(0, serverid, 'hehe')
            if type == 'normal':
                await ctx.reply("Hehe has been turned off.")
            elif type == 'slash':
                await ctx.respond("Hehe has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Hehe was already turned off.")
            elif type == 'slash':
                await ctx.respond("Hehe was already turned off.")
    elif option == 'helicopter':
        variable = await turnonoff.read(serverid, "helicopter")
        if variable == 1:
            await turnonoff.update(0, serverid, 'helicopter')
            if type == 'normal':
                await ctx.reply("Helicopter has been turned off.")
            elif type == 'slash':
                await ctx.respond("Helicopter has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Helicopter was already turned off.")
            elif type == 'slash':
                await ctx.respond("Helicopter was already turned off.")
    elif option == 'hello there':
        variable = await turnonoff.read(serverid, "hellothere")
        if variable == 1:
            await turnonoff.update(0, serverid, 'hellothere')
            if type == 'normal':
                await ctx.reply("Hello there has been turned off.")
            elif type == 'slash':
                await ctx.respond("Hello there has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Hello there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Hello there was already turned off.")
    elif option == 'boss':
        variable = await turnonoff.read(serverid, "boss")
        if variable == 1:
            await turnonoff.update(0, serverid, 'boss')
            if type == 'normal':
                await ctx.reply("Boss there has been turned off.")
            elif type == 'slash':
                await ctx.respond("Boss there has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Boss there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Boss there was already turned off.")
    elif option == 'indie home':
        variable = await turnonoff.read(serverid, "home")
        if variable == 1:
            await turnonoff.update(0, serverid, 'home')
            if type == 'normal':
                await ctx.reply("Indie home there has been turned off.")
            elif type == 'slash':
                await ctx.respond("Indie home there has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Indie home there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Indie home there was already turned off.")
    elif option == 'lachje':
        variable = await turnonoff.read(serverid, "lachje")
        if variable == 1:
            await turnonoff.update(0, serverid, 'lachje')
            if type == 'normal':
                await ctx.reply("Lachje has been turned off.")
            elif type == 'slash':
                await ctx.respond("Lachje has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Lachje there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Lachje there was already turned off.")
    elif option == 'lemons':
        variable = await turnonoff.read(serverid, "lemons")
        if variable == 1:
            await turnonoff.update(0, serverid, 'lemons')
            if type == 'normal':
                await ctx.reply("Lemons has been turned off.")
            elif type == 'slash':
                await ctx.respond("Lemons has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Lemons there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Lemons there was already turned off.")
    elif option == 'mcdonalds':
        variable = await turnonoff.read(serverid, "mcdonalds")
        if variable == 1:
            await turnonoff.update(0, serverid, 'mcdonalds')
            if type == 'normal':
                await ctx.reply("McDonalds has been turned off.")
            elif type == 'slash':
                await ctx.respond("McDonalds has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("McDonalds there was already turned off.")
            elif type == 'slash':
                await ctx.respond("McDonalds there was already turned off.")
    elif option == 'misinput':
        variable = await turnonoff.read(serverid, "misinput")
        if variable == 1:
            await turnonoff.update(0, serverid, 'misinput')
            if type == 'normal':
                await ctx.reply("Misinput has been turned off.")
            elif type == 'slash':
                await ctx.respond("Misinput has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Misinput there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Misinput there was already turned off.")
    elif option == 'omgekeerd':
        variable = await turnonoff.read(serverid, "offgekeerd")
        if variable == 1:
            await turnonoff.update(0, serverid, 'omgekeerd')
            if type == 'normal':
                await ctx.reply("Omgekeerd has been turned off.")
            elif type == 'slash':
                await ctx.respond("Omgekeerd has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Omgekeerd there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Omgekeerd there was already turned off.")
    elif option == 'raid':
        variable = await turnonoff.read(serverid, "raid")
        if variable == 1:
            await turnonoff.update(0, serverid, 'raid')
            if type == 'normal':
                await ctx.reply("Raid has been turned off.")
            elif type == 'slash':
                await ctx.respond("Raid has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Raid there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Raid there was already turned off.")
    elif option == 'sausage':
        variable = await turnonoff.read(serverid, "sausage")
        if variable == 1:
            await turnonoff.update(0, serverid, 'sausage')
            if type == 'normal':
                await ctx.reply("Sausage has been turned off.")
            elif type == 'slash':
                await ctx.respond("Sausage has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Sausage there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Sausage there was already turned off.")
    elif option == 'raining':
        variable = await turnonoff.read(serverid, "raining")
        if variable == 1:
            await turnonoff.update(0, serverid, 'raining')
            if type == 'normal':
                await ctx.reply("Raining has been turned off.")
            elif type == 'slash':
                await ctx.respond("Raining has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Raining there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Raining there was already turned off.")
    elif option == 'uvu':
        variable = await turnonoff.read(serverid, "uvu")
        if variable == 1:
            await turnonoff.update(0, serverid, 'uvu')
            if type == 'normal':
                await ctx.reply("Uvu has been turned off.")
            elif type == 'slash':
                await ctx.respond("Uvu has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Uvu there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Uvu there was already turned off.")
    elif option == 'vietnamese':
        variable = await turnonoff.read(serverid, "vietnamese")
        if variable == 1:
            await turnonoff.update(0, serverid, 'vietnamese')
            if type == 'normal':
                await ctx.reply("Vietnamese has been turned off.")
            elif type == 'slash':
                await ctx.respond("Vietnamese has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Vietnamese there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Vietnamese there was already turned off.")
    elif option == 'voicemail':
        variable = await turnonoff.read(serverid, "voicemail")
        if variable == 1:
            await turnonoff.update(0, serverid, 'voicemail')
            if type == 'normal':
                await ctx.reply("Voicemail has been turned off.")
            elif type == 'slash':
                await ctx.respond("Voicemail has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Voicemail there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Voicemail there was already turned off.")
    elif option == 'burgir':
        variable = await turnonoff.read(serverid, "burgir")
        if variable == 1:
            await turnonoff.update(0, serverid, 'burgir')
            if type == 'normal':
                await ctx.reply("Burgir has been turned off.")
            elif type == 'slash':
                await ctx.respond("Burgir has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Burgir there was already turned off.")
            elif type == 'slash':
                await ctx.respond("Burgir there was already turned off.")
    elif option == 'r2d2':
        variable = await turnonoff.read(serverid, "r2d2")
        if variable == 1:
            await turnonoff.update(0, serverid, 'r2d2')
            if type == 'normal':
                await ctx.reply("R2D2 has been turned off.")
            elif type == 'slash':
                await ctx.respond("R2D2 has been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("R2D2 there was already turned off.")
            elif type == 'slash':
                await ctx.respond("R2D2 there was already turned off.")