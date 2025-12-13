class MultiScopeError(Exception):
    """
    Base exception for all custom errors raised by the MultiScope application.

    Catching this exception allows for handling of all application-specific
    errors.
    """
    pass

class ProfileNotFoundError(MultiScopeError):
    """
    Raised when a specified game profile `.json` file cannot be found.
    """
    pass

class DependencyError(MultiScopeError):
    """
    Raised when a required external dependency (e.g., `bwrap`, `gamescope`)
    is not found on the system's PATH.
    """
    pass

class VirtualDeviceError(MultiScopeError):
    """
    Raised when there is an error creating or managing a virtual device.
    """
    pass
