from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges_to = {
    "january": "Complete a 30-day fitness challenge.",
    "february": "Read one book on personal development.",
    "march": "Start a new hobby and practice it daily.",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Write a daily journal entry.",
    "august": "Meditate for 10 minutes every day.",
    "september": "Declutter and organize one area of your home.",
    "october": "Try a new recipe every week.",
    "november": "Volunteer for a local charity or cause.",
    "december": None
}


def index(request):
    months = list(monthly_challenges_to.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_to.keys())
    if month >len(months):
        return HttpResponseNotFound("this does not exists")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_to[month]
        return render(request, "challenges/challenge.html" ,{
            "text" : challenge_text,
            "month_key" : month
        }) 
    except:
        raise Http404()

