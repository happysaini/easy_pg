from django.shortcuts import render,HttpResponse
from main.form import Login,SignUp, SignUpOwnForm, LoginOwn,PgDetails
from main.models import SignUpData,SignUpOwnData,PgDetailData
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponseNotFound
# Create your views here.

u_id = None
def index(request):
    global u_id
    if request.session.has_key('u_id'):
        
        u_id = request.session['u_id']
        name = request.session['name']
    return render(request,'main/index.html', {"u_id":u_id,"name":name})
def logout(request):
    request.session.clear(); 
    global u_id
    u_id = None       
    return HttpResponseRedirect("/")
def display_owner(request):   
    return render(request,'main/display_owner.html')
def display_tenant(request):
    pgdata=PgDetailData.objects.all()
    return render(request,'main/display_tenant.html',{'pgdata':pgdata})
# just for testing
def tenant_help(request):
    return render(request,'main/tenant_help.html')
def edit(request):
    if(request.method=="POST"):
        #Getting data from the form
        form=PgDetails(request.POST,request.FILES) # if subsequent request => need to pass data in method  #Bound Form
 
        if(form.is_valid()):
           form.save()
           return HttpResponseRedirect("/")
        else:
            return render(request,"main/edit.html",{"form":form})
    else:
        form=PgDetails()
        return render(request,'main/edit.html',{"form":form})

def owner_help(request):
    return render(request,'main/owner_help.html')
def about(request):
    return render(request,'main/about.html')
def helps(request):
    return render(request,'main/help.html')
def home(request):
    return render(request,'main/home.html')
def tandc(request):
    return render(request,'main/tandc.html')
def signview(request):
    return render(request,'main/signview.html')

def loginown(request):
    if(request.method=='POST'):
        data=SignUpOwnData.objects.all().values()
        match=request.POST
        catch=LoginOwn(match)        
        return render(request,'main/display_owner.html',{"data":data})        
    else:
        form=Login()
        return render(request,'main/loginown.html',{"form":form})
    
def loginview(request):
    return render(request,'main/loginview.html')
# this is a login form
def signup(request):
    if(request.method=="POST"):
        data=request.POST
        form=SignUp(data)       
        if(form.is_valid()):
            name=form.cleaned_data["name"]
            contact=form.cleaned_data["contact"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            p=SignUpData(name=name,contact=contact,email=email,password=password)
            p.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,'main/signup.html',{"form":form})
    else:
        form=SignUp()
        return render(request,'main/signup.html',{"form":form})
# this is a login fuction

def login(request):   
    if request.method == "POST":
        data = request.POST #Getting data from the form
        form = Login(data) # if subsequent request => need to pass data in method  #Bound Form
        if form.is_valid():
            u_email = form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]          
            p = SignUpData.objects.filter(email=u_email,password=u_password).values('id','name','contact','email','password')
            x = list(p)
            for x1 in x:                
                user_id = x1['id']
                name = x1['name']
                contact=x1['contact']
                email=x1['email']
                password=x1['password']                
            if (p.count()>0):  #session is mantained from here
                request.session['u_id'] = user_id
                request.session['name'] = name
                request.session['contact'] = contact
                request.session['email'] = email
                return HttpResponseRedirect("/display_tenant")
            else:
                form = Login()
                return render(request,"main/login.html",{"form":form, "msg":"Wrong email or password"})
        else:
            return render(request,"main/login.html",{"form":form}) #UnBound Form
    # Not a subsequent Request
    else:       
        form = Login() # if first request then no need to pass data in method
        return render(request,'main/login.html',{"form":form})
# this is a owner from and 
def signupown(request):
    if(request.method=="POST"):
        data=request.POST #Getting data from the form
        sform=SignUpOwnForm(data) # if subsequent request => need to pass data in method  #Bound Form
        if(sform.is_valid()):
            ownername1=sform.cleaned_data["ownername"]
            owneremail1=sform.cleaned_data["owneremail"]
            ownerpassword1=sform.cleaned_data["ownerpassword"]
            ownercontact1=sform.cleaned_data["ownercontact"]     
            p=SignUpOwnData(ownername=ownername1,owneremail=owneremail1,ownerpassword=ownerpassword1,ownercontact=ownercontact1)
            p.save()             
            return HttpResponseRedirect('main/edit.html')            
        else:
            return render(request,"main/signupown.html",{"form":sform}) #UnBound Form
    # Not a subsequent Request
    else:       
        sform=SignUpOwnForm() # if first request then no need to pass data in method
        return render(request,'main/signupown.html',{"form":sform})     