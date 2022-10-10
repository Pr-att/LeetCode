s = "(())))"
new_S = ''
i, j, k1, stack, index, string = 0, 0, 0, [], [], ''
while True:
    try:
        if s[i] == '(':
            new_S += s[i]
            stack.append(s[i])
            index.append(i)
            i += 1
            continue
        elif s[i] == ')' and len(stack) != 0:
            new_S += s[i]
            stack.pop()
            index.pop()
            i += 1
        elif s[i] != ')':
            new_S += s[i]
            i += 1
        else:
            k1 += 1
            i += 1
    except IndexError:
        if len(stack) != 0:
            l1 = [_ for _ in new_S]
            index = [i-k1 for i in index]
            index.reverse()
            for k in index:
                l1.pop(k)
            string = ''.join(l1)
            break
        else:
            string = new_S
            break

print(string)
