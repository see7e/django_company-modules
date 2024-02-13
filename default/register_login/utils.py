import time

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()

        print(f"Function {func.__name__} took {end - start} seconds to run")
        return value
    return wrapper


from functools import wraps
from collections import defaultdict
from django.shortcuts import render
from django.db.models import Q
from .models import Menu, CustomUser

def update_sidenav(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        print("Updating sidenav menus...")

        # Query for the side menu
        menu_data = (
            Menu.objects
            # .filter(Q(group__in=request.user.groups.all()) | Q(subgroup=request.user.subgroup))
            .filter(group__in=request.user.groups.all())
            .values('id', 'menu', 'submenu', 'url', 'icon', 'group', 'subgroup')
            .distinct()
        )

        # Convert the queryset into a list of dictionaries
        data = list(menu_data)

        # Create a dictionary to store the data grouped by menu
        grouped_data = defaultdict(list)

        # Group items by menu
        for item in data:
            menu = item['menu']
            grouped_data[menu].append({
                'id': item['id'],
                'submenu': item['submenu'],
                'icon': item['icon'],
                'url': item['url'],
                'group': item['group'],
                'subgroup': item['subgroup']
            })

        # Convert the dictionary back to a list of dictionaries
        result_list = [{'menu': menu, 'items': items} for menu, items in grouped_data.items()]

        # Store the data in the session
        request.session['menu_data'] = result_list

        return func(request, *args, **kwargs)
    return wrapper
