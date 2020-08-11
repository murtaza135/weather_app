def checkIfVarIsType(var, type_):
    if type(var) != type_:
        raise TypeError(f"{var} is not a {type_}")