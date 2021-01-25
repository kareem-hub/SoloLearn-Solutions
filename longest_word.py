#take & store words in a list
txt = input().split()
#get length of longest word in the txt list
maxwrd=max(len(i) for i in txt)
#loop over txt, if the word length == maxwrd print the word
for word in txt:
    if len(word)==maxwrd:
        print(word)