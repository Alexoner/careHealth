from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from accounts.forms import UserForm, UserProfileForm


# Create your views here.
def register(request):
    # Like before,get the request's context.
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # two forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # save the user's form data to the database
            user = user_form.save()

            # hash the password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # save UserProfile model instance
            profile.save()

            registered = True

        # invalid forms,
        else:
            print user_form.errors, profile_form.errors

    # not a http post
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context
    return render_to_response(
        'accounts/register.html',
        {'user_form': user_form,
         'profile_form': profile_form,
         'registered': registered},
        context
    )


def user_login(request):
    # Like before,obtain the context for user's requst
    context = RequestContext(request)

    # If the request is a HTTP POST,try to pull out the relevant information
    if request.method == 'POST':
        # Gather the username and password provided by the user
        # This is information is obtained from the login form
        username = request.POST['username']
        password = request.POST['password']

        # Django's machinery to check if the combination is valid
        user = authenticate(username=username, password=password)

        # have a User object,details are correct
        if user:
            # active
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/polls/')
            else:
                # A inactive account was used - no logging in!
                return HttpResponse("Your account is disabled")
        else:
            # Bad login details
            print "Invalid login details:{0},{1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # request not a HTTP POST.
    else:
        # No context variables to pass to the template system,hence the
        # blank dictionary object...
        return render_to_response('accounts/login.html', {}, context)


# use the login_required() decorator to ensure only those logged in can
# access the view
@login_required(login_url='/accounts/login/')
def user_logout(request):
    # Since we know the user is logged in,we can now just log them out.
    logout(request)

    # Take the user back to the homepage
    return HttpResponseRedirect('/admin/')
