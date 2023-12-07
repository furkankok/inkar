
from django.http import HttpResponse
from inkan.decorator import pass_only_get

@pass_only_get
def my_view(request, name):
    # This view get name parameter from url.
    # If there is not name in url, name will be None.

    # save_db(name)

    return HttpResponse('OK')

@pass_only_get(check_type = True)
def my_view(request, name):
    # This view get name parameter from url.
    # If there is not name in url, it thorws TypeError.

    # save_db(name)

    return HttpResponse('OK')

@pass_only_get(check_type = HttpResponse('Not Found'))
def my_view(request, name):
    # This view get name parameter from url.
    # If there is not name in url, it returns HttpResponse('Not Found').

    # save_db(name)

    return HttpResponse('OK')

@pass_only_get(check_type = Exception('Not Found'))
def my_view(request, name):
    # This view get name parameter from url.
    # If there is not name in url, it throws Exception('Not Found').

    # save_db(name)

    return HttpResponse('OK')

@pass_only_get
def my_view(request, name: str):
    # This view get name parameter from url.
    # Trying to convert name to str.

    # save_db(name)

    return HttpResponse('OK')

@pass_only_get(check_type = True)
def my_view(request, name: str):
    # This view get name parameter from url.
    # Trying to convert name to str.
    # If it fails, it thorws TypeError.

    # save_db(name)

    return HttpResponse('OK')

@pass_only_get
def my_view(request, name: str = "myname"):
    # This view get name parameter from url.
    # Trying to convert name to str.
    # If there is not name in url, name will be "myname".

    # save_db(name)

    return HttpResponse('OK')

# This examples are also valid for all decorators.