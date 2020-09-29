import random

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "generator/home.html")


def password(request):
    password_length = int(request.GET.get('length'))
    password_uppercase_letter = request.GET.get('uppercase')
    password_number = bool(request.GET.get('number'))
    password_special = bool(request.GET.get('special'))

    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_letters = list('ABCDEFGHIJKLMNPQRSTUVWXYZ')
    numbers = list('0123456789')
    special_characters = list('!"§$%&()=?*#;:')

    charactor_list = lowercase_letters

    if password_uppercase_letter:
        charactor_list += uppercase_letters
    if password_number:
        charactor_list += numbers
    if password_special:
        charactor_list += special_characters

    new_password = ''.join(random.choice(charactor_list) for i in range(password_length))

    return render(request, "generator/password.html", {'password': new_password})

