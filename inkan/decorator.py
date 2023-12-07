import inspect
import json
from functools import wraps
from typing import Any

from django.http import HttpResponse


def convertable_types(val, to):
    try:
        to(val)
        return True
    except:
        return False


def pass_only_get(*args: Any, **kwargs: Any) -> Any:
    def main_dec(func, check_type = False):
        @wraps(func)
        def wrapper_decorator(request, *args, **kwargs):
            specs = inspect.signature(func)
            for name, param in specs.parameters.items():
                if name == "request": continue

                param_type = param.annotation
                has_default = param.default != inspect.Parameter.empty
                parameter = request.GET.get(name, param.default if has_default else None)
                if param_type != inspect.Parameter.empty:
                    if param_type == type(parameter) or convertable_types(parameter, param_type):
                        kwargs[name] = parameter
                    else:
                        if check_type:
                            if isinstance(check_type, HttpResponse):
                                return check_type
                            elif isinstance(check_type, Exception):
                                raise check_type
                            raise TypeError(f"parameter {name} should be {param_type}, not {type(parameter)}")
                        kwargs[name] = parameter
                else:
                    kwargs[name] = parameter
            value = func(request, *args, **kwargs)
            return value
        return wrapper_decorator

    if args and callable(args[0]):
        return main_dec(args[0])

    def decorator(func):
        return main_dec(func, *args, **kwargs)
    return decorator


def pass_only_post(*args: Any, **kwargs: Any) -> Any:
    def main_dec(func, check_type = False):
        @wraps(func)
        def wrapper_decorator(request, *args, **kwargs):
            specs = inspect.signature(func)
            for name, param in specs.parameters.items():
                if name == "request": continue

                param_type = param.annotation
                has_default = param.default != inspect.Parameter.empty
                parameter = request.POST.get(name, param.default if has_default else None)
                if param_type != inspect.Parameter.empty:
                    if param_type == type(parameter) or convertable_types(parameter, param_type):
                        kwargs[name] = parameter
                    else:
                        if check_type:
                            if isinstance(check_type, HttpResponse):
                                return check_type
                            elif isinstance(check_type, Exception):
                                raise check_type
                            raise TypeError(f"parameter {name} should be {param_type}, not {type(parameter)}")
                        kwargs[name] = parameter
                else:
                    kwargs[name] = parameter
            value = func(request, *args, **kwargs)
            return value
        return wrapper_decorator

    if args and callable(args[0]):
        return main_dec(args[0])

    def decorator(func):
        return main_dec(func, *args, **kwargs)
    return decorator



def pass_only_post_and_get(*args: Any, **kwargs: Any) -> Any:
    def main_dec(func, check_type = False):
        @wraps(func)
        def wrapper_decorator(request, *args, **kwargs):
            specs = inspect.signature(func)
            for name, param in specs.parameters.items():
                if name == "request": continue

                param_type = param.annotation
                has_default = param.default != inspect.Parameter.empty
                parameter = request.POST.get(name, request.GET.get(name, param.default if has_default else None))
                if param_type != inspect.Parameter.empty:
                    if param_type == type(parameter) or convertable_types(parameter, param_type):
                        kwargs[name] = parameter
                    else:
                        if check_type:
                            if isinstance(check_type, HttpResponse):
                                return check_type
                            elif isinstance(check_type, Exception):
                                raise check_type
                            raise TypeError(f"parameter {name} should be {param_type}, not {type(parameter)}")
                        kwargs[name] = parameter
                else:
                    kwargs[name] = parameter
            value = func(request, *args, **kwargs)
            return value
        return wrapper_decorator

    if args and callable(args[0]):
        return main_dec(args[0])

    def decorator(func):
        return main_dec(func, *args, **kwargs)
    return decorator


def pass_json_body(*args: Any, **kwargs: Any) -> Any:
    def main_dec(func, check_type = False):
        @wraps(func)
        def wrapper_decorator(request, *args, **kwargs):
            specs = inspect.signature(func)
            try:
                json_body = json.loads(request.body)
            except:
                json_body = {}

            for name, param in specs.parameters.items():
                if name == "request": continue

                param_type = param.annotation
                has_default = param.default != inspect.Parameter.empty
                parameter = json_body.get(name, param.default if has_default else None)
                if param_type != inspect.Parameter.empty:
                    if param_type == type(parameter) or convertable_types(parameter, param_type):
                        kwargs[name] = parameter
                    else:
                        if check_type:
                            if isinstance(check_type, HttpResponse):
                                return check_type
                            elif isinstance(check_type, Exception):
                                raise check_type
                            raise TypeError(f"parameter {name} should be {param_type}, not {type(parameter)}")
                        kwargs[name] = parameter
                else:
                    kwargs[name] = parameter
            value = func(request, *args, **kwargs)
            return value
        return wrapper_decorator

    if args and callable(args[0]):
        return main_dec(args[0])

    def decorator(func):
        return main_dec(func, *args, **kwargs)
    return decorator

