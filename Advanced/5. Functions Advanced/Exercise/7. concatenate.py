def concatenate(*args, string = ''):
    if args == ():
        return string

    return args[0] + concatenate(*args[1:])

