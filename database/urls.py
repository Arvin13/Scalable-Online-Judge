from django.urls import path
from . import views


app_name = 'judge'
urlpatterns = [
        path('signin/', views.signin , name = 'signin'),
        path('signup/', views.signup, name = 'signup'),
        path('main/',views.contest, name='main'),
        path('<int:contest_id>/', views.problem, name='contest'),
        path('<int:contest_id>/<int:problem_id>/', views.submit, name='submission'),
        path('<int:contest_id>/<int:problem_id>/result', views.result, name='result'),
        path('test', views.test, name='test')
        ]
