from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import User, Resource, TrackParticipant
from .forms import CustomUserCreateForm,UserForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            if user is not None:
                login(request, user)
                messages.info(request, 'You have succesfully logged in.')
                return redirect('base:home')
            else:
                messages.error(request, 'Email OR Password is incorrect')
                return redirect('base:login')
    else:
        form=AuthenticationForm()

    return render(request,'login.html',{'form':form})

def register_view(request):
    if request.method=='POST':
        form=CustomUserCreateForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            login(request, user)
            messages.success(request, 'User account was created!')
            return redirect('base:home')
        else:
            messages.error(request, 'An error has occurred during registration')
        
    else:
        form=CustomUserCreateForm()

    return render(request,'register.html',{'form':form})
    
@login_required(login_url='/login')
def home_view(request):
    user=request.user
    tracks = TrackParticipant.objects.filter(participant=user)
    resources = Resource.objects.all()

    context = {'resources': resources,'tracks': tracks,}
    return render(request,'home.html',context)


def logout_view(request):
    logout(request)
    return redirect('base:login')

# @login_required(login_url='/login')
# def members_view(request):
#     members=User.objects.all()
#     return render(request,'all_members.html',{'members':members})

@login_required(login_url='/login')
def profile_view(request,pk):
    profile=User.objects.get(id=pk)
    return render(request,'profile.html',{'profile':profile})


@login_required(login_url='/login')
def edit_profile_view(request):

    form = UserForm(instance=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES,  instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('base:home')

    context = {'form': form}
    return render(request, 'edit_profile.html', context)


# @login_required(login_url='/login')
# def account_view(request,pk):

#     # user = request.user
#     account = User.objects.get(id=pk)
#     context = {'account': account}
#     return render(request, 'account.html', context)

