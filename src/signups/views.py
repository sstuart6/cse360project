from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from django.contrib import messages
# Create your views here.

from .forms import UserForm
from .forms import LoginForm
from .forms import PictureForm
from .forms import SettingsForm
#need settings form

from .models import User
from .models import Picture
from .models import Settings
#need settings model

from django.core.validators import EmailValidator

#defining home
def home(request) :
    
    return render_to_response("home.html",
                              locals(),
                              context_instance = RequestContext(request))
def register(request) :
    
    form = UserForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for joining!')
        return HttpResponseRedirect('/thank-you/')

    return render_to_response("register.html",
                              locals(),
                              context_instance = RequestContext(request))
def thankyou(request) :

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance = RequestContext(request))
def userhome(request) :
    
    form = UserForm(request.POST or None)
    form = PictureForm(request.POST or None)
    loginUser = User.objects.get(id=request.session['current_user_id'])
    pictures = Picture.objects.filter(user_id=loginUser)
    context_instance = RequestContext(request)
    context_instance['current_user'] = loginUser
    context_instance['pictures'] = pictures
    
    #online code start --------------------------------------
    # Handle file upload
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = Picture(user_id=loginUser, photo= form.cleaned_data['photo'])
            newpic.save()

    else:
        form = PictureForm() # A empty, unbound form
    # Load documents for the list page
    photos = pictures
    # Render list page with the documents and the form
    return render(request, "userhome.html",{'photos': photos, 'form': form, 'loginUser': loginUser})
    #online code end ---------------------------------------
    #this would be an example of a page where you use the session    

def settings(request) :
    loginUser = User.objects.get(id=request.session['current_user_id'])
    # Handle file upload
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = Settings.objects.get_or_create(user=loginUser)[0]
            newpic.profile_pic = form.cleaned_data['profile_pic']
            newpic.save()
            # Redirect to the document list after POST
    else:
        form = SettingsForm() # A empty, unbound form

    # Load documents for the list page
    settings = loginUser.settings.all()
    settings = settings[:1].get() if settings.exists() else None

    # Render list page with the documents and the form
    return render(request, "settings.html",{'settings': settings, 'form': form, 'loginUser': loginUser})

def aboutus(request) :
    
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance = RequestContext(request))
def logout(request):
    try:
        del request.session['current_user_id']
    except KeyError:
        pass
    #return HttpResponse("You're logged out.")
    return render_to_response("logout.html",
                              locals(),
                              context_instance = RequestContext(request))

def login(request):
    
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        #next line etches the user information 
        loginUser = User.objects.get(email= request.POST['email'])
        
        #next line validates the password 
        if loginUser.password == request.POST['password']:
            #if the password is correct to the username, go to thank you
            #change it to go to the main page of the User
            request.session['current_user_id'] = loginUser.id
            return HttpResponseRedirect('/userhome')
        else:
            messages.success(request, 'SHIT! You must enter the correct password to see your shit')
            
            return render_to_response("login.html",
                              locals(),
                              context_instance = RequestContext(request))
    else:
        return render_to_response("login.html",
                              locals(),
                              context_instance = RequestContext(request))
    
    
