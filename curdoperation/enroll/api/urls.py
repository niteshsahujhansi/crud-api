# from django.urls import include, path
# from enroll.api import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('crud', views.UserViewSet, basename='user')

# urlpatterns = [
#     path('', include(router.urls))
# ]

# /////////////////////////////////////////////////////////////////////////////////////////

# from django import views
# from . import views 
from enroll.api import views
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    # path('stuinfo/<int:pk>', views.student_detail),
    # path('stuinfo/', views.student_list),
    # path('stucreate/', views.student_create),
    # path('crud/', views.student_api),
    # path('crud/<int:pk>', views.student_api),
    path('crud/', views.StudentAPI.as_view()),
    path('crud/<int:pk>', views.StudentAPI.as_view()),
]