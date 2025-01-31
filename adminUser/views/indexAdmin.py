from django.shortcuts import render

# Create your views here.

def indexAdmin(request):
    return render(request, 'admin/indexAdmin.html')


def baseAdmin(request):
    return render(request, 'admin/baseAdmin.html')