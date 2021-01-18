from django.shortcuts import render
from django.contrib.auth import logout as log_out
from django.contrib.auth import login as log_in
from .models import *
import jsonpickle
from django.core import serializers
from .forms import *
from django.shortcuts import redirect
# Create your views here.

def bounties(request):
    if request.user.is_authenticated:

        json_serializer = serializers.get_serializer("json")()
        bs = json_serializer.serialize(Bounty.objects.all(), ensure_ascii=False)
        context = {"bounties":bs}
        return render(request, 'bounties/bounties.html', context)

    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                Hunter.objects.create(user=user, name=username)

                log_in(request, user)
                json_serializer = serializers.get_serializer("json")()
                bs = json_serializer.serialize(Bounty.objects.all(), ensure_ascii=False)
                context = {"bounties":bs}
                return render(request, 'bounties/bounties.html', context)

        return render(request, 'bounties/register.html', {'form':UserCreationForm})

def account(request):
    you = ""
    hunters = [hunter for hunter in Hunter.objects.all()]
    for hunter in hunters:
        if hunter.name == request.user.username:
            you = hunter
    return render(request, 'bounties/account.html', {"hunter":you})    

def submit(request):
    
    form = SubmissionForm()

    if request.method == "POST":
        return render (request, 'bounties/submitted.html')

    return render(request, 'bounties/submit.html', {'form':form}) 

def submitted(request):
    return render(request, 'bounties/submitted.html')

def about(request):
    return render(request, 'bounties/about.html')

def contact(request):
    return render(request, 'bounties/contact.html')

def register(request):
    # create a User associated with a Hunter in a OneToOneField

    if request.method == "POST":
        # registered, add user, AND THEN login
        pass
    return render(request, 'bounties/register.html')

def register_sponsor(request):
    # create a User associated with an Organization in a OneToOneField
    pass

def login(request):
    # login the User (related to Hunter) to allow for full functionality
    pass

def login_sponsor(request):
    # login the User (related to Organization) to allow 
    pass

def sponsor(request):
    # post method sends transaction, shows sponsor's balance
    pass

def add_bounty(request):
    pass

def logout(request):
    log_out(request)
    return render(request, "bounties/logged_out.html")

def add_bounty(request):
    if request.method == "POST":
        form = BountyForm(request.POST)

        you = ""
        hunters = [hunter for hunter in Hunter.objects.all()]
        for hunter in hunters:
            if hunter.name == request.user.username:
                you = hunter

        form.hunter = hunter
        if form.is_valid():
            form.save()
            json_serializer = serializers.get_serializer("json")()
            bs = json_serializer.serialize(Bounty.objects.all(), ensure_ascii=False)
            context = {"bounties":bs}
            return render(request, 'bounties/bounties.html', context)
    else:    
        return render(request, "bounties/create.html", {'form':BountyForm()})