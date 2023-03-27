from django.shortcuts import render,redirect
from django.db.models.functions import ExtractWeekDay,ExtractMonth
from django.db.models import Count
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import User, Material,HuaweiTrack,Participant
from .forms import CustomUserCreateForm,UserForm,HuaweiTrackForm

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
            form.instance.username = f'{random.randrange(10000000)}'
            user=form.save()
            
            login(request, user)
            messages.success(request, 'User account was created!')
            return redirect('base:select-huawei-track')
        else:
            messages.error(request, 'An error has occurred during registration')
        
    else:
        form=CustomUserCreateForm()

    return render(request,'register.html',{'form':form})

    
@login_required(login_url='/login')
def home_view(request):
    user=request.user
    huawei_track = request.user.huaweitrack_set.first()
    materials=Material.objects.filter(track=huawei_track)
    context = {'track': huawei_track,'materials':materials,}
    return render(request,'home.html',context)
    
@login_required(login_url='/login')
def resources_view(request):
    user=request.user
    huawei_track = request.user.huaweitrack_set.first()
    materials=Material.objects.filter(track=huawei_track)
    context = {'track': huawei_track,'materials':materials,}
    return render(request,'resources.html',context)

def logout_view(request):
    logout(request)
    return redirect('base:login')

def about_view(request):
    return render(request, 'about.html',)


@login_required(login_url='/login')
@permission_required(perm="/dashboard",raise_exception=True)
def dashboard_view(request):
    students=User.objects.filter(is_superuser=False)
    # weekly
    users_by_day=User.objects.annotate(
        day=ExtractWeekDay('date_joined')
    ).values('day').annotate(count=Count('id')).order_by('day')
    weeklylabels=['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat','Sun']
    weeklydata=[0]*7
    for user in users_by_day:
        weeklydata[user['day']-1]=user['count']
        # monthly 
    users_by_month=User.objects.annotate(
        month=ExtractMonth('date_joined')
    ).values('month').annotate(count=Count('id')).order_by('month')
    monthlylabels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    monthlydata=[0]*12
    for user in users_by_month:
        monthlydata[user['month']-1]=user['count']


    return render(request, 'dashboard/dashboard.html',{'students':students,'weeklylabels':weeklylabels, 'weeklydata':weeklydata,'monthlylabels':monthlylabels,'monthlydata':monthlydata})

@login_required(login_url='/login')
def all_students_view(request):
    students=User.objects.filter(is_superuser=False)
    return render(request, 'dashboard/all_students.html',{'students':students})

@login_required(login_url='/login')
def administrators_view(request):
    admins=User.objects.filter(is_superuser=True)
    return render(request, 'dashboard/admins.html',{'admins':admins})

@login_required(login_url='/login')
def calendar_view(request):
    return render(request, 'dashboard/calendar.html',)


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

def select_huawei_track(request):
    if request.method == 'POST':
        form = HuaweiTrackForm(request.POST)
        if form.is_valid():
            track_name = form.cleaned_data['track']
            # get the selected track from the database
            huawei_track = HuaweiTrack.objects.get(name=track_name)
            # add the user to the participants of the track
            huawei_track.participants.add(request.user)
            return redirect('base:home')  # replace with the appropriate URL
    else:
        form = HuaweiTrackForm()
    return render(request, 'select_huawei_track.html', {'form': form})

