from django.shortcuts import render

# Create your views here.
def start(request):
    if request.user.is_superuser == True:
        return render(
            request = request,
            template_name = 'start.html',
            context = None
        )