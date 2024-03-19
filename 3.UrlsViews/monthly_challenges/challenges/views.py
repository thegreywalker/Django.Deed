from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk atleast for 20 min for every day!" ,
    "march": "Learn Django for atleast 20 mins every day!",
    "april": "Try try but don't cry!",
    "may": "It's that time of the month!",
    "june": "Time to give semester exams",
    "july": "It's now time to open a book store.",
    "august": "Hope, I have saved enough money!",
    "september": "I buy my first car & my birthday",
    "october": "Driving the Car to College & expanding my business revenue.",
    "november": "My book store is running awesome and I am earning 60k per month from it.",
    "december": "Time to bid good bye to this year again."
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        redirect_path = reverse("Monthly_Challenges", args=[month])
        list_items += f"<li><a href=\"{redirect_path}\">{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    if month > len(monthly_challenges.keys()):
        return HttpResponseNotFound("<h1>Invalid Month!!</h1>")

    redirect_month = list(monthly_challenges.keys())[month - 1]
    redirect_path = reverse("Monthly_Challenges", args=[redirect_month]) # /challenges/<month_name>
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month: str):
    try:
        challenge_text=monthly_challenges[month.casefold()]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!!</h1>")

