
class ViaField:
    """ Returns a value from a field on the first argument (typically self) """
    
    def __init__(self, fieldName):
        """ Initialize the Value Provider """
        self.fieldName = fieldName
        
    def shouldProvide(self, argument, args, kwargs):
        """ Return if the Value Provider should be used """
        return False
        
    def getValue(self, obj, *args, **kwargs):
        """ Return the value for this default """
        return getattr(obj, self.fieldName)