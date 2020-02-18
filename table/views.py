from django.shortcuts import render


def show_table(request):
    name = 'OH DADDY'
    return render(request, 'table/index.html', context={'name': name})
