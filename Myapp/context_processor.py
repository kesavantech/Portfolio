from .models import Portfolio, Skill, Education

def profile_data(request):
    profile = Portfolio.objects.first()


    return {
        "profile" : profile,
        
    }

def skill_data(request):
    skills = Skill.objects.all()

    return {
        "skills": skills
    }

def education_data(request):
    educations = Education.objects.all()
    return{
        "educations" : educations
    }
