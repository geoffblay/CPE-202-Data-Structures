def bears(n: int) -> bool:
    if n == 42:
        # base case
        return True

    elif n > 42:
        # checks if n is still above 42
        str_n = str(n)
        lst_conditions_met = []

        if n % 2 == 0:
            # is n even
            lst_conditions_met.append(1)
        if (n % 3 == 0) or (n % 4 == 0):
            if (int(str_n[len(str_n) - 1]) != 0) and (
                    int(str_n[len(str_n) - 2]) != 0):
                # if the final 2 digits of n contain a zero, return false
                # because function will get stuck in an infinite loop of
                # giving back 0 and recursing with the same n value
                lst_conditions_met.append(2)
        if n % 5 == 0:
            # is n divisible by 5
            lst_conditions_met.append(3)

        if (1 in lst_conditions_met) and (2 in lst_conditions_met):
            # recurse with updated n values based on conditions met
            return (bears(int(n / 2))) or (bears(
                n - (int(str_n[len(str_n) - 1]) * int(str_n[len(str_n) - 2]))))
        elif (1 in lst_conditions_met) and (3 in lst_conditions_met):
            print('D')
            # recurse with updated n values based on conditions met
            return (bears(int(n / 2))) or (bears(n - 42))
        elif (2 in lst_conditions_met) and (3 in lst_conditions_met):
            # recurse with updated n values based on conditions met
            return (bears(n - (int(str_n[len(str_n) - 1]) *
                               int(str_n[len(str_n) - 2])))) or (bears(n - 42))
        elif 1 in lst_conditions_met:

            # recurse with updated n values based on conditions met
            return bears(int(n / 2))
        elif 2 in lst_conditions_met:

            # recurse with updated n values based on conditions met
            return bears(
                n - (int(str_n[len(str_n) - 1]) * int(str_n[len(str_n) - 2])))
        elif 3 in lst_conditions_met:
            # recurse with updated n values based on conditions met
            return bears(n - 42)
        else:
            # if no conditions are met, return false
            return False

    else:
        # if n does not equal 42 or is less than 42, return false
        return False
