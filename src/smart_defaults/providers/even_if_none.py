from .provider_helper import HasProviderInterface

class EvenIfNone:
    """ Represents a default value that should be used 
        even if it is specified in the arguments as None """
    
    def __init__(self, defaultOrProvider):
        """ Initialize the provider with the default value """
        self.defaultValue = None
        self.provider = None
        if HasProviderInterface(defaultOrProvider):
            self.provider = defaultOrProvider
        else:
            self.defaultValue = defaultOrProvider
        
    def shouldProvide(self, argument, args, kwargs):
        """ Return if the Provider should be used """
        return argument.providedAs(args, kwargs, None) or (self.provider and self.provider.shouldProvide(argument, args, kwargs))
        
    def getValue(self, *args, **kwargs):
        """ Return the value for this default """
        return self.defaultValue if self.defaultValue else self.provider.getValue(*args, **kwargs)