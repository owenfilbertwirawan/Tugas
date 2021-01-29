import sys


string1 = ""
alphabets = digits = special = 0

for line in sys.stdin:
    string1 = line
    for i in range(len(string1)):
        if((string1[i] >= 'a' and string1[i] <= 'z') or (string1[i] >= 'A' and string1[i] <= 'Z')): 
            alphabets = alphabets + 1 
        elif(string1[i] >= '0' and string1[i] <= '9'):
            digits = digits + 1
        else:
            special = special + 1

sys.stdout.write("Total angka: " + str(digits))
sys.stdout.write('\n')
sys.stdout.write("Total huruf: " + str(alphabets))
sys.stdout.write('\n')
sys.stdout.write("Total symbol: " + str(special))
sys.stdout.write('\n')
