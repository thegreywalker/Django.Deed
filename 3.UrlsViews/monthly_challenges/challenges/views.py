from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk atleast for 20 min for every day!")

# def march(request):
#     return HttpResponse("Learn Django for atleast 20 mins every day!")

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month: str):
    challenge_text=None
    if month.casefold() == "january".casefold():
        challenge_text = "Eat no meat for the entire month!"
    elif month.casefold() == "february".casefold():
        challenge_text = "Walk atleast for 20 min for every day!"
    elif month.casefold() == "march".casefold():
        challenge_text = "Learn Django for atleast 20 mins every day!"
    else:
        return HttpResponseNotFound("This month is not supported!!")

    return HttpResponse(challenge_text)

