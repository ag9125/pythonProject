
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from Olxapp.forms import SellForm,UpdateForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.views.generic import FormView
from django.core.paginator import Paginator
from Olxapp.models import Olx,Category,Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# for profile
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView, CreateView
# from about.forms import ProfileForm,UserForm

from about.models import Profile
##########

def homePage(request):

   save = Olx.objects.all().order_by('-list_date')
   cats = Category.objects.all()
   paginator = Paginator(save,7)
   page_number = request.GET.get('page')
   ServiceDataFinal =  paginator.get_page(page_number)
   totalPage = ServiceDataFinal.paginator.num_pages
   if  request.GET.get('serch') :
       item = request.GET.get('serch')
       if item!=None:
        ServiceDataFinal = Olx.objects.filter(title__icontains = item)  
       
  
   data = {
           'store':ServiceDataFinal,
           'cats':cats,
          
             'totalPage':totalPage, #to get last page
       'totalPageList' : [n+1 for n in range(totalPage)],
        }    
   return render(request,"navbar.html",data)

def show_image(request):
    return render(request, 'show_image.html')

def signup(request):
        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
           
            password1=request.POST.get('pass1')
            password2=request.POST.get('pass2')
            user=User.objects.filter(email=email)
            user2=User.objects.filter(username=name)
            
             
            if password1==password2:
                if user.exists():
                    messages.info(request,"Email already exists")
                    return redirect('/signup/')
                if user2.exists():
                    messages.info(request,"Username already exists")
                    return redirect('/signup/')
                
                user=User.objects.create(
                    
                    username=name,
                    email=email,
                    
                    # username=email,
                    # email=name,

                )
                user.set_password(password1)
                user.save()

                return redirect('/login/')
            
            else:
                messages.info(request,"Both Passwords Are Different")
                return redirect('/signup/')
        return render(request,"signup.html")


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid username")
            return redirect('/login/')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/show-image/')

        
    return render(request,"login.html")
@login_required(login_url='/login/')
def sell(request):
    if request.method == 'POST':
        formSell = SellForm(request.POST, request.FILES)
        if formSell.is_valid():
            recipe_instance = formSell.save(commit=False)
            recipe_instance.user = request.user
            recipe_instance.save()
            formSell.save()
            for Upload_image in request.FILES.getlist('more_images'):
                image_instance = Image(Upload_image=Upload_image, listing=recipe_instance)
                image_instance.save()
            
            def send_mail_to_client():
                   subject = " New Addition to Our Website!"
                   message =  f'''Dear User,
I hope this email finds you well. I'm excited to inform you that we have recently added a new item to our website that I believe you'll find intriguing.                              
Item Title : {recipe_instance.title}
Item Description :  {recipe_instance.Description}
For more information And To explore this exciting addition, simply visit our website and navigate to the  section/category. Don't hesitate to reach out if you have any questions or need assistance with anything.
Thank you for your continued support, and we look forward to serving you with more exciting offerings in the future.
Best regards,
Ankit Gupta
Contact Me : +919369599113'''
                   from_email = settings.EMAIL_HOST_USER
                   users = User.objects.all()
                   recipient_list = [x.email for x in users]

                   send_mail(subject,message,from_email,recipient_list)
            send_mail_to_client()
            return HttpResponseRedirect('/')
    else:
        formSell = SellForm()
  
    return render(request, "Recipe.html", {'formSell': formSell,})

def requests(request):
    event_list = Olx.objects.filter(Approved=False)
    if request.user.is_superuser:
         return render(request,"request.html",{'store':event_list})
    else:
       messages.success("You are not Authorized to this Page")
       return redirect('/')
    return render(request,"request.html")
def approve(request,id):
    item = Olx.objects.get(id=id)
    item.Approved = True
    item.save()
    return HttpResponseRedirect('/')
def deleteitem(request,id):
   queryset = Olx.objects.get(id =  id)
   queryset.delete()
   return HttpResponseRedirect("/myads/")

def updateitem(request,id):
   content = Olx.objects.get(id = id)
   if request.method == 'POST':
      data = request.POST
      title = request.POST.get('naam')
      price = request.POST.get('price')
      Description  = request.POST.get('description')
      recipe_image = request.FILES.get('file')
      content.title = title
      content.SET_A_PRICE = price
      content.Description = Description
      if recipe_image:
         content.Upload_image = recipe_image
      content.save()
      return HttpResponseRedirect("/")

   context = {'content':content}
   # print(content.recipe_name) Instant Pot® Shrimp Curry
   return render(request,"update.html",context)
def log_out(request):
   logout(request)
   return HttpResponseRedirect('/')
def item(request, id):
    cats = Category.objects.all()
    data = Olx.objects.get(id=id)
    img = Profile.objects.all()
    product_images = data.images.all()  # Assuming 'images' is the related name in the recipe model
    service = {'data': data, 'cats': cats, 'product_images': product_images,'content':img}
    return render(request, "item.html", service)

def category(request,id):
   
   cats = Category.objects.all()
   catid =Category.objects.get(id=id)
   save = Olx.objects.filter( category= catid)
   if  request.GET.get('serch') :
       item = request.GET.get('serch')
       if item!=None:
        save = Olx.objects.filter(title__icontains = item)  
        print(save) 
   data = {
           'store':save,
            'cats':cats,
            'catid':catid
        }    
   return render(request,"category.html",data)

@login_required(login_url='/login/')
def myads(request):
    cats = Category.objects.all()
    mylisting = Olx.objects.filter(user = request.user)
    data = {
         'cats':cats,
         'lst':mylisting
     }
    
    return render(request,"myads.html",data)

# profile
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
# from apps.userprofile.models import Profile

from django.contrib import messages

@login_required(login_url='/login/')
# def ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'profile.html'
def ProfileView(request):
    return render(request, "profile.html")



def profileUpdate(request):
    if request.method=='POST':
            username=request.POST.get('name')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')  #email changed evrywhere with username
            bio=request.POST.get('bio')
            phone=request.POST.get('phone')
            dob=request.POST.get('dob')
            image=request.FILES.get('pImage')


            user_profile, created = Profile.objects.get_or_create(user=request.user)

        # Update the user's email
            if email and email != request.user.email:
                request.user.email = email
                request.user.save()
            if username and username != request.user.username:
                request.user.username = username
                request.user.save()

            # Update the profile fields
            request.user.first_name=firstname
            request.user.last_name=lastname
            # user_profile.first_name=firstname
            # user_profile.last_name=lastname
            user_profile.bio = bio
            user_profile.phone_number = phone
            user_profile.birth_date = dob
            if image:
                user_profile.profile_image = image

            # Save the updated profile
            user_profile.save()

            # Redirect to the profile page
            return redirect('/profile/')  # Update this URL according to your project

    return render(request, 'profileUpdate.html')

