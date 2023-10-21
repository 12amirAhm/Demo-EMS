from django.shortcuts import render
from django.shortcuts import render, redirect
from My_app.forms import EmployeeForm  
from My_app.models import Employee  
 

#This function is used to ADD a single record  
def addnew(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
 
 
#This function is used to LIST all the employees
def index(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
 
 
#This function is used to link to edit page
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
 
 
#This function is used to UPDATE a single record
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  
 
#This function is used to DELETE a single record    
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/") 

#This function will show the home page
def home(request):
    return render(request, "home.html")
