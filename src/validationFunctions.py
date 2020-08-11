def checkIfVarIsType(var, type_, *args):
    if type(var) != type_:
        raise TypeError(f"{var} is not a {type_}")

def checkVarAgainstMultipleTypes(var, *args):
    if len(args) == 0:
        raise KeyError("Expected atleast one type to compare variable to, but none was given")

    no_match = False
    for arg in args:
        if type(var) == arg:
            break
    else:
        raise TypeError(f"{var} did not match any from {args}")