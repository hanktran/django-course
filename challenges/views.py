from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
  'january': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'february': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'march': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'april': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'may': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'june': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'july': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'august': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'september': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'october': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'november': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
  'december': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales arcu suscipit dignissim venenatis.',
}

def index(request):
  months = list(monthly_challenges.keys())

  return render(request, "challenges/index.html", {
    "months": months
  })

def monthly_challenge_number(request, month):
  months = list(monthly_challenges.keys())
  
  if month > len(months):
    return HttpResponseNotFound("Invalid month")

  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request ,"challenges/challenge.html", {
      "text": challenge_text,
      "month_name": month
    })
  except:
    raise Http404()