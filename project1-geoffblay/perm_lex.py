from __future__ import annotations


def perm_gen_lex(string: str) -> list[str]:
    if len(string) == 0:
        # base case
        return ['']

    else:
        perm_lst = []
        for char in string:
            # remove each character in the string one at a time to make
            # simpler strings, recurse with simpler strings to find simple
            # permutations
            simple_str = string.replace(char, '')
            perms_simple_str = perm_gen_lex(simple_str)
            for i in range(0, len(perms_simple_str)):
                # add removed character to simple permutations and add it to
                # list to be returned
                perm_lst.append(char + perms_simple_str[i])
        return perm_lst
