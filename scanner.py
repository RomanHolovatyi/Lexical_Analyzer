from tables import *
from prettytable import PrettyTable


class EOFException(Exception):
    pass


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
        # new_symbol = tsymbol()
        char = f.read(1).lower()
        # print(char, end="")
        # if not char:
        #     raise EOFException
        # return Symbol(char, get_symbol_attribute(char))
        new_symbol = tsymbol(char, get_symbol_attribute(char))
        return new_symbol

    def scan(self):
        # read_flag = True
        # res = []
        lex_code = 0
        with open("test.dat") as f:
            try:
                symbol = self.gets(f)
                while True:
                    fuck = False
                    buffer = ""
                    if symbol.value == '':
                        break
                    lex_code = 0
                    while symbol.attr == 0 and symbol.value != '':  # Whitespaces
                        symbol = self.gets(f)
                    # elif symbol.attr == 1:  # Constant
                    #     while symbol.attr == 1:
                    #         buffer += symbol.value
                    #         symbol = gets(f)
                    if symbol.attr == 2:  # identifier
                        while symbol.attr == 2 or symbol.attr == 1:
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
                        try:
                            second_symbol = self.gets(f)
                            # ???
                            if second_symbol != '*':
                                lex_code = ord('(')
                                buffer = "("
                            else:
                                while symbol.value != ')':
                                    symbol = self.gets(f)
                                    while symbol.value != '*':
                                        symbol = self.gets(f)
                        except EOFException:
                            errors.append("Expected *) but end of file was found")
                            pass
                    elif symbol.attr == 4:  # delimiters
                        buffer = symbol.value
                        lex_code = delimiters[buffer]
                        symbol = self.gets(f)
                    elif symbol.attr == 5:  # Error
                        errors.append("Wrong symbol: %s" % symbol.value)
                    if fuck != True:
                        code_list.append(lex_code)
                        lexeme_list.append(buffer)
            except EOFException:
                pass

if __name__ == '__main__':
    la = LexicalAnalyzer()
#    la.prerry_print()
    la.scan()
    for i in lexeme_list, code_list:
        print(i)