import re

def main(input):
    res = 0


    for line in input:
        digit = ""


        for ch in line:
            if ch.isdigit():
                digit += ch

        res += int(digit[0] + digit[-1])

    print(res)
    return res


import re
def main2():

    input_file = "input.txt"
    replace_pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine))")
    replace_input = []
    word_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five" : "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    with open(input_file, "r") as f:
        replace_input = [replace_pattern.sub(lambda x: word_to_num.get(x.group(1), ""), i) for i in f]

    main(replace_input)


if __name__ == "__main__":
    main2()