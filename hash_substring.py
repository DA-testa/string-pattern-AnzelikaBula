# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

    input_type = input()

    if 'I' in input_type:

        pattern = input().rstrip()
        text = input().rstrip()

    elif 'F' in input_type:

        filename = "file"

        with open("tests/" + filename, 'a') as f:

            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    return (pattern, text)


def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable


    p_l = len(pattern)
    t_l = len(text)

    p_h = hash(pattern)
    t_h = hash(text[:p_l])


    positions = []


    for i in range(t_l - p_l + 1):

        if p_h == t_h and pattern == text[i:i+p_l]:

            positions.append(i)

        if i < t_l - p_l:

            t_h = hash(text[i+1:i+p_l+1])


    return positions


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


