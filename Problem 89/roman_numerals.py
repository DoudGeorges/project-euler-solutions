values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

inverted_values = {val: letter for letter, val in values.items()}

def to_number(roman: str) -> int:
    length = len(roman)
    number = 0
    idx = 0
    while idx < length:
        val = values[roman[idx]]
        if idx + 1 < length:
            next_val = values[roman[idx + 1]]
            if val < next_val:
                val = next_val - val
                idx += 1

        number += val
        idx += 1

    return number

def to_roman(number: int) -> str:
    number = str(number)
    length = len(number)
    roman = ""
    for idx in range(length):
        val = int("1" + "0" * (length - idx - 1))
        num = int(number[idx])
        if val == 1000:
            roman += inverted_values[val] * num
        else:
            if num == 9:
                roman += inverted_values[val] + inverted_values[val * 10]
            elif num == 4:
                roman += inverted_values[val] + inverted_values[val * 5]
            elif num >= 5:
                roman += inverted_values[val * 5] + inverted_values[val] * (num - 5)
            else:
                roman += inverted_values[val] * num
    
    return roman

def minimize(roman: str) -> str:
    return to_roman(to_number(roman))

if __name__ == "__main__":
    original = ""
    minimized = ""
    with open("Problem 89/roman.txt") as numerals:
        for roman in numerals:
            roman = roman.strip()
            original += roman
            minimized += minimize(roman)

    original = len(original)
    minimized = len(minimized)

    print(f"Original: {original} chars\nMinimized: {minimized} chars\n(Saved {original - minimized} chars)")