def file_reader(file):
    with open(file) as textfile:
        print(textfile.read().swapcase())

        # for line in textfile.readlines():
        #     print(line)
        #     print(line.swapcase())


file_reader("sentences.txt")
