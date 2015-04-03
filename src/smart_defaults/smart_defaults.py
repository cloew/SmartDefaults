from .function_metadata import FunctionMetadata
from .smart_default import SmartDefault
from .providers.provider_helper import HasProviderInterface

def smart_defaults(fn):
    """ Set the function to use Smart Defaults """
    metadata = FunctionMetadata(fn)
    defaults = [SmartDefault(metadata.nameToArg[arg], metadata.nameToDefaultValue[arg]) for arg in metadata.nameToDefaultValue if HasProviderInterface(metadata.nameToDefaultValue[arg])]
    def setKwargs(*args, **kwargs):
        args = list(args)
        for default in defaults:
            if default.shouldUseDefault(args, kwargs):
                default.setDefault(args, kwargs)
        return fn(*args, **kwargs)
    return setKwargs