#pages/views.py
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    
class AboutPageView(TemplateView): #new
    template_name = "about.html"