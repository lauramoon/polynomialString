def get_polynomial_string(coeffs:list) -> str:
    """
    turns a list of integer coefficients for a one-dimensional polynomial
    into a nice-looking string representing the polynomial
    :param coeffs: list of coefficients
    :return: string displaying the polynomial with variable x
    """

    # remove any leading '0' coefficients
    while len(coeffs) >= 1 and (coeffs[0] == 0 or coeffs[0] is None):
        coeffs = coeffs[1:]

    # check that coefficients other than 0 were provided
    if not coeffs:
        return "0"

    # the string to return
    pretty_string = ""

    # highest exponent
    order = len(coeffs) - 1

    for i in range(0, len(coeffs)):
        # exponent
        exp = order - i
        # coefficient
        cof = coeffs[i]

        # check for 0 or None coefficient
        if cof == 0 or cof is None:
            continue

        # create string for sign and coefficient
        if i == 0:
            # first term is simple
            cof_str = str(cof)
        else:
            # later terms differ depending if coefficient is positive or negative
            cof_str = f" + {str(cof)}" if cof > 0 else f" - {str(-cof)}"

        # coefficients of 1 are different, unless at the end
        if cof_str[-1] == "1" and exp != 0:
            # drop the 1
            cof_str = cof_str[:-1]
            # no parentheses
            term_str = f"{cof_str}x^{exp}" if exp >= 2 else f"{cof_str}x"

        else:
            if exp >= 2:
                term_str = f"{cof_str}(x^{exp})"
            elif exp == 1:
                term_str = f"{cof_str}x"
            else:
                term_str = cof_str

        pretty_string += term_str

    return pretty_string
