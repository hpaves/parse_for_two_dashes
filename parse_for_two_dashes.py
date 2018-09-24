import string


def read_file():
    """Reads from a file."""
    with open('dashes') as file_contents:
        text = file_contents.read().splitlines()
        return(text)


def parse_for_two_dashes():
    """Iterates over the file line by line to find at least two dashes per line."""
    lines = read_file()
    for line in lines:
        counter = 0
        for letter in line:
            if letter == "-":
                counter = counter + 1
        if counter > 1:
            print(line)


if __name__ == "__main__":
    parse_for_two_dashes()
