from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    return redirect('/random_words')

def random(request):
    if request.method == 'GET':
        print('GET method is being ran')
    if 'counter' not in request.session:
        request.session['counter'] = 0

    request.session['random_char']=get_random_string(length=14)
    request.session['counter'] += 1
    return render(request, 'random_word_gen.html')

# def zero(request):
#     request.session['counter'] = 0
#     return render(request, 'random_word_gen.html')
def zero(request):
    request.session.flush()
    return redirect('/random_words')

# Create your views here.


