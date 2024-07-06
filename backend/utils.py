import os


def get_required_environment_variable(name: str) -> str:
    if name not in os.environ:
        raise Exception(f"The variable '{name}' was not defined and is required for the application to start")
    return os.environ.get(name)
