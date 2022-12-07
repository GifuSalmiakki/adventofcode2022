
file = open("day7_input.txt")
input = file.read()

split_input = input.split("\n")

directories = []

class Dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.children = {} # directories in this directory
        self.parent = False # parent directory

def create_directory(dir_name):

     return Dir(dir_name)

def count_files(dir, total_file_size):

    for file in dir.files:

        split_file = file.split(" ")
        total_file_size += int(split_file[0]) # <file size> filename

    if len(dir.children) == 0:
        return total_file_size

    else:
        for child in dir.children:
            count_files(child, total_file_size)


def main():
    current_directory = False
    # setting up the directory system
    for row in split_input:
        if "$" in row:
            if "cd" in row and ".." not in row:

                dir_name = row[5:]

                if not current_directory:
                    new_dir = create_directory(dir_name)
                    current_directory = new_dir

                    directories.append(new_dir)

                else:
                    current_directory = current_directory.children[dir_name]

            elif ".." in row:
                current_directory = current_directory.parent

        else:
            # prints of children in directory

            if "dir" in row:
                # subdir
                dir_name = row[4:]
                if dir_name not in current_directory.children:

                    new_dir = create_directory(dir_name)
                    new_dir.parent = current_directory
                    current_directory.children[dir_name] = new_dir

                    directories.append(new_dir)
            else:
                # file
                if row not in current_directory.files:
                    current_directory.files.append(row)

    total_file_size = 0
    total_sum = 0

    for direct in directories:
        print(direct.files)
        #file_size = count_files(direct, total_file_size)
        #print(file_size)



main()

