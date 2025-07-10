from django.shortcuts import render
# handles the requests

# Create your views here.
def home (request):
    """Render the home page

    """
    return render(request, 'home.html')
def login_views(request):
    return render(request, 'login.html')

def signup_views(request):
    return render(request, 'signup.html')
