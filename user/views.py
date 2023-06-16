from django.shortcuts import render,redirect
import json
from . import algo
from . import mongodb
# Create your views here.

# Create your views here.
from django.http import HttpResponse
'''
f = open('../user_data.json')
a_data = json.load(f)
print(a_data)
'''
def user(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        data={'email':email,'pwd':pwd}
        '''
        f = open('user_data.json')
        a_data = json.load(f)
        if not a_data: a_data={}
        dd=algo.find(a_data,email)
        '''

        db=mongodb.DB()
        ddd=db.retrieve_user(email)
        if not ddd:
            return render(request,"user.html",{'success':data,'status':'Your email address is not registered yet','email':email})
        elif not ddd['password']==pwd:
            return render(request,"user.html",{'success':data,'status':'The password is incorrect. Please try again','email':email})
        else:
            return redirect('/user/profile?email='+email)
            #return profile(request,email)
        return render(request,"user.html",{'name':'1234'})
    return render(request,"user.html")

def profile(request):
    email=request.GET['email']
    db=mongodb.DB()
    data=db.retrieve_user(email)
    return render(request,"profile.html",{'status':'Success','user':data})

def editprofile(request):
    if request.method=='GET':
        email=request.GET['email']
        db=mongodb.DB()
        data=db.retrieve_user(email)
        return render(request,'editprofile.html',{'user':data})
    if request.method=='POST':
        name=request.POST['name']
        job=request.POST['job']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        hoppy=request.POST['hoppy']
        data={'name':name,'job':job,'phone':phone,'age':age,'hoppy':hoppy}
        db=mongodb.DB()
        db.collection.update_one(
            {'email': email},
            {'$set':
                 data
             }
        )
        return redirect('/user/profile?email=' + email)
        #return profile(request,email)
    return render(request,'editprofile.html')
def register(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        r_pwd=request.POST['r_pwd']
        data={'email':email,'password':pwd}
        '''
        f = open('user_data.json')
        a_data = json.load(f)
        if not a_data: a_data={}
        '''
        db=mongodb.DB()
        if db.exist_user(email):
            return render(request, "register.html", {'fail': 'Your email address is already registered!', 'data': data})
        elif pwd == r_pwd:
            '''
            f = open("user_data.json", "w")
            a_data.update({len(a_data): data})
            f.write(json.dumps(a_data))
            # print(a_data)
            f.close()
            '''
            db.insert_user(data)
            return render(request, "register.html", {'success': data, 'data': data})
        else:
            return render(request, "register.html", {'fail': 'Password not match! Please try again.', 'data': data})
    return render(request,"register.html")

def submit(request):
    if request.method=='POST':
        return render(request,"submit.html",{})
        #return HttpResponse('hi')
    return render(request,"user.html")

