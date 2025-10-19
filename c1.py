with open('codingal.txt','r')as f2:
    data = f2.readlines()
    for line in data:
        word = line.split()
        print(word)

    f2.close()