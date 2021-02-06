from django.shortcuts import render

# Create your views here.
def index(request):
    heading = "Maps"
    return render(request, "maps/index.html", {
        "heading": heading
    })
