
class SmartArg:
    """ Helper class to handle interacting with a particular argument """
    
    def __init__(self, argName, funcMetadata):
        """ Initialize the smart argument with its name and the metadata of the function """
        self.argName = argName
        self.inlineIndex = funcMetadata.argToIndex[self.argName]
        
    def isProvided(self, args, kwargs):
        """ Return if this argument has been specified in the given arguments """
        return self.argName in kwargs or len(args) > self.inlineIndex
        
    def getValue(self, args, kwargs):
        """ Return the argument value """
        if len(args) > self.inlineIndex:
            return args[self.inlineIndex]
        else:
            return kwargs[self.argName]
        
    def setValue(self, args, kwargs, newValue):
        """ Set the argument to the specified value """
        if len(args) > self.inlineIndex:
            args[self.inlineIndex] = newValue
        else:
            kwargs[self.argName] = newValue