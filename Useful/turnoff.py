import config_file
from SQL import turnonoff


async def turnoff(ctx, option, type):
    serverid = ctx.guild.id
    if option == 'all':
        for i in range(len(config_file.functions)-1):
            await turnonoff.update(0, serverid, config_file.functions[i+1])
        if type == 'normal':
            await ctx.reply("All functions have been turned off.")
        elif type == 'slash':
            await ctx.respond("All functions have been turned off.")
    elif option == 'sounds':
        variable = await turnonoff.read(serverid, "sounds")
        if variable == 1:
            await turnonoff.update(0, serverid, 'sounds')
            if type == 'normal':
                await ctx.reply("Random sounds have been turned off.")
            elif type == 'slash':
                await ctx.respond("Random sounds have been turned off.")
        else:
            if type == 'normal':
                await ctx.reply("Random sounds were already turned off.")
            elif type == 'slash':
                await ctx.respond("Random sounds were already turned off.")
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