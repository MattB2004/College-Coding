import letters

def highest_freq(file):
    dic = letters.letter_count(file) # counts the amount of each letters in a file

    global max_freq
    global max_letter
    

    max_freq = max(dic.values()) # finds max value within dictionary
    max_freq = max_freq/sum(dic.values()) # turns max frequency into a frequency
    max_letter = max(dic, key=dic.get) # fetches letter of value

    return max_letter, max_freq

highest_freq('assert_tests.txt')
assert max_letter == 'b'