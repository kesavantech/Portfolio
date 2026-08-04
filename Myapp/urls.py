from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView, name="home"),
    path("index/",views.IndexView, name="index"),
    path("profile/", views.ProfileView, name="profile"),
    path("contact/", views.ContactView, name="contact"),

    # Employee
    path("employee/", views.EmployeeView, name="employee"),
    path("employee_detailes/", views.EmployeeDetailsView, name="employee_detailes"),
    path("employee_edit/<int:emp_id>", views.EmployeeEditView, name="employee_edit"),
    path("employee_delete/<int:emp_id>", views.EmployeeDeleteView, name="employee_delete"),

]