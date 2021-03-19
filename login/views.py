from django.shortcuts import render

def home(request):
    return render(request,'login/homepage.html')
def adminLogin(request):
    return render(request,'login/adminLogin.html')
def staffLogin(request):
    return render(request,'login/staffLogin.html')
def admin(request):
    return render(request,'login/adminHome.html')
def staff(request):
    return render(request,'login/staffHome.html')
def event(request):
    return render(request,'login/deptHome.html')
def staffdet(request):
    return render(request,'login/staffDetails.html')
def staffreg(request):
    return render(request,'login/staffReg.html')
def studentdet(request):
    return render(request,'login/studentDetails.html')
def studentreg(request):
    return render(request,'login/studentReg.html')
