word = "ABFCACDB"
stack =[]
for x in word:
    if x == "B" and stack and stack[-1] == "A":
        stack.pop()
    elif x == "D" and stack and stack[-1] == "C":
        stack.pop()
    else:
        stack.append(x)
print(len(stack))





                                    # ░█▀▀▀█ ▀▀█▀▀ ─█▀▀█ ░█▀▀█ ░█─▄▀ 　 ░█▀▀█ ─█▀▀█ ░█─── ░█─── 　 ░█▀▀▀ ░█─░█ ░█▄─░█ ░█▀▀█ ▄▀ ▀▄ 
                                    # ─▀▀▀▄▄ ─░█── ░█▄▄█ ░█─── ░█▀▄─ 　 ░█─── ░█▄▄█ ░█─── ░█─── 　 ░█▀▀▀ ░█─░█ ░█░█░█ ░█─── █─ ─█ 
                                    # ░█▄▄▄█ ─░█── ░█─░█ ░█▄▄█ ░█─░█ 　 ░█▄▄█ ░█─░█ ░█▄▄█ ░█▄▄█ 　 ░█─── ─▀▄▄▀ ░█──▀█ ░█▄▄█ ▀▄ ▄▀