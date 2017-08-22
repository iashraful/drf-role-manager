# Note to use this package


1. Add this into project urls.py or equivalent file `url(r'^api/drf-role/', include('drf_role.urls')),`
2. Create new model name Profile. Like below,

```python
    class Profile(models.Model):
        user = models.OneToOneField(User)
        role = models.ForeignKey(Role)
        # You may add anything you need
        ... ... ... ... ... ...
```
3. Run this command `python manage.py init_data`
4. Add this to settings,
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'drf_role.permissions.BaseRolePermission',
    )
}
```
OR add `permission_classes=(BaseRolePermission,)` in your every view. (Where you need)