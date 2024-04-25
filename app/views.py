from django.http import HttpResponse
from django.shortcuts import render

musicians_data = {
        'favorite_musicians': [
            {'id':1,'name': 'Nusrat Fateh Ali Khan', 'genre': 'Qawwali'},
            {'id':2,'name': 'Arijit Singh', 'genre': 'Bollywood'},
            {'id':3,'name': 'Atif Aslam', 'genre': 'Pop'}
        ]
    }

def musicians(request):
    return render(request, 'musicians.html', musicians_data)

# Create your views here.
def music_details(request, id):
    
    return render(request, 'music_details.html')

def hello(request, name):
    context = {
        'name': name,
        'age': 23,
        'courses': ['Course 1', 'Course 2', 'Course 3']
    }
    return render(request, 'students.html', context)

def nameidentifier(request, name):
    print(type(name))
    return HttpResponse(f'Hello, {name}!')

def ageidentifier(request, age):
    print(type(age))
    return HttpResponse(f'You are {age} years old!')

def template_example(request):
    
    return render(request, 'index.html', context)

def music(request):
    context = {
        'musicians': [
            {'id': 1, 'name': 'Nusrat Fateh Ali Khan', 'genre': 'Qawwali'},
            {'id': 2, 'name': 'Arijit Singh', 'genre': 'Bollywood'},
            {'id': 3, 'name': 'Atif Aslam', 'genre': 'Pop'}
        ]
    }
    return render(request, 'music.html', context)
