
class SmartDefault:
    """ Represents a smart default argument """
        
    def __init__(self, argument, provider):
        """ Set the default's metadata """
        self.argument = argument #SmartArg(argName, metadata)
        self.provider = provider
        # self.metadata = metadata
        
    def shouldUseDefault(self, args, kwargs):
        """ Return if the default value should be used """
        return not self.argument.isProvided(args, kwargs) or self.provider.shouldProvide(self.argument, args, kwargs)
        
    def setDefault(self, args, kwargs):
        """ Return get the default value for the argument """
        self.argument.setValue(args, kwargs, self.provider.getValue(self.argument, *args, **kwargs))