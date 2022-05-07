def snake_talk(sentence: str):
    list_of_words = sentence.split()

    for index, word in enumerate(list_of_words):
        if (index + 1) % 3 == 0:
            list_of_words[index] = word.title()
        elif (index + 1) % 4 == 0:
            list_of_words[index] = word + "!"
    return " ".join(list_of_words)


print(snake_talk("Write a program that will display the given sentence."))