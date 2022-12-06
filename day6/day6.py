
from collections import Counter

file = open("day6_input.txt")
input = file.read()
test_input = "nppdvjthqldpwncqszvftbrmjlhg"
def main():

    found = False
    for index in range(len(input)+1):
        if index >= 3 and not found:
            group_of_four = input[index-4:index]
            unique_chars = ""
            for char in group_of_four:
                if char not in unique_chars:
                    unique_chars += char

                if len(unique_chars) == 4:
                    print(index)
                    found = True
                else:
                    pass

main()