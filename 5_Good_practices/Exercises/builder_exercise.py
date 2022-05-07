from abc import ABC, abstractmethod

FILE_NAME = "builder_exercise_text"


class String:
    def __init__(self):
        self._value = ""


class Director:
    def __init__(self, file_name):
        self.text = None
        self.converter = None
        self.file_name = file_name
        self.read_file(self.file_name)

    def set_converter(self, converter):
        self.converter = converter

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            self.text = f.read()

    def convert(self):
        for line in self.text.splitlines():
            for letter in line:
                self.converter.convert(letter)

    def get_text(self):
        return self.converter.get_text()


class Converter(ABC):
    def __init__(self):
        self.string = String()

    @abstractmethod
    def convert(self, text):
        pass

    @abstractmethod
    def get_text(self):
        pass


class HexConverter(Converter):
    def convert(self, text):
        # print(text, end="/")
        self.string._value += f"{text}-{hex(ord(text))}"

    def get_text(self):
        return self.string._value


class UpperConverter(Converter):
    def convert(self, text):
        # print(text, end="")
        self.string._value += text.upper()

    def get_text(self):
        return self.string._value


class LowerConverter(Converter):
    def convert(self, text):
        # print(text, end="")
        self.string._value += text.lower()

    def get_text(self):
        return self.string._value


class CounterConverter(Converter):
    def __init__(self):
        super().__init__()
        self.string._value = 0

    def convert(self, text):
        self.string._value += 1

    def get_text(self):
        return self.string._value


if __name__ == "__main__":
    director = Director(FILE_NAME)
    director.set_converter(HexConverter())
    director.convert()
    print(director.converter.get_text())

    director.set_converter(UpperConverter())
    director.convert()
    print(director.get_text())
    print(director.converter.get_text())

    director.set_converter(LowerConverter())
    director.convert()
    print(director.converter.get_text())

    director.set_converter(CounterConverter())
    director.convert()
    print(director.converter.get_text())
