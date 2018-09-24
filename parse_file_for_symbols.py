import string


def read_file():
    """Reads from a file."""
    with open('inputfile') as file_contents:
        text = file_contents.read().splitlines()
        return(text)


def ask_symbol():
    while True:
        symbol = input("What case sensitive symbol do you want to parse for: ")
        if symbol == "":
            print("Symbol needed.")
        else:
            return symbol


def ask_number():
    while True: # https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659
        try:
            number = int(input("How many of those symbols per line: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue

        if number < 1:
            print("It needs to be at least 1.")
            continue
        else:
            #shift was successfully parsed!
            #we're ready to exit the loop.
            return number


def parse_lines(symbol,number):
    """Iterates over the file line by line to find at least two dashes per line."""
    lines = read_file()
    for line in lines:
        counter = 0
        for letter in line:
            if letter == symbol:
                counter = counter + 1
        if counter > (number - 1):
            print(line)


if __name__ == "__main__":
    symbol = ask_symbol()
    number = ask_number()
    parse_lines(symbol,number)
