"""Helper code for Computing 5 Exercise 11

Sam Scott, McMaster University, 2025"""

def digit_convert(d):
    """Given integer d in the range 0 to 35, outputs a string digit
    representation, where 10 = A, 11 = B, etc. If the digit is out
    of range, returns "*" """

    # simple digits
    if d >= 0 and d < 10:
        return str(d)

    # letter digits
    elif d >= 10 and d < 36:
        return chr(d+55)

    # bad digit value
    else:
        return "*"