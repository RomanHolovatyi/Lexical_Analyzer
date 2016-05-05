from collections import namedtuple

tsymbol = namedtuple("tsymbol", "value attr")
letters = "abcdefghigklmnopqrstuvwxyz"
digits = "0123456789"
whitespaces = [' ', '\n', '\t', '\r', '\f']
key_words = {'program': 501,
             'const': 502,
             'begin': 503,
             'end': 504,
             'procedure': 505,
             'integer': 506,
             'float': 507,
             }
delimiters = {
    ';': ord(';'),
    ',': ord(','),
    ':': ord(':'),
    '=': ord('='),
    '(': ord('('),
    ')': ord(')'),
}
code_dict = {}
code_list = []
constTab = {}
variables_tab = {}
errors = []