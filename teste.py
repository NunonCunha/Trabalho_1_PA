text = open("text.txt", "r")

d = dict()

for line in text:

    line = line.strip()

    line = line.lower()    

    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

print(d)