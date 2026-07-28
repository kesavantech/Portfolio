from .models import Portfolio

def profile_data(request):
    profile = Portfolio.objects.first()

    return {
        "profile" : profile
    }
