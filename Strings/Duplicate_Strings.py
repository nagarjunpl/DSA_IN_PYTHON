def printDuplicates(s):
    s = ''.join(sorted(s))

    i = 0
    while i < len(s):
        count = 1
        
        while i + count < len(s) and s[i] == s[i + count]:
            count += 1

        if count > 1:
            print(f"['{s[i]}', {count}]")

        i += count

s = "nagarjun p l"
printDuplicates(s)
