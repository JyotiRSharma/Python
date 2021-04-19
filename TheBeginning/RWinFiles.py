fw = open("Sample.txt", 'w')
fw.write("Chant Hare Krishna and Be happy!")
fw.close()

fr = open('Sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
