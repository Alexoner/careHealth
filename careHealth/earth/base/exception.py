class EnvVarException(Exception):
    pass


class ProjectNameNotSet(EnvVarException):
    pass


class ProjectNameInvalid(EnvVarException):
    pass


class ProjectEnvNotSet(EnvVarException):
    pass


class ProjectEnvInvalid(EnvVarException):
    pass
