from django.shortcuts import render

posts = [
    {
        'author': 'Anahita',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 27, 2022'
    },
    {
        'author': 'Elmira',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})