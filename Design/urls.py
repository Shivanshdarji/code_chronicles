from django.urls import path
from . import views

urlpatterns = [
   
    path("",views.home,name="home"),
    path("student_login",views.student_login,name="student_login"),
    path("student_login1",views.student_login1,name="student_login1"),
    path("Logintrans",views.Logintrans,name="Logintrans"),
    path("Logintrans1",views.Logintrans1,name="Logintrans1"),
    path("intro",views.intro,name="intro"),
    path("map",views.map,name="map"),
   path('topic1', views.topic1, name='topic1'), 
   path('topic2', views.topic2, name='topic2') ,
   path('topic3', views.topic3, name='topic3'),
   path('nested', views.nested, name='nested'),
   path('index1', views.index1, name='index1'),
    path('thanks', views.thanks, name='thanks'),
     path('datatypes', views.datatypes, name='datatypes'),
    path('index2', views.index2, name='index2'),
    path('thanks2', views.thanks2, name='thanks2'),
    path("map1",views.map1,name="map1"),
    path('index3', views.index3, name='index3'),
    path('thanks3', views.thanks3, name='thanks3'),
    path('index4', views.index4, name='index4'),
    path('thanks4', views.thanks4, name='thanks4'),
    path('index5', views.index5, name='index5'),
    path('thanks5', views.thanks5, name='thanks5'),
    path('arithmetic', views.arithmetic, name='arithmetic'),
    path('logical', views.logical, name='logical'),
    path('variables', views.variables, name='variables'),
     path('progress', views.progress, name='progress'),
      path('review', views.review, name='review'),
   path('interactive_page', views.interactive_page, name='interactive_page')
]