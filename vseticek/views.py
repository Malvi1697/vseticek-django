from django.shortcuts import render

def home_view(request):
    context = {
        'page_title': 'Vseticek.com'
        }
    return render(request, 'portfolio.html', context)
