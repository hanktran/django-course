from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
  list_items = ""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)

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
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("This month is not supported!")