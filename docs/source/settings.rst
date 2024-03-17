========
Settings
========

Fimbu is configured the same way as django, there is a settings.py file where you define certain behaviors such as debugging mode and templates and static files.

Here we will cover the basic settings, and each will refer to its own settings.

**BASE_DIR**
    The base directory of the project.

**SECRET**
    The secret key used for security functions (be sure not to share it publicly).

**DEBUG**
    A flag specifying whether debug mode is enabled or not. It's recommended to disable it in production.

**INSTALLED_APPS**
    The list of applications installed in the project.

**MIDDLEWARE**
    The list of middlewares used in the project.

**MIDDLEWARE_FROM_FACTORY_BEFORE**
    If this setting is True, Fimbu will first load middlewares defined on the application; otherwise, it will first load middlewares from the settings.

**PLUGINS**
    The list of plugins used in the project.

**ASGI_APPLICATION**
    The ASGI application used for the project.
