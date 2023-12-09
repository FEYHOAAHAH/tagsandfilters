from django.shortcuts import render


# Create your views here.

def show_tag_page(request):
    return render(request, 'mytags.html')
