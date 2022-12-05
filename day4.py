
file = open(r"C:\Users\suvis\Desktop\day4_input.txt")
input = file.read()

def main():
    count = 0
    rows = input.split("\n")
    for row in rows:
        first_pair, second_pair = row.split(",")
        first_range = first_pair.split("-")
        second_range = second_pair.split("-")

        first_range = list(map(lambda i: int(i), first_range))
        second_range = list(map(lambda i: int(i), second_range))
        print(first_range, second_range)
        # check how many do not overlap
        if first_range[1] < second_range[0] or first_range[0] > second_range[1]:
            count += 1
        elif second_range[1] < first_range[0] or second_range[0] > first_range[1]:
            count += 1

    # find overlapping rows, count = amount of rows NOT overlapping
    row_amount = len(rows)
    overlap = row_amount-count
    print(overlap)





main()