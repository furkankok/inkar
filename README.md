
# Django Decorators

This Python package provides a collection of decorators for Django views to streamline handling of request types and parameters.

## Installation

You can install the package using pip:

```shell
pip install django-validate-decorators
```

## Usage

Import the desired decorators from the package and apply them to your view functions:

```python
from django.http import HttpResponse
from inkar.decorators import pass_only_get, pass_json_body

@pass_only_get
def my_view(request, name: str, age: int):
    # Your view logic
    # Use name and age here
    return HttpResponse('Hello World.')
```

## Features

- `pass_only_get`: Ensures that the view only processes GET requests.
- `pass_only_post`: Ensures that the view only processes POST requests.
- `pass_only_post_and_get`: Ensures that the view only processes POST and GET requests.
- `pass_json_body`: Parses and validates JSON request bodies.

## Config

You can pass parameters to check types and values of request parameters. The following parameters are available:

- `check_type=False`: Checks parameters type, if set True. (Default: False), it throws `TypeError` if the type is not matched.
- `check_value=HttpResponse`: Checks parameters type if set HttpResponse. It throws `HttpResponse` if the value is not matched.
- `check_value=Exception`: You can customize your own exception class. It throws your exception if the value is not matched.


## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
