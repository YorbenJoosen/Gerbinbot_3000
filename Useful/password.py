import random


async def password(ctx, length, type):
    if type == 'normal':
        await ctx.message.delete()
    createdpassword = ''
    length = int(length)
    if length < 2000:
        while length != 0:
            letter = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                    "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
            number = random.randint(0, 9)
            character = random.choice(["-", ".", "!", "@", "$", "?", "&", "%", " "])
            numberorcharacterorletter = random.choice(["number", "character", "letter"])
            capitalorlower = random.choice(["capital", "lower"])
            if numberorcharacterorletter == "letter":
                if capitalorlower == "capital":
                    createdpassword += letter
                else:
                    createdpassword += letter.lower()
            elif numberorcharacterorletter == "number":
                createdpassword += str(number)
            else:
                createdpassword += character
            length -= 1
        member = ctx.author
        channel = await member.create_dm()
        await channel.send(createdpassword)
        if type == 'slash':
            await ctx.respond("Sent a DM!", ephemeral=True)
    else:
        member = ctx.author
        channel = await member.create_dm()
        await channel.send("Password length can't be greater than 2000.")
        if type == 'slash':
            await ctx.respond("Sent a DM!", ephemeral=True)
