from .models import Portfolio, Skill

def profile_data(request):
    profile = Portfolio.objects.first()

    return {
        "profile" : profile,
        
    }

def skill_data(request):
    skill = Skill.objects.all()

    return {
        "skill": skill
    }
