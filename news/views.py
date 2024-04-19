from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'news/home.html')

def movies(request):
    news1 = 'Things fall apart'
    news2 = 'Telugu movie'
    news3 = 'Broken arrow 2'
    my_dict = {'news1': news1, 'news2': news2, 'news3': news3}
    return render(request, 'news/movies.html', context=my_dict)