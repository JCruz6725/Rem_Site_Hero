from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('accounts/<str:username>/', views.AccountDetail.as_view()),
    path('resume/', views.UserResumeList.as_view()),
    path('project/', views.UserProjectList.as_view()),
    path('education/', views.UserEducationList.as_view()),
    path('professional/', views.UserProfessionalList.as_view()),
    #path('project/<int:id>', views.ProjectDetail.as_view())
    #path('person/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)