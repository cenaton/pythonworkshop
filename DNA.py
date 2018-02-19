C = 0
G = 0
text_file = open("DNA.txt").read()
total=len(text_file)


for i in range(len(text_file)):
    if text_file[i] == "C":
        C=C+1.00

    if text_file[i] == "G":
        G=G+1.00

print "The total number of C: ", C
print "The total number of G: ", G
print "The total number of DNA:", len(text_file)
print "The Percent of C and G is:", ((C+G)/total)*100
