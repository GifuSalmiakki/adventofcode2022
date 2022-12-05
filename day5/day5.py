import string

file = open("/home/gifu/AoC/day5/day5_input.txt")
input = file.read()

split_input = input.split("\n")

# reading input manually, easier than working with indices
starting_stacks = [["G", "T", "R", "W"], ["G", "C", "H", "P", "M", "S", "V", "W"], ["C", "L", "T", "S", "G", "M"],
                   ["J", "H", "D", "M", "W", "R", "F"], ["P", "Q", "L", "H", "S", "W", "F", "J"],
                   ["P", "J", "D", "N", "F", "M", "S"], ["Z", "B", "D", "F", "G", "C", "S", "J"],
                   ["R", "T", "B"], ["H", "N", "W", "L", "C"]]

test_stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
test_instructions = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]

# creating stacks
stacks = []
for i in range(0, 9, 1):
    stack = starting_stacks[i]
    stacks.append(stack)

instructions = split_input[10:]

def day5_part1():

    for row in instructions:
        split_row = row.split(" ")

        if len(split_row) > 1:

            nro_of_crates = int(split_row[1])
            from_stack = int(split_row[3])-1
            to_stack = int(split_row[5])-1

            i = 0
            while i < nro_of_crates:
                crate_to_move = stacks[from_stack].pop()
                stacks[to_stack].append(crate_to_move)
                i += 1

    # getting top-crate of each stack
    for stack in stacks:
        print(stack.pop())


def main():

    for row in instructions:
        split_row = row.split(" ")

        if len(split_row) > 1:

            nro_of_crates = int(split_row[1])
            from_stack = int(split_row[3])-1
            to_stack = int(split_row[5])-1

            # adding crates
            index = len(stacks[from_stack])-nro_of_crates
            crates_to_move = stacks[from_stack][index:]
            stacks[to_stack] = stacks[to_stack] + crates_to_move

            # removing crates
            i = 0
            while i < nro_of_crates:
                stacks[from_stack].pop()
                i += 1

    # getting top-crate of each stack
    for stack in stacks:
        print(stack.pop())


main()