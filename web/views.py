import datetime
import json

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
from django.shortcuts import HttpResponse, render

from .models import requests,posts,font
from .updateTopPosts import updatePost,showCase


# Create your views here.
def index(request):
    des  = updatePost()
    films = showCase("Films")
    tv = showCase("Tv Serias")
    mod  = showCase("Mod Apps")
    pro = showCase("Pro Apps")
    sof  =showCase("Softwears")
    if request.COOKIES.get("_id") is not None:
        global isLoged
        isLoged = True
    else:
        isLoged  = False
        
    token  = get_token(request)
    print(tv)
    return render(request,"index.html",{"token":token,"isLoged":isLoged,"des":des,"films":films,"tv":tv,"pro":pro,"sof":sof,"mod":mod})


def signin(request):
    new_user =None
    if request.method== 'POST':
        response = {"errors":['no'],"isLoged":False}
        data =  request.POST
        dataB = [request.POST['email'],request.POST['password'],request.POST['first_name'],request.POST['last_name']]
        db  =User.objects.all()
        for i in db:
            if ( data['email']== str(i)):
                response['is']=False
                print('eledy exsites')
                response['errors'] = ['UserNameAlerdyExsites','']
                break
            else:
                try:
                    new_user = User.objects.create_user(dataB[2], dataB[0], dataB[1], first_name=dataB[2],last_name=dataB[3])
                    print("user objext",new_user)
                    if str(new_user) == str(dataB[2]):
                        response["is"] = True
                        response['errors'] = ["Succses full registation"]
                        print("saved",str(new_user))

             

                except:
                    print("not save")
                    response["is"] = False
                    response['errors'] = ["User name or email alerdy exsits"]
                break

        return HttpResponse( json.dumps(response))




def logIn(request):
    response = {"errors":"no","is":False,"isLoged":False}
    dataB = [request.POST['uname'],request.POST['password']]

    if request.COOKIES.get("_id") is not None:
        response['errors']  ="some one alerdy Loged"
        return HttpResponse(json.dumps(response))
    else:
        user =authenticate(username=dataB[0],password=dataB[1])
        if user is not None:
            response['errors']  ="sucsess full Login"
            response['is'] =True
            response['isLoged'] =True
            a  = HttpResponse(json.dumps(response))
            a.set_cookie("_id",1,60*60*60)
            return a
        else:
            response["errors"]="check your usernmae or password"
            response['isLoged'] =False
            return HttpResponse(json.dumps(response))
    




def newRequest(request):
    primarykey = request.COOKIES.get("_id")
    response = {'errors':'noErrors',"isLoged":False,"is":False,"request":False}
    if request.method == "POST":
        dataB = [request.POST['catagory'],request.POST['pname'],request.POST['ver'],request.POST['dev']]
        db =requests()
        print(dataB)
        user = User.objects.get(pk=primarykey)
        db.ide = user
        db.catogory = dataB[0]
        db.product_name =dataB[1]
        db.version =dataB[2]
        db.dev_company =dataB[3]
        if(requests.objects.filter(product_name=dataB[1]).exists()):
            response['errors']="Thanks for Your Request But aledry recived"
            response['is']=True
        else:
            try: 
                db.save()
            except:
                response['errors']="something went wrong"
                response['is']=False
            else:
                response['errors']="request send sucess"
                response['is']=True
                response['request']=True

   

        return HttpResponse(json.dumps(response))






def viewBox(request):
    id = int(request.GET['id'])
    db =posts.objects.get(pk=id)
    data = db.description

    return render(request,"view.html",{"data":data,"id":id})


def fonts(request):
    db = font.objects.all()
    return render(request,'fonts.html',{"data":db})


def tf(request):
    db =  None
    if request.method == "GET":
    
        if request.GET['para'] == "tv":
            db = posts.objects.filter(catagorye = "Tv Serias")
        
        elif request.GET['para'] == "films":
            db = posts.objects.filter(catagorye = "Films")
        
            
    return render(request,'tv_films.html',{"data":db}) 


def softwears(request):
    db =  None
    if request.method == "GET":
        print("GET METHOD",request.method,request.GET['para'])
        if request.GET['para'] == "mod":
            db = posts.objects.filter(catagorye = "Mod Apps")
            
        elif request.GET['para'] == "sof":
            db = posts.objects.filter(catagorye = "Softwears")
            
        elif request.GET['para'] == "pro":
            print("pro")
            db = posts.objects.filter(catagorye = "Pro Apps")

            
    print(db)        
    return render(request,"softwears.html",{"data":db})














def search(request):
    f  = request.GET['val']
    error = None
    result =  None
    data = []
    db = posts.objects.filter(title__contains = f)
    if len(db)==0:
        error = "No Result Pound"
        result = {"is":False,"error" : error,"data":None}
    else:
        error = str(len(db))+" result Pound"
        for i in range(len(db)):
            data.append([db[i].id,db[i].title])
            

        result = {"is":True,"error":error,"data":data}
    return HttpResponse(json.dumps(result))


def about_us(request):
    return render(request,"about_us.html")