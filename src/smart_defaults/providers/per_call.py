import copy

class PerCall:
    """ Returns a copy of the default value from the function defaults """
    
    def __init__(self, defaultValue):
        """ Initialize the provider with the default value """
        self.defaultValue = defaultValue
        
    def shouldProvide(self, argument, args, kwargs):
        """ Return if the Provider should be used """
        return False
        
    def getValue(self, *args, **kwargs):
        """ Return the value for this default """
        return copy.deepcopy(self.defaultValue)