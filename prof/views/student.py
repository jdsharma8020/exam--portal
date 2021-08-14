from django.shortcuts import render
from main.models import *
from authAccount.models import User
from django.http import HttpResponseForbidden


def view_students(request):
    prof = request.user
    return render(request, 'prof/student/view_students.html', {
        'students': User.objects.filter(isStudent=True), 'prof': prof
    })
    