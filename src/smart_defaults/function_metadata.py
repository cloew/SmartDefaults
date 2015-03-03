import inspect

class FunctionMetadata:
    """ Represents a functions metadata """
    
    def __init__(self, func):
        """ Initialize the metadata """
        args, varargs, keywords, defaults = inspect.getargspec(func)
        self.defaults = dict(zip(reversed(args), reversed(defaults)))
        self.argToIndex = {arg:args.index(arg) for arg in args}