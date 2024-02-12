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
        print("Updating sidenav")

        # Fetch managed teams and subteams
        managed_teams = request.user.managed_teams.all()
        managed_subteams = request.user.managed_subteams.all()

        # Combine queries using Q objects for optimization
        menu_data = (
            Menu.objects
            .filter(Q(team__in=managed_teams) | Q(subteam__in=managed_subteams))
            .values('id', 'menu', 'submenu', 'url')
            .distinct()
        )

        # Convert the queryset into a list of dictionaries
        data = list(menu_data)

        # Create a dictionary to store the data grouped by menu
        grouped_data = defaultdict(list)

        # Group items by menu
        for item in data:
            menu = item['menu']
            grouped_data[menu].append({'id': item['id'], 'submenu': item['submenu'], 'url': item['url']})

        # Convert the dictionary back to a list of dictionaries
        result_list = [{'menu': menu, 'submenus': submenus} for menu, submenus in grouped_data.items()]

        # Store the data in the session
        request.session['user_menu'] = result_list

        return func(request, *args, **kwargs)
    return wrapper
