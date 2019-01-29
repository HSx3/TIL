def bruteForce(text, pattern):
    i, j =0, 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return i

def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt =0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt += 1
        if(cnt >= len(pattern)) : return i
    return -1


text = "TTTTAACCA"
pattern = "TTA"
print("{}".format(bruteForce(text, pattern)))
print("{}".format(bruteForce2(text, pattern)))
print(text.find(pattern))