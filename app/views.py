from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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
    context = {
        'name': 'Mamoon',
        'age': 25,
        'hobbies': ['Reading', 'Coding', 'Gaming'],
        'friends': [
            {'name': 'Ali', 'age': 25},
            {'name': 'Ahmed', 'age': 24},
            {'name': 'Asad', 'age': 26}
        ],
        'favorite_musicians': [
            {'name': 'Nusrat Fateh Ali Khan', 'genre': 'Qawwali'},
            {'name': 'Arijit Singh', 'genre': 'Bollywood'},
            {'name': 'Atif Aslam', 'genre': 'Pop'}
        ]
    }
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

def music_details(request, id):
    context = {
        'musician': {
            'id': id,
            'name': 'Nusrat Fateh Ali Khan',
            'genre': 'Qawwali'
        }
    }
    return render(request, 'music_details.html', context)