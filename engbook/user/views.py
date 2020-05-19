from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from log.models import Logger



  



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('profile-edit')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
##        b_form = BioUpdateForm(request.POST, request.FILES, instace=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
##            b_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-edit')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
##        b_form = BioUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
##        'b_form':b_form
    }

    return render(request, 'user/profile-edit.html', context)


def homepage(request):
    context = {
        'loggers': Logger.objects.filter(user=request.user)
    }

    return render(request, 'user/homepage.html', context)


def landingpage(request):
    return render(request, 'user/landingpage.html')

def viewlog(request, uuid):
    try:
        selectedlog = Logger.objects.filter(slug=uuid)[0]
        context = {
            "logger": selectedlog
        }
    except:
        context = {
            "error":"404 - The selected log was not found"
        }
    return render(request, 'user/viewlog.html', context)


def editlog(request, uuid):
    if request.method == "POST":
        logtext = request.POST.get('logdata', False)
        logtitle = request.POST.get('logtitle', False)
        thelog = Logger.objects.filter(slug=uuid)[0]
        thelog.note=logtext
        thelog.title=logtitle
        thelog.save()


        messages.success(request, 'Your log has been saved')    
        return redirect('user-home')
    try:
        selectedlog = Logger.objects.filter(slug=uuid)[0]
        context = {
            "logger": selectedlog
        }
    except:
        context = {
            "error":"404 - The selected log was not found"
        }
    return render(request, 'user/editlog.html', context)

def newlog(request):
    if request.method == "POST":
        logtext = request.POST.get('logdata', False)
        logtitle = request.POST.get('logtitle', False)
        newlog = Logger.objects.create(
            note=logtext,
            user=request.user,
            title=logtitle,


        )
        newlog.save()

        messages.success(request, 'Your log has been created')
        return redirect('user-home')
        # return redirect('home')
    return render(request, 'user/newlog.html')