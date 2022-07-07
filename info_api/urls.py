from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import views

urlpatterns = [
    #path('accounts/', views.AccountList.as_view()),
    #path('accounts/<str:username>/', views.AccountDetail.as_view()),



    path('resume/', views.UserResumeList.as_view()),

    path('project/', views.UserProjectList.as_view()),
    path('project/<str:project_name>', views.UserProjectUpdate.as_view()),
    
    path('education/', views.UserEducationList.as_view()),
    path('professional/', views.UserProfessionalList.as_view()),


    path('profile/<str:email>/', views.ProfileView.as_view()),

    path('profile/<str:email>/<str:title>', views.ProfileResumeView.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)