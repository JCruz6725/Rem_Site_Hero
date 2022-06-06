from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('project/', views.ProjectList.as_view()),
    path('project/<int:id>', views.ProjectDetail.as_view())
    #path('person/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)