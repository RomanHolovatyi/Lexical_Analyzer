from tables import *


def get_symbol_attribute(char):
    if char in whitespaces:
        return 0
    elif char in digits:
        return 1
    elif char in letters:
        return 2
    elif char == "(":
        return 3
    elif char in delimiters:
        return 4
    else:
        return 5


class LexicalAnalyzer:
    identifiers = {}
    constants = {}
    errors = []

    def gets(self, f):
        char = f.read(1).lower()
        new_symbol = tsymbol(char, get_symbol_attribute(char))
        return new_symbol

    def scan(self):
        lex_code = 0
        open("test.txt", 'w').close()
        with open("test.dat") as f:
                symbol = self.gets(f)
                while True:
                    flag = False
                    buffer = ""
                    if symbol.value == '':
                        break
                    lex_code = 0
                    while symbol.attr == 0 and symbol.value != '':  # Whitespaces
                        symbol = self.gets(f)
                    if symbol.attr == 2:  # identifier
                        while symbol.attr == 2 or symbol.attr == 1 and symbol.value != '':
                            buffer += symbol.value
                            symbol = self.gets(f)
                        if buffer in key_words:
                            lex_code = key_words[buffer]
                        elif buffer in variables_tab:
                            lex_code = variables_tab[buffer]
                        else:
                            lex_code = len(variables_tab) + len(key_words) + 501
                            variables_tab[buffer] = lex_code
                    elif symbol.attr == 3:  # comments
                            symbol = self.gets(f)
                            if symbol.value != '*':
                                lex_code = ord('(')
                                buffer = "("
                            else:
                                while symbol.value != ')':
                                    while symbol.value != '*':
                                        if symbol.value == '':
                                            errors.append("Expected *) but end of file was found")
                                            break
                                        symbol = self.gets(f)
                                    flag = True  # because of empty symbol is in buffer
                                    if symbol.value == '':
                                        errors.append("Expected *) but end of file was found")
                                        break
                                    symbol = self.gets(f)
                                symbol = self.gets(f)
                    elif symbol.attr == 4:  # delimiters
                        buffer = symbol.value
                        lex_code = delimiters[buffer]
                        symbol = self.gets(f)
                    elif symbol.attr == 5:  # Error
                        errors.append("Wrong symbol: %s" % symbol.value)
                    if flag != True:
                        with open("test.txt", "a") as output_file:
                            output_file.write(buffer + " : " + str(lex_code) + "\n")


if __name__ == '__main__':
    la = LexicalAnalyzer()
    la.scan()
    with open("test.txt", "a") as output_file:
        output_file.write("---------------------")
        output_file.write("Variable Table")
        output_file.write("---------------------")
        output_file.write("\n" + "|Name      Code|" + "\n")
        for i in variables_tab:
            output_file.write(i + "       " + str(variables_tab[i]) + "\n")
