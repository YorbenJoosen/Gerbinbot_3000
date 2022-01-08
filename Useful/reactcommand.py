async def reactcommand(message, emojiguild):
    emojis = await emojiguild.fetch_emojis()
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
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            i = 0
            j = 0
            k = 0
            l = 0
            m = 0
            n = 0
            o = 0
            p = 0
            q = 0
            r = 0
            s = 0
            t = 0
            u = 0
            v = 0
            w = 0
            x = 0
            y = 0
            z = 0
            for iterator in range(0, length):
                character = content[iterator]
                if character == 'a':
                    if a == 0:
                        await reference.add_reaction('🇦')
                        a += 1
                    elif a == 1:
                        await reference.add_reaction(emojis[0])
                        a += 1
                    elif a == 2:
                        await reference.add_reaction(emojis[26])
                        a += 1
                elif character == 'b':
                    if b == 0:
                        await reference.add_reaction('🇧')
                        b += 1
                    elif b == 1:
                        await reference.add_reaction(emojis[1])
                        b += 1
                    elif b == 2:
                        await reference.add_reaction(emojis[27])
                        b += 1
                elif character == 'c':
                    if c == 0:
                        await reference.add_reaction('🇨')
                        c += 1
                    elif c == 1:
                        await reference.add_reaction(emojis[2])
                        c += 1
                    elif c == 2:
                        await reference.add_reaction(emojis[28])
                        c += 1
                elif character == 'd':
                    if d == 0:
                        await reference.add_reaction('🇩')
                        d += 1
                    elif d == 1:
                        await reference.add_reaction(emojis[3])
                        d += 1
                    elif d == 2:
                        await reference.add_reaction(emojis[29])
                        d += 1
                elif character == 'e':
                    if e == 0:
                        await reference.add_reaction('🇪')
                        e += 1
                    elif e == 1:
                        await reference.add_reaction(emojis[4])
                        e += 1
                    elif e == 2:
                        await reference.add_reaction(emojis[30])
                        e += 1
                elif character == 'f':
                    if f == 0:
                        await reference.add_reaction('🇫')
                        f += 1
                    elif f == 1:
                        await reference.add_reaction(emojis[5])
                        f += 1
                    elif f == 2:
                        await reference.add_reaction(emojis[31])
                        f += 1
                elif character == 'g':
                    if g == 0:
                        await reference.add_reaction('🇬')
                        g += 1
                    elif g == 1:
                        await reference.add_reaction(emojis[6])
                        g += 1
                    elif g == 2:
                        await reference.add_reaction(emojis[32])
                        g += 1
                elif character == 'h':
                    if h == 0:
                        await reference.add_reaction('🇭')
                        h += 1
                    elif h == 1:
                        await reference.add_reaction(emojis[7])
                        h += 1
                    elif h == 2:
                        await reference.add_reaction(emojis[33])
                        h += 1
                elif character == 'i':
                    if i == 0:
                        await reference.add_reaction('🇮')
                        i += 1
                    elif i == 1:
                        await reference.add_reaction(emojis[8])
                        i += 1
                    elif i == 2:
                        await reference.add_reaction(emojis[34])
                        i += 1
                elif character == 'j':
                    if j == 0:
                        await reference.add_reaction('🇯')
                        j += 1
                    elif j == 1:
                        await reference.add_reaction(emojis[9])
                        j += 1
                    elif j == 2:
                        await reference.add_reaction(emojis[35])
                        j += 1
                elif character == 'k':
                    if k == 0:
                        await reference.add_reaction('🇰')
                        k += 1
                    elif k == 1:
                        await reference.add_reaction(emojis[10])
                        k += 1
                    elif k == 2:
                        await reference.add_reaction(emojis[36])
                        k += 1
                elif character == 'l':
                    if l == 0:
                        await reference.add_reaction('🇱')
                        l += 1
                    elif l == 1:
                        await reference.add_reaction(emojis[11])
                        l += 1
                    elif l == 2:
                        await reference.add_reaction(emojis[37])
                        l += 1
                elif character == 'm':
                    if m == 0:
                        await reference.add_reaction('🇲')
                        m += 1
                    elif m == 1:
                        await reference.add_reaction(emojis[12])
                        m += 1
                    elif m == 2:
                        await reference.add_reaction(emojis[38])
                        m += 1
                elif character == 'n':
                    if n == 0:
                        await reference.add_reaction('🇳')
                        n += 1
                    elif n == 1:
                        await reference.add_reaction(emojis[13])
                        n += 1
                    elif n == 2:
                        await reference.add_reaction(emojis[39])
                        n += 1
                elif character == 'o':
                    if o == 0:
                        await reference.add_reaction('🇴')
                        o += 1
                    elif o == 1:
                        await reference.add_reaction(emojis[14])
                        o += 1
                    elif o == 2:
                        await reference.add_reaction(emojis[40])
                        o += 1
                elif character == 'p':
                    if p == 0:
                        await reference.add_reaction('🇵')
                        p += 1
                    elif p == 1:
                        await reference.add_reaction(emojis[15])
                        p += 1
                    elif p == 2:
                        await reference.add_reaction(emojis[41])
                        p += 1
                elif character == 'q':
                    if q == 0:
                        await reference.add_reaction('🇶')
                        q += 1
                    elif q == 1:
                        await reference.add_reaction(emojis[16])
                        q += 1
                elif character == 'r':
                    if r == 0:
                        await reference.add_reaction('🇷')
                        r += 1
                    elif r == 1:
                        await reference.add_reaction(emojis[17])
                        r += 1
                    elif r == 2:
                        await reference.add_reaction(emojis[42])
                        r += 1
                elif character == 's':
                    if s == 0:
                        await reference.add_reaction('🇸')
                        s += 1
                    elif s == 1:
                        await reference.add_reaction(emojis[18])
                        s += 1
                    elif s == 2:
                        await reference.add_reaction(emojis[43])
                        s += 1
                elif character == 't':
                    if t == 0:
                        await reference.add_reaction('🇹')
                        t += 1
                    elif t == 1:
                        await reference.add_reaction(emojis[19])
                        t += 1
                    elif t == 2:
                        await reference.add_reaction(emojis[44])
                        t += 1
                elif character == 'u':
                    if u == 0:
                        await reference.add_reaction('🇺')
                        u += 1
                    elif u == 1:
                        await reference.add_reaction(emojis[20])
                        u += 1
                    elif u == 2:
                        await reference.add_reaction(emojis[45])
                        u += 1
                elif character == 'v':
                    if v == 0:
                        await reference.add_reaction('🇻')
                        v += 1
                    elif v == 1:
                        await reference.add_reaction(emojis[21])
                        v += 1
                    elif v == 2:
                        await reference.add_reaction(emojis[46])
                        v += 1
                elif character == 'w':
                    if w == 0:
                        await reference.add_reaction('🇼')
                        w += 1
                    elif w == 1:
                        await reference.add_reaction(emojis[22])
                        w += 1
                    elif w == 2:
                        await reference.add_reaction(emojis[47])
                        w += 1
                elif character == 'x':
                    if x == 0:
                        await reference.add_reaction('🇽')
                        x += 1
                    elif x == 1:
                        await reference.add_reaction(emojis[23])
                        x += 1
                    elif x == 2:
                        await reference.add_reaction(emojis[48])
                        x += 1
                elif character == 'y':
                    if y == 0:
                        await reference.add_reaction('🇾')
                        y += 1
                    elif y == 1:
                        await reference.add_reaction(emojis[24])
                        y += 1
                elif character == 'z':
                    if z == 0:
                        await reference.add_reaction('🇿')
                        z += 1
                    elif z == 1:
                        await reference.add_reaction(emojis[25])
                        z += 1
                    #elif z == 2:
                    #    await reference.add_reaction(emojis[49])
                    #    z += 1
        except AttributeError:
            return
