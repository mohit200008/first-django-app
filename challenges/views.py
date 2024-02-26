from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This is a January Task!",
    "february": "This is a February Task!",
    "march": "This is a March Task!",
    "april": "This is a April Task!",
    "may": "This is a May Task!",
    "june": "This is a June Task!",
    "july": "This is a July Task!",
    "august": "This is a August Task!",
    "september": "This is a September Task!",
    "october": "This is a October Task!",
    "november": None,
    "december": "This is a December Task!"
}


# Create your views here.

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())

  return render(request, "challenges/index.html", {
      "months": months
  })

def monthly_challenge_by_numbers(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge,
            "month": month
        })
    except:
        raise Http404() 
        
