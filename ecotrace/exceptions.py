class EcoTraceError(Exception):
    pass


class TracerInitializationError(EcoTraceError):
    """Tracer is initialized twice"""
    pass


class ModelingError(EcoTraceError):
    """Operation or computation not allowed"""
    pass
