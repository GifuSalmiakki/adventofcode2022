
def main():
    file = open("/home/gifu/AoC/input_day1.txt")
    input = file.read()

    split_input = input.split("\n\n")
    cleaned_input = []
    for line in split_input:
        line = line.split("\n")
        if "" in line:
            line.remove("")
        ints = [int(i) for i in line]
        sums = sum(ints)
        cleaned_input.append(sums)
    cleaned_input.sort(reverse=True)
    top = 0
    for i in range(3):
        top += cleaned_input[i]
    print(top)


main()

