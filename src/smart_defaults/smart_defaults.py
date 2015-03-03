from function_metadata import FunctionMetadata
from smart_default import SmartDefault

def HasProviderInterface(value):
    """ Return if the default value has the provider interface """
    return hasattr(value, "shouldProvide") and hasattr(value, "getValue")

def smart_defaults(fn):
    """ Set the function to use Smart Defaults """
    metadata = FunctionMetadata(fn)
    defaults = [SmartDefault(arg, metadata.defaults[arg], metadata) for arg in metadata.defaults if HasProviderInterface(metadata.defaults[arg])]
    def setKwargs(*args, **kwargs):
        args = list(args)
        for default in defaults:
            if default.shouldUseDefault(args, kwargs):
                default.setDefault(args, kwargs)
        return fn(*args, **kwargs)
    return setKwargs