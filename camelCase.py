def main():
    # take name input in camelCase
    name = input("camelCase: ")

    # split each word and make them lower case
    name = split_uppercase(name)

    # add _ between each word
    name = "_".join(name)

    # output name in snake_case
    print("snake_case: ", name)

def split_uppercase(s):
    result = []
    current_word = []
    for char in s:
        if char.isupper() and current_word: # If uppercase and not the first character
            result.append("".join(current_word).lower())
            current_word = [char]
        else:
            current_word.append(char)
    result.append("".join(current_word).lower()) # Append the last word
    return result


main()