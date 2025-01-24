import string
counted_letters = {k: 0 for k in string.ascii_lowercase}
letter_frequencies = counted_letters

def letter_count(file):
    
    # counts each letter in a given file
    with open(file, "r") as f:
        for line in f:
            for char in line.lower():
                if char.lower() in string.ascii_lowercase:
                    if char in counted_letters:
                        counted_letters[char] += 1
                    else:
                        counted_letters[char] = 1
    f.close()
    return counted_letters

def letter_frequency(counted_values = {}):
    s = sum(letter_frequencies.values()) # adds values for total letters

    for keys, values in letter_frequencies.items():
        percent = values / s # calculates frequency
        letter_frequencies[keys] = percent #puts it in dictionary

    return letter_frequencies

    
letter_count('assert_tests.txt')
assert counted_letters['b'] == 5

letter_frequency()
assert letter_frequencies['a'] == 0.4444444444444444