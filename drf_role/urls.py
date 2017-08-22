from django.conf.urls import url

from drf_role.views import RoleView, PermissionView, AccessControlView, AllUrlList

urlpatterns = [
    url(r'^roles/', RoleView.as_view(), name='role-view'),
    url(r'^permissions/', PermissionView.as_view(), name='permission-view'),
    url(r'^accesses/', AccessControlView.as_view(), name='access-control-view'),
    url(r'^all-urls/', AllUrlList.as_view(), name='url-list'),
]
