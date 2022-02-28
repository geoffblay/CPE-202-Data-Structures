def convert(num: int, base: int) -> str:
    if num == 0:
        # base case
        return ''

    else:
        remainder = num % base

        # base symbols
        if remainder == 10:
            rem_str = 'A'
        elif remainder == 11:
            rem_str = 'B'
        elif remainder == 12:
            rem_str = 'C'
        elif remainder == 13:
            rem_str = 'D'
        elif remainder == 14:
            rem_str = 'E'
        elif remainder == 15:
            rem_str = 'F'
        else:
            rem_str = str(num % base)

        # recurse with new values
        return (str(convert(num // base, base))) + rem_str
