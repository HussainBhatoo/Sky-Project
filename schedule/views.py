from django.shortcuts import render

def placeholder(request):
    """Temporary placeholder for student modules"""
    return render(request, 'placeholder.html', {'app_name': 'Project Schedule'})
