def print_numbers(data):
   

    for line in data.splitlines():
        for word in line.split():
            if word.isdigit():
                print(word)


def get_file_size(filename):
   

    import os

    return os.path.getsize(filename)


def main():
    filename = "numbers.txt"

    data = read_file(filename)
    print_numbers(data)

    file_size = get_file_size(filename)
    print("The size of the file is {} bytes.".format(file_size))


