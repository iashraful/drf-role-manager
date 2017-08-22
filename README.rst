================================
DjangoRESTFramework Role Manager
================================
drf_role is a small, simple and lightweight role manager who can manage READ/WRITE & NoAccess permissions
for each role. It basically work with DRF internal system like permission class, object level permission, etc.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'drf_role',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^api/<YOUR VERSION NUMBER>/drf-role/', include('drf_role.urls')),

3. Run `python manage.py migrate` to create the drf_role models.

4. Start the development server and visit,
    http://127.0.0.1:8000/api/<VERSION>/roles/
    http://127.0.0.1:8000/api/<VERSION>/permissions/
    http://127.0.0.1:8000/api/<VERSION>/accesses/
    http://127.0.0.1:8000/api/<VERSION>/all-urls/

Please look up on docs for details...
