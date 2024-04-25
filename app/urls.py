from django.urls import path
from .views import hello, music, music_details, nameidentifier, ageidentifier, template_example, musicians

urlpatterns = [
    path('hello/<str:name>', hello),
# domainname.com/year/month/slug
    path('nameidentifier/<name>', nameidentifier),
    path('ageidentifier/<int:age>', ageidentifier),
    
    path('htmlpage', template_example, name='htmlpage'),
    path('music', music, name='music'),
    path('music_details/<int:id>', music_details, name='music_details'),
    path('musicians', musicians, name='singers')
]
