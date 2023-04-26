from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
            #get the new user info and set the group for this user to LibraryMember
            user = User.objects.get(username=uname)
            lib_group = Group.objects.get(name='LibraryMember')
            user.groups.add(lib_group)
            user.save()
            return redirect('login')

        return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

#add send e - mail confirmation
# set up the subject, message, and user’s email address
def passwordreset(request):
    subject = '{}, the email subject’.format(“Password Reset Requested”)'
    message = 'this is the message "{}"' #.format(“You requested for a password reset. Please find the link below”):

    user = request.user  # request was passed to the method as a parameter for the view
    user_email = user.email  # pull user’s email out of the user record

    # try to send the e-mail – note you can send to multiple users – this just sends
    # to one user.
    try:
        send_mail(subject, message, 'project0myclass@gmail.com', [user_email])
        sent = True
    except:
        print("Error sending e-mail")
