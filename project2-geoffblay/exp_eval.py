from array_stack import push, pop, peek, is_empty, size, ArrayStack


def postfix_eval(input_string: str) -> float:
    """Evaluates the given RPN expression.

    Args:
        input_string: an RPN expression

    Returns:
        The result of the expression evaluation

    Raises:
        ValueError: if the input is not well-formed
        ZeroDivisionError: if the input would cause division by zero
    """

    if input_string == '':
        raise ValueError('empty input')

    input_lst = input_string.split()
    eval_stack = ArrayStack(len(input_lst))

    for token in input_lst:
        try:
            value = float(token)
            push(eval_stack, value)
        except ValueError:
            if token != '+' and token != '-' and token != '*' and token != '/'\
                    and token != '//' and token != '**':
                raise ValueError('invalid token')

            val1 = pop(eval_stack)
            try:
                val2 = pop(eval_stack)
            except IndexError:
                raise ValueError('insufficient operands')

            if token == '+':
                push(eval_stack, val2 + val1)
            elif token == '-':
                push(eval_stack, val2 - val1)
            elif token == '*':
                push(eval_stack, val2 * val1)
            elif token == '/':
                if val1 == 0:
                    raise ZeroDivisionError
                push(eval_stack, val2 / val1)
            elif token == '//':
                if val1 == 0:
                    raise ZeroDivisionError
                push(eval_stack, val2 // val1)
            elif token == '**':
                push(eval_stack, val2 ** val1)

    ret = pop(eval_stack)
    if is_empty(eval_stack):
        return ret

    raise ValueError('too many operands')


def infix_to_postfix(input_string: str) -> str:
    """Converts the given infix string to RPN.

    Args:
        input_string: an infix expression

    Returns:
        The equivalent expression in RPN
    """
    input_lst = input_string.split()
    eval_stack = ArrayStack(len(input_lst))
    rpn_expression = ''

    for token in input_lst:
        try:
            value = float(token)

            if '.' in token:
                rpn_expression += (str(float(value)) + ' ')
            else:
                rpn_expression += (str(int(value)) + ' ')

        except ValueError:
            if token == '(':
                push(eval_stack, token)
            elif token == ')':
                while peek(eval_stack) != '(':
                    rpn_expression += (pop(eval_stack) + ' ')
                pop(eval_stack)
            elif token == '+' or token == '-' or token == '*' or token == '/' \
                    or token == '//' or token == '**':

                o1 = token
                bool1 = True
                while bool1 and (eval_stack.items[0] is not None) and \
                        (peek(eval_stack) == '+' or peek(eval_stack) == '-' or
                         peek(eval_stack) == '*' or peek(eval_stack) == '/'
                         or peek(eval_stack) == '//' or
                         peek(eval_stack) == '**'):

                    o2 = peek(eval_stack)

                    if o2 == '**' and o1 != '**':
                        rpn_expression += (pop(eval_stack) + ' ')

                    elif (o2 == '*' or o2 == '/' or o2 == '//') and \
                            (o1 == '*' or o1 == '/' or o1 == '//' or o1 == '+'
                             or o1 == '-'):
                        rpn_expression += (pop(eval_stack) + ' ')

                    elif (o2 == '+' or o2 == '-') and (o1 == '+' or o1 == '-'):
                        rpn_expression += (pop(eval_stack) + ' ')

                    else:
                        bool1 = False

                push(eval_stack, o1)

    for i in range(0, size(eval_stack)):
        rpn_expression += (pop(eval_stack) + ' ')

    rpn_expression = rpn_expression.rstrip()

    return rpn_expression
