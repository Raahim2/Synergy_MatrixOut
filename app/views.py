from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        web = request.POST.get('text')
        return render(request , 'index.html'  , {'web':web})
    return render(request , 'index.html'  )