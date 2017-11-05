from django.conf.urls import url

from drf_role.views import RoleView, PermissionView, AccessControlView, AllUrlList

urlpatterns = [
    url(r'^roles/', RoleView.as_view()),
    url(r'^permissions/', PermissionView.as_view()),
    url(r'^accesses/', AccessControlView.as_view()),
    url(r'^all-urls/', AllUrlList.as_view()),
]
