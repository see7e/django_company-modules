# TODO

> next steps to be done

- [ ] attach the event middleware to the functions
- [ ] create and set workflow to read from `core.models.Event`

---

- [ ] study and configure `pre-commit` to run `black` and `flake8` before commiting (`.git\modules\django_company-modules\hooks\pre-commit`)
- [ ] improve database suport
- [ ] improve user experience
- [ ] improve runtime of virtural environment creation
- [ ] run `python.exe -m pip install --upgrade pip`
- [ ] add instalation of `django` and `docutils` after virtual environment creation and activation
- [ ] implement development and production environment logic
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
- [ ] run `migrate` and add django superuser creation option at the end of the setup
    >    divided the logic between the `auth.models.Group` and the `register_login.models.SubGroup` avoiding clashing when trying to override the default model
- [ ] implement `permission_required` decorator[#](https://docs.djangoproject.com/en/5.0/topics/auth/default//#the-permission-required-decorator "Permalink to this headline") to access the views
- [ ] `register_login.html`: move styles to css file
- [ ] `core/css/styles.css`: remove the unused classes in file
- [ ] impement pages pf user profile menu
- [ ] create project board
- [ ] Also the `settings.py` file needs to be updated to fetch different configurations based on the environment role. The following checklist includes settings that:
    > -   [Run `manage.py check --deploy`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#run-manage-py-check-deploy)
    > -   [Critical settings](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#critical-settings)
    >     -   [`SECRET_KEY`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#secret-key)
    >     -   [`DEBUG`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#debug)
    > -   [Environment-specific settings](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#environment-specific-settings)
    >     -   [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#allowed-hosts)
    >     -   [`CACHES`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#caches)
    >     -   [`DATABASES`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#databases)
    >     -   [`EMAIL_BACKEND` and related settings](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#email-backend-and-related-settings)
    >     -   [`STATIC_ROOT` and `STATIC_URL`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#static-root-and-static-url)
    >     -   [`MEDIA_ROOT` and `MEDIA_URL`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#media-root-and-media-url)
    > -   [HTTPS](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#https)
    >     -   [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#csrf-cookie-secure)
    >     -   [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#session-cookie-secure)
    > -   [Performance optimizations](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#performance-optimizations)
    >     -   [Sessions](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#sessions)
    >     -   [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#conn-max-age)
    >     -   [`TEMPLATES`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#templates)
    > -   [Error reporting](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#error-reporting)
    >     -   [`LOGGING`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#logging)
    >     -   [`ADMINS` and `MANAGERS`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#admins-and-managers)
    >     -   [Customize the default error views](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#customize-the-default-error-views)
- [ ] install and configure `ansible` to automate the deployment of the project


## DONE

- [x] split the databases depending on the usage (users, etc)
- [x] fix `DATABASES` information settings at `settings.py` file
- [x] create a `requirements.txt` file (`python -m pip freeze > requirements.txt`)
- [x] fix `ROOT_URLCONF` pointing to the wrong file (replace the name of the app for "settings")
- [x] `register_login.html`: reduce some of the nestings
- [x] `register_login.html`: replace form with forms.py code
- [x] implement the update of the menus in the `sidenav` by `@update_sidenav` decorator
- [x] fix `<class 'register_login.admin.TeamAdmin'>`: (admin.E019) The value of `filter_horizontal[0]` refers to `permissions`, which is not a field of `register_login.Team`.
- [x] fix  `register_login.User.position`: (fields.E303) Reverse query name for `register_login.User.position` clashes with field name `register_login.Team.user`.
- [x] **auth.Group.permissions**: (fields.E304) Reverse accessor `Permission.group_set` for `auth.Group.permissions` clashes with reverse accessor for `register_login.Group.permissions`. **register_login.Group.permissions**: (fields.E304) Reverse accessor `Permission.group_set` for `register_login.Group.permissions` clashes with reverse accessor for `auth.Group.permissions`.
    >    Renamed `User` to `CustomUser` to avoid clash with the django default user model
- [x] new order forms and page list display
- [x] setup `redis-server` (`django-select2` depends on it)
