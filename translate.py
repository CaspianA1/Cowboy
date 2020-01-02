# translate.py

import os

trans_dict = {
    "MY GUN DOES THE TALKING": "try",
    "TOUGH AS NAILS": "except",
    "ACE IN THE HOLE": "finally",
    "ARY": "or",
    "IS ALL-STANDINGLY": "is",
    "AMONG THE WILLOWS": "not",
    "OUT OF THE SALOON": "nonlocal",
    "LAY DOWN THE LAW FOR": "class",
    "DOUBLE WHAMMY": "async",
    "HOLD YOUR HORSES": "await",
    "WHEN HE KEEPS ON WITH ": "while",
    "ATWEEN": "and",
    "FROM YONDER": "from",
    "BETWEEN HAY AND GRASS": "as",
    "OUTSIDER, THAT": "global",
    "SHUT YOUR BIG BAZOO": "break",
    "LET IT GO": "pass",
    "IN MY EYE": "False",
    "A SON OF A GUN": "True",
    "ARE YOU SURE ABOUT THAT": "assert",
    "TAKE HIM ALONG,": "import",
    "COTTONWOOD BLOSSOM": "del",
    "IF THE": "if",
    "HOW ABOUT": "elif",
    "LAST CHANCE": "else",
    "AIR THE LUNGS": "raise",
    "OLD DAN DELIVERS": "return",
    "PASS THE PROG": "yield",
    "IN THIS COUNTY OF": "in",
    "HERE'S THE PLAN": "lambda",
    "A BEE IN YOUR BONNET": "def",
    "FROM": "from",
    "FOR EVERY DARN": "for",
    "GIDDY UP": "continue",
    "WIT": "with",
    "BURROW MILK": "None",
    "IS JUST AS GOOD AS": "=",
    "IS JUST LIKE AN OLD FASHIONED": "==",
    "DOWN SHE GOES": "-",
    "YAR SHE GOES": "+",
    "IS OUTRIGHT WORSE THAN A": "<",
    "IS OUTRIGHT BETTER THAN A": ">",
    "DON'T TAKE HER AWAY": "+=",
    "TAKE HER AWAY": "-=",
}


def translate_file(file_name):
    os.system(["clear", "cls"][os.name == "nt"])
    with open(f"{file_name}", "r") as text_in:
        for line in text_in.readlines():
            result = line
            for key in trans_dict.keys():
                result = result.replace(key, trans_dict[key])
            with open("text_out.py", "a") as text_out:
                text_out.write(result)

        print("Process complete")
