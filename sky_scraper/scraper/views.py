from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Link

# Create your views here.

def scrape(request):
    page = requests.get('https://google.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    for a in soup.find_all('a'):
        address = a.get('href')
        name = a.text.strip()
        Link.objects.create(address=address, name=name)
    
    links = Link.objects.all()
    if links:
        Link.objects.all().delete()
        
    return render(request, 'scraper/result.html', {'links':links})