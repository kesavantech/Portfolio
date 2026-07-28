from django.shortcuts import render, redirect
from Myapp.models import Portfolio

# Create your views here.
def HomeView(request):
    return render(request, "Home.html")

def IndexView(request):
    return render(request, "index.html")

def ProfileView(request):
    profile = Portfolio.objects.first()

    if request.method == "POST":
        if profile is None:
            profile = Portfolio()

            '''
            என்று எழுதுறோம். இதன் அர்த்தம்
                "Database-ல Portfolio object இல்லையா?"
                "பரவாயில்லை... புதிய Portfolio object create பண்ணிக்கறேன்."
            '''
     
        
        profile.name = request.POST.get("name")
        profile.title = request.POST.get("title")
        profile.about = request.POST.get("about")
        profile.email = request.POST.get("email")
        profile.phone = request.POST.get("phone")
        profile.location = request.POST.get("location")
        profile.github = request.POST.get("github")
        profile.linkedin = request.POST.get("linkedin")

        if request.FILES.get("profile_image"):
            profile.profile_image= request.FILES.get("profile_image")
        
        if request.FILES.get("resume"):
            profile.resume = request.FILES.get("resume")
        profile.save()

        return redirect("home")
    return render(request, "profile.html", {"profile": profile})

