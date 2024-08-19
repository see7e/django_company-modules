from django.shortcuts import render
from django.http import JsonResponse
from core.models import CustomUser
from core.db import create_warehouse_tables, create_menu_data

####################################################################################################
import subprocess
from warehouse.models import Shed, Rack, Item
import os

# creates some initial data for the database, so you can see how the application works
#    without having to create a bunch of data yourself. It's a good idea to remove this file from the
#    project before deploying it to a production server.


def dev_fill_tables(request):
    """ Creates filler data for project visualization """
    all_data = {}
    message = ""
    manager_user, created = CustomUser.objects.get_or_create(
        email="admin@mail.com",
        first_name="Admin",
        last_name="Admin",
        is_superuser=True,
        is_staff=True,
        is_active=True,
    )

    all_data = {}
    message = ""
    all_data["register_login"] = create_menu_data(manager=manager_user)
    # create Data (
    #   register_login{CustomUser, CustomGroup, CustomSubGroup, Menu,
    #   warehouse{Shed, Rack, Item,},
    all_data["warehouse"] = create_warehouse_tables()
    #   hr{},
    #   reports{}
    #   sales{},
    #   purchases{},
    # )

    for key in all_data:
        message += (
            f"{key} - {len(all_data[key])} objects created\n"
            if len(all_data[key]) > 0
            else f"{key} - No objects created\n"
        )
    status = "success" if not "No objects created" in message else "error"

    return JsonResponse({"status": status, "message": message})


####################################################################################################
# def dev_login(superuser: dict):
#     subprocess.run(
#         [
#             "../manage.py",
#             "login",
#             "--username",
#             superuser.email,
#             "--password",
#             superuser.password,
#         ]
#     )
####################################################################################################
