from django.urls import path

from role_test_app.views import ProfileListView

urlpatterns = [
    path('profile-list/', ProfileListView.as_view(), name='profile-list'),
]
