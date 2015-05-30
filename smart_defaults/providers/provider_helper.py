
def HasProviderInterface(value):
    """ Return if the default value has the provider interface """
    return hasattr(value, "shouldProvide") and hasattr(value, "getValue")