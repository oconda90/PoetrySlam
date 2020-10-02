from random import choice, randint

def get_file_lines(filename):
    infile = open(filename, 'r')
    read_poem = infile.readlines()
    infile.close()
    return read_poem
#print(get_file_lines('Poetry-slam/poem.txt'))

def lines_printed_backwards(lines_list):
    num_lines = (len(lines_list))
    lines_list = lines_list[::-1]

    for i in range(num_lines):
       v = str(num_lines - i) + " " + lines_list[i]
       print(v)
f = open('Poetry-slam/poem.txt', 'r')
poem = (f.read().splitlines())
lines_printed_backwards(poem)
f.close()

def lines_printed_random(lines_list):
    for random_index in range(len(lines_list)):
        random_index = (randint(0, len(lines_list)-1)) 
        print(lines_list[random_index])
        
lines_printed_random(poem)
f.close()

def lines_printed_custom(lines_list):
    num_lines = len(lines_list)
    for i in range(num_lines):
        if i % 2 == 0:
            print(str(i) + " " +  lines_list[i])
    return []
lines_printed_custom(poem)
f.close()
