from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,WebPage
from first_app.forms import EmailForm,PostForm, UserForm
from first_app.forms import UserProfileInfo

from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    context = {'access_record':webpage_list, 'name':'amir mahdi rashvand', 'number':10000}
    template = 'index.html'
    return render(request, template, context )


def about(request):

    template = "first_app/about.html"
    message = "you are now beginner and 3 weeks after you are professional"
    return render(request, template, {'message':message})


def form(request):
    form = EmailForm()
    template = 'form.html'
    context = {'form':form}


    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            print('name  : ' +form.cleaned_data['name'])
            print('email : '+ form.cleaned_data['email'])
            print('text  : '+ form.cleaned_data['text'])

    return render(request, template, context)


def postform(request):

    post_form = PostForm()
    template = 'post_form.html'
    context = {'post_form':post_form}


    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save(commit=True)
            # print('name  : ' +post_form.cleaned_data['top'])
            print('email : '+ post_form.cleaned_data['url'])
            print('text  : '+ post_form.cleaned_data['name'])
        else:
            print("form invalid")


    return render(request, template, context)


def other(request):
    return render(request, 'other.html')



#  ارور داریم برای لاگین دوباره قسمت ها رو ببین
# register form
def register(request):

    registerd = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=True)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registerd = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form  = UserProfileInfo()

    return render(request, 'registration.html', {'user_form':user_form,
                                                'profile_form':profile_form,
                                                 'registerd':registerd})



@login_required
def special(request):
    return HttpResponse("you are logged in")
# user logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponse(reverse('index'))
# user login
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print("someone tried to login failed")
            print("username : {} and password {}".format(username,password))
