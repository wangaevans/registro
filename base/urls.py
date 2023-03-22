from django.urls import path,include
from . import views
app_name="base"

urlpatterns = [
    path('',views.home_view,name="home"),
    path('login',views.login_view,name="login"),
    path('register',views.register_view,name="register"),
    path('logout',views.logout_view,name="logout"),
    # path('members',views.members_view,name="members"),
    path('profile/<str:pk>/',views.profile_view,name="profile"),
    path('editprofile',views.edit_profile_view,name="editprofile"),
    # path('account/<str:pk>/',views.account_view,name="account"),
]
