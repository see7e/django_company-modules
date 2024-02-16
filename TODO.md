# TODO

- [ ] improve database suport
- [x] split the databases depending on the usage (users, etc)
- [x] fix `DATABASES` information settings at `settings.py` file
- [ ] improve user experience
- [ ] improve runtime of virtural environment creation
- [ ] run `python.exe -m pip install --upgrade pip`
- [ ] add instalation of `django` and `docutils` after virtual environment creation and activation
- [x] create a `requirements.txt` file (`python -m pip freeze > requirements.txt`)
- [ ] implement development and production environment logic
- [x] fix `ROOT_URLCONF` pointing to the wrong file (replace the name of the app for "settings")
- [ ] fix the abomination for the db configuration at `setup.py` file
    ```python
    with open(settings_path, "w") as f:
        for line in lines:
            if line.strip().startswith("'ENGINE'"):
                f.write(f"        'ENGINE': 'django.db.backends.{database_type}',\n")
            elif line.strip().startswith("'NAME'"):
                f.write(f"        'NAME': 'mydatabase',\n")
            elif line.strip().startswith("'USER'"):
                if database_type == "sqlite":
                    f.write(f"        'USER': '',\n")
                else:
                    f.write(f"        'USER': 'postgres',\n")
            elif line.strip().startswith("'PASSWORD'"):
                if database_type == "sqlite":
                    f.write(f"        'PASSWORD': '',\n")
                else:
                    f.write(f"        'PASSWORD': '{db_password}',\n")
            elif line.strip().startswith("'HOST'"):
                if database_type == "sqlite":
                    f.write(f"        'HOST': '',\n")
                else:
                    f.write(f"        'HOST': 'localhost',\n")
            elif line.strip().startswith("'PORT'"):
                if database_type == "sqlite":
                    f.write(f"        'PORT': '',\n")
                else:
                    f.write(f"        'PORT': '',\n")
            else:
                f.write(line)
    ```
- [x] fix `<class 'register_login.admin.TeamAdmin'>`: (admin.E019) The value of `filter_horizontal[0]` refers to `permissions`, which is not a field of `register_login.Team`.
- [x] fix  `register_login.User.position`: (fields.E303) Reverse query name for `register_login.User.position` clashes with field name `register_login.Team.user`.
    >    Renamed `User` to `CustomUser` to avoid clash with the django default user model
- [ ] run `migrate` and add django superuser creation option at the end of the setup
- [x] **auth.Group.permissions**: (fields.E304) Reverse accessor `Permission.group_set` for `auth.Group.permissions` clashes with reverse accessor for `register_login.Group.permissions`. **register_login.Group.permissions**: (fields.E304) Reverse accessor `Permission.group_set` for `register_login.Group.permissions` clashes with reverse accessor for `auth.Group.permissions`.
    >    divided the logic between the `auth.models.Group` and the `register_login.models.SubGroup` avoiding clashing when trying to override the default model  
- [ ] implement `permission_required` decorator[#](https://docs.djangoproject.com/en/5.0/topics/auth/default//#the-permission-required-decorator "Permalink to this headline") to access the views
- [ ] `register_login.html`: move styles to css file
- [x] `register_login.html`: reduce some of the nestings
- [x] `register_login.html`: replace form with forms.py code
- [ ] `styles.css`: remove the unused classes in file
- [x] implement the update of the menus in the `sidenav` by `@update_sidenav` decorator
- [ ] impement pages pf user profile menu
- [ ] create project board
- [ ] 