i_fileName = input("Enter the input file name: ")
o_fileName = input("Enter the output file name: ")

with open(i_fileName, 'r') as f, open(o_fileName, 'w') as w:
    number = 0
    for line in f:
        number += 1
        w.write('{:>4}> {}'.format(number, line))

input("Press ENTER to close")
