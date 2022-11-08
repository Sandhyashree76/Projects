def perm(strg,i=0):
    if i==len(strg):
        print("".join(strg))
    for j in range(i,len(strg)):
        word=[c for c in strg]

        word[i],word[j]= word[j],word[i]
        perm(word,i+1)
print(perm("man"))
