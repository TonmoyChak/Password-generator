from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)




    if request.GET.get('uppercase'):
        alphabet_string = string.ascii_uppercase
        alphabet_list.extend(alphabet_string)


    if request.GET.get('special'):
        alphabet_string = string.punctuation
        alphabet_list.extend(alphabet_string)

    if request.GET.get('numbers'):
        alphabet_string = string.digits
        alphabet_list.extend(alphabet_string)

    thePass= ''

    length= int(request.GET.get('length'))

    for x in range(length):
        thePass+= random.choice(alphabet_list)

    return render(request,'generator/password.html', {'password':thePass})
