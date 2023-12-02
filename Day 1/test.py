import re

def main():
    input = ["fourtwojrvzzctzs5eight2vlm", "52sevenone"]

    repl = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    replace_pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine))")
    replace_input = [replace_pattern.sub(lambda x: repl.get(x.group(1), ""), i) for i in input]

    print(replace_input)
if __name__ == "__main__":
    main()