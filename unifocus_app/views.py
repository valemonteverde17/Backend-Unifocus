from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from  django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request):
    return render (request,"home.html")


def register(request):
    if request.method == "GET":
        return render (request,"register.html",{
            "form" : UserCreationForm
        })
    else:
        req=request.POST
        if req['password1']==req['password2']:   
            try: 
                user = User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request,user)
                return redirect('/')
            except IntegrityError as ie:
                return render (request,"register.html",{
                "form" : UserCreationForm,
                "msg" : "Ese nombre de usuario ya exciste, favor de elegir otro nombre de usuario"
            })
            except Exception as e:
                return render (request,"register.html",{
                "form" : UserCreationForm,
                "msg" : "Se ha presentado el siguiente error {e}"
            })
        else:
            return render (request,"register.html",{
                "form" : UserCreationForm,
                "msg" : "Favor de verificar que las contraseñas coincidan"
            }) 

def iniciarSesion(request):
    if request.method=="GET":
        return render(request,"login.html",{
            "form": AuthenticationForm,
         })    
    else:
        try:
            user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,"login.html",{
                "form": AuthenticationForm,
                "msg" : "El usuario o la contraseña son incorrectos"
            }) 
        except Exception as e:
            return render(request,"login.html",{
                "form": AuthenticationForm,
                "msg" : f"Se produjo un error{e}"
            }) 
        
def cerrarsesion(request):
    logout(request)
    return redirect('/')
    
                   
