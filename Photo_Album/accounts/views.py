from django.shortcuts import render


def index(request):
    txt = 'Some text'
    context = {
       'txt': txt,
    }

    return render(request, 'accounts/to_delete.html', context)