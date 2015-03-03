
class EvenIfNone:
    """ Represents a default value that should be used 
        even if it is specified in the arguments as None """
    
    def __init__(self, defaultValue):
        """ Initialize the provider with the default value """
        self.defaultValue = defaultValue
        
    def shouldProvide(self, argument, args, kwargs):
        """ Return if the Value Provider should be used """
        return argument.isProvided(args, kwargs) and argument.getValue(args, kwargs) is None
        
    def getValue(self, *args, **kwargs):
        """ Return the value for this default """
        return self.defaultValue