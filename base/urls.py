from django.urls import path,include
from . import views

app_name='base'

urlpatterns = [
    path('',views.home_view,name="home"),
    path('resources',views.resources_view,name="resources"),
    path('login',views.login_view,name="login"),
    path('register',views.register_view,name="register"),
    path('administrators',views.administrators_view,name="administrators"),
    path('logout',views.logout_view,name="logout"),
    path('dashboard',views.dashboard_view,name="dashboard"),
    path('all-students',views.all_students_view,name="all-students"),
    path('calendar',views.calendar_view,name="calendar"),
    path('about',views.about_view,name="about"),
    path('profile/<str:pk>/',views.profile_view,name="profile"),
    path('editprofile',views.edit_profile_view,name="editprofile"),
    path('select-huawei-track', views.select_huawei_track, name='select-huawei-track'),
]
