import string

lower_values = [*range(1, 27, 1)]
upper_values = [*range(27, 53, 1)]

lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)

dict_lower = {}
dict_upper = {}
for a in lower_alphabet:
    dict_lower[a] = lower_values[lower_alphabet.index(a)]

for A in upper_alphabet:
    dict_upper[A] = upper_values[upper_alphabet.index(A)]


def split_list(list):
    half = len(list)//2
    return list[:half], list[half:]

def day3_part1():

    file = open(r"C:\Users\suvis\Desktop\day3_input.txt")
    input = file.read()

    rows = input.split("\n")
    priority_sum = 0
    for row in rows:
        found = False # Count each matching item only once:
                      # i.e. aab and abc have one matching letter "a"
        first_half, second_half = split_list(row)

        for char in first_half:
            if char in second_half and not found:
                found = True
                if char.upper() == char:
                    priority = dict_upper[char]
                    priority_sum += priority
                else:
                    priority = dict_lower[char]
                    priority_sum += priority

    print(priority_sum)

def main():
    # part 2 code
    file = open(r"C:\Users\suvis\Desktop\day3_input.txt")
    input = file.read()

    rows = input.split("\n")
    priority_sum = 0
    for i in range(0, len(rows)-2, 3): # split rows into groups of three

        found = False # count each matching element only once
        for char in rows[i]:
            if char in rows[i+1] and char in rows[i+2] and not found:
                found = True
                if char.upper() == char:
                    priority = dict_upper[char]
                    priority_sum += priority
                else:
                    priority = dict_lower[char]
                    priority_sum += priority

    print(priority_sum)



main()

