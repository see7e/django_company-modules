import os
import sys
import time
import hashlib
import subprocess
from tqdm import tqdm

# ANSI escape codes for text color and formatting
class color:
    HEADER = "\033[95m"
    GRAY = "\033[90m"
    ENDC = "\033[0m"


def create_virtual_environment():
    print(color.GRAY + "Creating a virtual environment..." + color.ENDC)
    # Create a new tqdm instance for the virtual environment creation progress
    with tqdm(
        total=4, desc="Virtual Environment", bar_format="{l_bar}{bar}", ncols=60
    ) as pbar:
        try:
            # Create a virtual environment
            subprocess.run(["python", "-m", "venv", ".venv"], check=True)
        except subprocess.CalledProcessError as e:
            print(
                color.GRAY
                + f"Error: Failed to create virtual environment: {e}"
                + color.ENDC
            )
            return
        pbar.update(1)  # Update progress bar

        # Activate the virtual environment
        if sys.platform.startswith("win"):
            activate_script = os.path.join(".venv", "Scripts", "activate.bat")
        else:
            activate_script = os.path.join(".venv", "bin", "activate")
        subprocess.run([activate_script])
        pbar.update(1)  # Update progress bar

        # Install Django
        subprocess.run(["pip", "install", "django"])
        pbar.update(1)  # Update progress bar

        # Install tqdm
        subprocess.run(["pip", "install", "tqdm"])
        pbar.update(1)  # Update progress bar


def create_django_project():
    # Ask for the name of the Django project
    project_name = input(
        color.GRAY + "Enter the name of the Django project: " + color.ENDC
    )

    # Ask about the type of database to use
    database_type = input(
        color.GRAY
        + "Enter the type of database to use (postgresql/mysql/sqlite3): "
        + color.ENDC
    )

    # Ask about the Docker image to use
    docker_image = input(
        color.GRAY + "Enter the Docker image to use (python/ubuntu): " + color.ENDC
    )

    print(color.GRAY + "Creating a new directory for the project..." + color.ENDC)
    time.sleep(0.5)
    # Create a new directory for the project
    os.makedirs(project_name)

    print(color.GRAY + "Changing to the project directory..." + color.ENDC)
    time.sleep(0.5)
    # Change to the project directory
    os.chdir(project_name)

    # Call the function to create the virtual environment
    create_virtual_environment()

    print(color.GRAY + "Creating a new Django project..." + color.ENDC)
    time.sleep(0.5)
    # Create a new Django project in the project directory
    with tqdm(
        total=1, desc="Django Project Creation", bar_format="{l_bar}{bar}", ncols=60
    ) as pbar:
        subprocess.run(["django-admin", "startproject", project_name, "."])
        pbar.update(1)  # Update progress bar

    # Move the settings directory to 'settings'
    os.rename(project_name, "settings")

    # Generate a random password for the database
    db_password = hashlib.sha384(os.urandom(32)).hexdigest()

    # Replace the database configuration in settings.py
    settings_path = os.path.join("settings", "settings.py")
    with open(settings_path, "r") as f:
        lines = f.readlines()
    with open(settings_path, "w") as f:
        for line in lines:
            if line.strip().startswith("'ENGINE'"):
                f.write(f"        'ENGINE': 'django.db.backends.{database_type}',\n")
            elif line.strip().startswith("'NAME'"):
                f.write(f"        'NAME': 'mydatabase',\n")
            elif line.strip().startswith("'USER'"):
                if database_type == "sqlite3":
                    f.write(f"        'USER': '',\n")
                else:
                    f.write(f"        'USER': 'postgres',\n")
            elif line.strip().startswith("'PASSWORD'"):
                if database_type == "sqlite3":
                    f.write(f"        'PASSWORD': '',\n")
                else:
                    f.write(f"        'PASSWORD': '{db_password}',\n")
            elif line.strip().startswith("'HOST'"):
                if database_type == "sqlite3":
                    f.write(f"        'HOST': '',\n")
                else:
                    f.write(f"        'HOST': 'localhost',\n")
            elif line.strip().startswith("'PORT'"):
                if database_type == "sqlite3":
                    f.write(f"        'PORT': '',\n")
                else:
                    f.write(f"        'PORT': '',\n")
            else:
                f.write(line)

    print(color.GRAY + "Creating a Dockerfile..." + color.ENDC)
    time.sleep(0.5)
    # Create a Dockerfile
    with tqdm(
        total=1, desc="Dockerfile Creation", bar_format="{l_bar}{bar}", ncols=60
    ) as pbar:
        dockerfile_content = f'FROM {docker_image}:latest\n\n\
            WORKDIR /app\n\n\
            COPY . .\n\n\
            RUN pip install -r requirements.txt\n\n\
            CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]'

        with open("Dockerfile", "w") as dockerfile:
            dockerfile.write(dockerfile_content)
        pbar.update(1)  # Update progress bar

    print(color.GRAY + "Creating a docker-compose.yml file..." + color.ENDC)
    time.sleep(0.5)
    # Create a docker-compose.yml file
    with tqdm(
        total=1, desc="docker-compose.yml Creation", bar_format="{l_bar}{bar}", ncols=60
    ) as pbar:
        database_service = ""
        if database_type == "postgresql":
            database_service = "\
        db:\n\
            image: postgres\n\
            environment:\n\
                POSTGRES_USER: postgres\n\
                POSTGRES_PASSWORD: postgres\n\
                POSTGRES_DB: mydatabase"

        elif database_type == "mysql":
            database_service = "\
        db:\n\
            image: mysql\n\
            environment:\n\
                MYSQL_ROOT_PASSWORD: root\n\
                MYSQL_DATABASE: mydatabase\n\
        "
        elif database_type == "sqlite3":
            database_service = "\
        db:\n\
            image: sqlite"

        docker_compose_content = f"\
        version: '3'\n\n\
        services:\n\
            web:\n\
                build: .\n\
                ports:\n\
                    - \"8000:8000\"\n\
            {database_service}"

        with open("docker-compose.yml", "w") as docker_compose:
            docker_compose.write(docker_compose_content)
        pbar.update(1)  # Update progress bar

    print(
        color.GRAY
        + f"Successfully created Django project '{project_name}' with Docker support and {database_type} database."
        + color.ENDC
    )


####################################################################################################
# def dev_run(port=8000):
#     subprocess.run(['../manage.py', 'runserver', port])

# def dev_login(superuser: dict):
#     subprocess.run(['../manage.py', 'login',
#         '--username', superuser.email,
#         '--password', superuser.password
#     ])
####################################################################################################

if __name__ == "__main__":
    # ASCII art animation for progress visualization
    print("Creating Django project:")
    for frame in tqdm(
        [
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
            "███▒▒▒▒▒▒▒",
        ],
        desc="Building:",
        bar_format="{l_bar}{bar}",
        ncols=60,
    ):
        time.sleep(0.01)
    create_django_project()
