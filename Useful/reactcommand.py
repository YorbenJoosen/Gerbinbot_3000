async def reactcommand(message):
    channel = message.channel
    content = message.content.split(' ')
    if len(content) > 1:
        try:
            referenceid = message.reference.message_id
            reference = await channel.fetch_message(referenceid)
            await message.delete()
            content = content[1]
            content = content.lower()
            if len(content) > 20:
                length = 20
            else:
                length = len(content)
            a = 0
            b = 0
            c = 0
            i = 0
            m = 0
            n = 0
            o = 0
            p = 0
            r = 0
            t = 0
            u = 0
            v = 0
            x = 0
            for iterator in range(0, length):
                character = content[iterator]
                if character == 'a':
                    if a == 0:
                        await reference.add_reaction('🇦')
                        a += 1
                    elif a == 1:
                        await reference.add_reaction('🅰️')
                        a += 1
                    elif a == 2:
                        await reference.add_reaction('🅰')
                        a += 1
                elif character == 'b':
                    if b == 0:
                        await reference.add_reaction('🇧')
                        b += 1
                    elif b == 1:
                        await reference.add_reaction('🅱️')
                        b += 1
                    elif b == 2:
                        await reference.add_reaction('🅱')
                        b += 1
                elif character == 'c':
                    if c == 0:
                        await reference.add_reaction('🇨')
                        c += 1
                    elif c == 1:
                        await reference.add_reaction('©️')
                        c += 1
                    elif c == 2:
                        await reference.add_reaction('©')
                        c += 1
                elif character == 'd':
                    await reference.add_reaction('🇩')
                elif character == 'e':
                    await reference.add_reaction('🇪')
                elif character == 'f':
                    await reference.add_reaction('🇫')
                elif character == 'g':
                    await reference.add_reaction('🇬')
                elif character == 'h':
                    await reference.add_reaction('🇭')
                elif character == 'i':
                    if i == 0:
                        await reference.add_reaction('🇮')
                        i += 1
                    elif i == 1:
                        await reference.add_reaction('ℹ️')
                        i += 1
                    elif i == 2:
                        await reference.add_reaction('ℹ')
                        i += 1
                elif character == 'j':
                    await reference.add_reaction('🇯')
                elif character == 'k':
                    await reference.add_reaction('🇰')
                elif character == 'l':
                    await reference.add_reaction('🇱')
                elif character == 'm':
                    if m == 0:
                        await reference.add_reaction('🇲')
                        m += 1
                    elif m == 1:
                        await reference.add_reaction('Ⓜ️')
                        m += 1
                    elif m == 2:
                        await reference.add_reaction('Ⓜ')
                        m += 1
                    elif m == 3:
                        await reference.add_reaction('〽️')
                        m += 1
                    elif m == 4:
                        await reference.add_reaction('〽')
                        m += 1
                    elif m == 5:
                        await reference.add_reaction('♍')
                        m += 1
                    elif m == 6:
                        await reference.add_reaction('♏')
                        m += 1
                elif character == 'n':
                    if n == 0:
                        await reference.add_reaction('🇳')
                        n += 1
                    elif n == 1:
                        await reference.add_reaction('♑')
                        n += 1
                elif character == 'o':
                    if o == 0:
                        await reference.add_reaction('🇴')
                        o += 1
                    elif o == 1:
                        await reference.add_reaction('🅾️')
                        o += 1
                    elif o == 2:
                        await reference.add_reaction('⭕')
                        o += 1
                    elif o == 3:
                        await reference.add_reaction('🅾')
                        o += 1
                elif character == 'p':
                    if p == 0:
                        await reference.add_reaction('🇵')
                        p += 1
                    elif p == 1:
                        await reference.add_reaction('🅿️')
                        p += 1
                    elif p == 2:
                        await reference.add_reaction('🅿')
                        p += 1
                elif character == 'q':
                    await reference.add_reaction('🇶')
                elif character == 'r':
                    if r == 0:
                        await reference.add_reaction('🇷')
                        r += 1
                    elif r == 1:
                        await reference.add_reaction('®️')
                        r += 1
                    elif r == 2:
                        await reference.add_reaction('®')
                        r += 1
                elif character == 's':
                    await reference.add_reaction('🇸')
                elif character == 't':
                    if t == 0:
                        await reference.add_reaction('🇹')
                        t += 1
                    elif t == 1:
                        await reference.add_reaction('✝️')
                        t += 1
                    elif t == 2:
                        await reference.add_reaction('✝')
                        t += 1
                elif character == 'u':
                    if u == 0:
                        await reference.add_reaction('🇺')
                        u += 1
                    elif u == 1:
                        await reference.add_reaction('⛎')
                        u += 1
                elif character == 'v':
                    if v == 0:
                        await reference.add_reaction('🇻')
                        v += 1
                    elif v == 1:
                        await reference.add_reaction('✅')
                        v += 1
                elif character == 'w':
                    await reference.add_reaction('🇼')
                elif character == 'x':
                    if x == 0:
                        await reference.add_reaction('🇽')
                        x += 1
                    elif x == 1:
                        await reference.add_reaction('✖️')
                        x += 1
                    elif x == 2:
                        await reference.add_reaction('❎')
                        x += 1
                    elif x == 3:
                        await reference.add_reaction('❌')
                        x += 1
                elif character == 'y':
                    await reference.add_reaction('🇾')
                elif character == 'z':
                    await reference.add_reaction('🇿')
        except AttributeError:
            return