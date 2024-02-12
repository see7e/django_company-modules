> # Django Project Builder
>
> This maybe in the future I'll split in a different project, but for now as it's still small I'll keep it here.
> 
> Need installed `tqdm`, run:
> 
> ```bash
> pip install tqdm
> python setup.py
> ```
> 
> It will ask for the project name and some configurations:
> 
> - Enter the name of the Django project:
> - Enter the type of database to use (postgresql/mysql/sqlite):
> - Enter the Docker image to use (python/ubuntu):


# Default Project - Modular Components

Welcome to the Default Project, a versatile enterprise solution comprising various modules designed to meet the needs of a wide range of businesses. These modules are crafted to be generic and adaptable, ensuring compatibility with diverse projects across different industries.

## Overview

This project aims to provide a foundation for building enterprise applications by offering a collection of essential modules. These modules are designed to be flexible and customizable, allowing developers to tailor them to specific business requirements without encountering legal constraints or proprietary limitations.

## Key Features

- **Modularity:** The project is structured into distinct modules, each addressing a specific aspect of enterprise functionality. This modular design promotes flexibility and scalability, enabling developers to easily add, remove, or modify modules as needed.

- **Customizability:** The modules are designed to be highly customizable, allowing developers to adjust them to suit the unique requirements of their projects. Whether it's fine-tuning configurations or extending functionality, the project provides ample flexibility for customization.

- **Interoperability:** The modules are built to seamlessly integrate with existing systems and technologies, facilitating smooth interoperability with other software components. This interoperability ensures compatibility with a wide range of platforms and frameworks, enhancing the project's versatility and usability.

## Usage

To incorporate the Default Project modules into your enterprise application, simply follow these steps:

1. **Module Selection:** Identify the modules that align with your project requirements. Choose from a diverse range of modules covering areas such as authentication, data management, reporting, and more.

2. **Integration:** Integrate the selected modules into your project by importing them into your codebase. Follow the provided documentation and guidelines to ensure smooth integration and compatibility.

3. **Customization:** Customize the modules as needed to tailor them to your project's specific needs. Adjust configurations, modify functionalities, or extend features to align with your business requirements.

4. **Testing and Deployment:** Thoroughly test the integrated modules to ensure proper functionality and compatibility. Once testing is complete, deploy your enterprise application with confidence, knowing that it's built on a solid foundation of versatile and adaptable modules.


### Deploying on Production

I need to improve the logic for the container to be able to run on production, in the moment it`s only running on development mode.

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set environment variable
ENV ENV_ROLE production

# Other Dockerfile instructions...
```

```docker-compose.yml
version: '3'
services:
    web:
        build: .
        environment:
            - ENV_ROLE=production
        # Other service configuration...
```

Also the `settings.py` file needs to be updated to fetch different configurations based on the environment role. The following checklist includes settings that:

-   [Run `manage.py check --deploy`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#run-manage-py-check-deploy)
-   [Critical settings](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#critical-settings)
    -   [`SECRET_KEY`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#secret-key)
    -   [`DEBUG`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#debug)
-   [Environment-specific settings](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#environment-specific-settings)
    -   [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#allowed-hosts)
    -   [`CACHES`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#caches)
    -   [`DATABASES`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#databases)
    -   [`EMAIL_BACKEND` and related settings](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#email-backend-and-related-settings)
    -   [`STATIC_ROOT` and `STATIC_URL`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#static-root-and-static-url)
    -   [`MEDIA_ROOT` and `MEDIA_URL`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#media-root-and-media-url)
-   [HTTPS](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#https)
    -   [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#csrf-cookie-secure)
    -   [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#session-cookie-secure)
-   [Performance optimizations](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#performance-optimizations)
    -   [Sessions](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#sessions)
    -   [`CONN_MAX_AGE`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#conn-max-age)
    -   [`TEMPLATES`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#templates)
-   [Error reporting](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#error-reporting)
    -   [`LOGGING`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#logging)
    -   [`ADMINS` and `MANAGERS`](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#admins-and-managers)
    -   [Customize the default error views](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist//#customize-the-default-error-views)


## Legal Notice

This project is provided under an open-source license, which grants users the freedom to use, modify, and distribute the code without restrictions. However, it's important to note that while the project itself is open-source, certain modules may incorporate third-party dependencies or libraries subject to their respective licenses. Users are advised to review and comply with the licensing terms of any third-party components used in conjunction with this project.

Some of the page design used here come from [**SB Admin**](https://github.com/startbootstrap/startbootstrap-sb-admin) a free, open source, MIT licensed Bootstrap admin template. 

## Contribution

Contributions to the Default Project are welcomed and encouraged! Whether it's bug fixes, feature enhancements, or documentation improvements, your contributions help enrich the project and benefit the community. To contribute, simply fork the project, make your changes, and submit a pull request. Be sure to follow the project's contribution guidelines and coding standards to ensure smooth integration of your contributions.

## Feedback

Your feedback is invaluable in shaping the future direction of the Default Project. Whether you have suggestions for improvements, encounter issues, or simply want to share your experiences, we welcome your feedback. Feel free to reach out through the project's issue tracker, discussion forums, or community channels to share your thoughts and contribute to the ongoing evolution of the project.

## Resources

- [Project Repository](https://github.com/default-project)
- [Documentation](https://docs.defaultproject.com)
- [Issue Tracker](https://github.com/default-project/issues)
- [Community Forums](https://forums.defaultproject.com)
- [License Information](https://github.com/default-project/LICENSE)

---

By adopting the Default Project and its modular components, you're not only harnessing the power of a versatile enterprise solution but also contributing to a collaborative community-driven effort aimed at empowering developers and businesses worldwide. Thank you for being a part of this journey!

---

admin admin
admin@mail.com
123 