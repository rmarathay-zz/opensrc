file = open('words.txt','r')

for line in file:
    words = line.split()
    for word in words:
        word0 = ord(word[0])-96
        word1 = ord(word[1])-96
        word2 = ord(word[2])-96
        word3 = ord(word[3])-96
        word4 = ord(word[4])-96
        total = word0+word1+word2+word3
        # print total
        # print ord(word[4]) - 96
        if(total == word4):
            print word
