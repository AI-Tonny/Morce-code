morse_code = {
    "a": "·-", "b": "-···", "c": "-·-·", "d": "-··", "e": "·",
    "f": "··-·", "g": "--·", "h": "····", "i": "··", "j": "·---",
    "k": "-·-", "l": "·-··", "m": "--", "n": "-·", "o": "---",
    "p": "·--·", "q": "--·-", "r": "·-·", "s": "···", "t": "-",
    "u": "··-", "v": "···-", "w": "·--", "x": "-··-", "y": "-·--",
    "z": "--··",
    "1": "·----", "2": "··---", "3": "···--", "4": "····-",
    "5": "·····", "6": "-····", "7": "--···", "8": "---··",
    "9": "----·", "0": "-----",
    " ": " "
}


def convert_to_morse(text):
    """
    Converts a given string of text into Morse code using the `morse_code` dictionary.
    Loops through each character in the input text, finds its Morse code equivalent,
    and combines them with spaces to create a single Morse code string.

    :param text: The input string to be translated to Morse code.
    :return: A string of Morse code representing the input text.
    """
    translator = [morse_code[char] for char in text if char in morse_code]
    result_code = ' '.join(translator)

    return result_code


def convert_from_morse(text):
    """
    Converts a Morse code string back into English text.
    Splits the Morse code input into separate codes, finds their English equivalents,
    and combines them into a single string with capitalized first letter.

    :param text: A string of Morse code to be translated into text.
    :return: A string of English text representing the input Morse code.
    """
    translator = [keys for code in text.split() for keys in morse_code if morse_code[keys] == code]
    result_code = ''.join(translator).capitalize()

    return result_code


def main():
    """
    Main function to run the Morse code converter program.
    Presents a menu to the user with options to convert text to Morse code,
    translate Morse code back to text, or exit the program.
    Loops until the user selects the exit option.

    Starts by displaying the menu, then prompts for user input to select an option.
    Based on the choice, it calls `convert_to_morse` or `convert_from_morse`
    to perform the respective translations and displays the results.

    Exits the program if the user selects option '3'.
    """
    input('Press enter to start...')
    print('-------------------------------')

    print("Menu")
    print("1. Convert to Morse Code")
    print("2. Translate Morse Code")
    print("3. Exit")
    while (choice := input("Enter your choice: ")) != "3":
        match choice:
            case "1":
                text = input("Enter text for translation on morse code: ").lower()
                result = convert_to_morse(text)

                print(f'Morse-code: {result}')
            case "2":
                morse = input("Enter morse code to translate into text: ")
                result = convert_from_morse(morse)

                print(f"Text: {result}")
            case _:
                print("Invalid input, try again")

    print("Exiting...")


if __name__ == '__main__':
    main()
