from django.urls import path
from .views import hello, music, musician_details, nameidentifier, ageidentifier, template_example, musicians

urlpatterns = [
    path('hello/<str:name>', hello),
# domainname.com/year/month/slug
    path('nameidentifier/<name>', nameidentifier),
    path('ageidentifier/<int:age>', ageidentifier),
    
    path('htmlpage', template_example, name='htmlpage'),
    path('music', music, name='music'),
    path('musician_details/<int:id>', musician_details, name='singer_details'),
    path('musicians', musicians, name='singers')
]
