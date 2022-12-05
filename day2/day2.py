
dict = {}
dict["A"] = 1 # rock
dict["X"] = 1 # lose

dict["B"] = 2 # paper
dict["Y"] = 2 # draw

dict["C"] = 3 # scissors
dict["Z"] = 3 # win

def main():

    points = 0
    file = open("/home/gifu/AoC/day2_input.txt")
    input = file.read()
    split_input = input.split("\n")
    print(len(split_input))

    for row in range(len(split_input)):
        row = split_input[row].replace(" ", "")

        if row[0] == "A":
            if row[1] == "X":
                points += 3 # lose with scissors
            elif row[1] == "Y":
                points += (1 + 3) # draw with rock
            else:
                # AZ
                points += (2 + 6) # win with paper

        elif row[0] == "B":
            if row[1] == "X":
                points += 1 # lose with rock
            elif row[1] == "Y":
                points += (2 + 3) # draw with paper
            else:
                # BZ
                points += (3 + 6) # win with scissors

        elif row[0] == "C":
            if row[1] == "X":
                points += 2 # lose with paper
            elif row[1] == "Y":
                points += (3 + 3) # draw with scissors
            else:
                # CZ
                points += (1 + 6)


        print(points)



main()



