from django.shortcuts import render, redirect
from Myapp.models import Portfolio, Employee
from django.contrib import messages
from django.shortcuts import get_object_or_404

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
        profile.hero_description = request.POST.get("hero_description")

        if request.FILES.get("profile_image"):
            profile.profile_image= request.FILES.get("profile_image")
        
        if request.FILES.get("resume"):
            profile.resume = request.FILES.get("resume")
        profile.save()

        return redirect("home")
    return render(request, "profile.html", {"profile": profile})

def ContactView(request):
    return render(request, "contact.html")


def EmployeeView(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_email = request.POST.get("emp_email")
        emp_phone = request.POST.get("emp_phone")
        emp_salary = request.POST.get("emp_salary")
        emp_address = request.POST.get("emp_address")

        emp = Employee.objects.create(
            emp_name = emp_name, emp_email = emp_email,
            emp_phone = emp_phone, emp_salary = emp_salary,
            emp_address = emp_address
        )
        
        messages.success(request, f"Employee '{emp.emp_name}' Profile created ")
        print(f"Employee '{emp.emp_name}' Profile Created Successfully !")
        return redirect("home")
    
    return render(request, "employee.html")

def EmployeeDetailsView(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees
    }
    return render(request, "employee_details.html", context)

def EmployeeEditView(request,emp_id):
    
    employee = get_object_or_404(Employee, id = emp_id)
    if request.method == "POST":
        employee.emp_name = request.POST.get("emp_name")
        employee.emp_email = request.POST.get("emp_email")
        employee.emp_phone = request.POST.get("emp_phone")
        employee.emp_salary = request.POST.get("emp_salary")
        employee.emp_address = request.POST.get("emp_address")

        employee.save()
        messages.success(request,f"Employee Updated Successfully !")
        return redirect("employee_detailes")
    context = {
        "employee" : employee
    }
    return render(request,"employee_edit.html",context)

def EmployeeDeleteView(request, emp_id):
    employee = get_object_or_404(Employee,id = emp_id)

    employee.delete()
    messages.success(request,f"user '{employee.emp_name}' Deleted Successfully !")
    
    return render(request,"employee_delete.html")