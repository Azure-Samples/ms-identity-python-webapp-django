"""View(s) in this file does NOT rely on settings.AUTH,
so that a post_logout view can be imported by settings.py without cyclic import.
"""
from django.http import HttpResponse

def post_logout(request):
    return HttpResponse("You have logged out successfully.")
