from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def scrape(request):
    page = requests.get('https://google.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    links = []
    for a in soup.find_all('a'):
        links.append(a.get('href'))
    
    return render(request, 'scraper/result.html', {'links':links})