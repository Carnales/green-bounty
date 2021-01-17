from django.shortcuts import render

# Create your views here.

def bounties(request):
    context = {}
    return render(request, 'bounties/bounties.html', context)