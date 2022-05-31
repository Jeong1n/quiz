from django.shortcuts import render, redirect
from .models import Category,Article


def home(request):
    return render(request, 'new.html')



def posting(request):
    if request.method == 'POST':
        posting = request.posting
        my_post = Category()
        my_post.author = posting
        my_post.content = request.POST.get('posting', '')
        my_post.save()
        return redirect('/home')