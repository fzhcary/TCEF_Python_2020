# The following is using decorator for who is interested.
# but you don't need understand it. 
level = 0
def trace(f):
    def g(*args):
        global level
        # pretty print indicating the level
        prefix = "|  " * level + "|--"
        strargs = ", ".join(repr(a) for a in args)
        print("{} {}({})".format(prefix, f.__name__, strargs))
        # increment the level before calling the function
        # and decrement it after the call
        level += 1
        result = f(*args)
        level -= 1
        return result
    return g
