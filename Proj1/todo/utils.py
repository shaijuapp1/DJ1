import types

def safe_exec(code, globals_dict=None, locals_dict=None):
    allowed_builtins = {
        'print': print,
        'len': len,
        'range': range,
        'min': min,
        'max': max,
        'sum': sum,
        # Add other safe built-ins as needed
    }

    if globals_dict is None:
        globals_dict = {}
    if locals_dict is None:
        locals_dict = {}

    globals_dict['__builtins__'] = allowed_builtins

    exec(code, globals_dict, locals_dict)
    return globals_dict, locals_dict
