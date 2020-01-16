from django.shortcuts import render
from . models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="Bali"
    dest1.desc="Bali is a province of Indonesia and the westernmost of the Lesser Sunda Islands. island of Bali and a few smaller neighbouring islands."
    dest1.image="destination_1.jpg"
    dest1.price=800

    dest2 = Destination()
    dest2.name = "Indonesia"
    dest2.desc = "Indonesia, country located off the coast of mainland Southeast Asia in the Indian and Pacific oceans. "
    dest2.image = "destination_2.jpg"
    dest2.price = 900

    dest3 = Destination()
    dest3.name = "San Francisco"
    dest3.desc = "Golden Gate Bridge is a suspension bridge across the place the where San Francisco Bay opens into the Pacific Ocean, so-called Golden Gate (hence the name)."
    dest3.image = "destination_3.jpg"
    dest3.price = 1200

    dest4 = Destination()
    dest4.name = "Paris"
    dest4.desc = "Paris, city and capital of France, situated in the north-central part of the country. People were living on the site of the present-day city."
    dest4.image = "destination_4.jpg"
    dest4.price = 1500

    dest5 = Destination()
    dest5.name = "Maldives"
    dest5.desc = "Maldives. Maldives, in full Republic of Maldives, also called Maldive Islands, independent island country in the north-central Indian Ocean."
    dest5.image = "destination_5.jpg"
    dest5.price = 1000

    dest6 = Destination()
    dest6.name = "Mykonos"
    dest6.desc = "Mykonos. Welcome to Greece's most famous cosmopolitan island, a whitewashed paradise in the heart of the Cyclades."
    dest6.image = "destination_6.jpg"
    dest6.price = 1800
    dests=[dest1,dest2,dest3,dest4,dest5,dest6]
    return render(request,'travello/index.html',{'dests':dests})

def about(request):
    return render(request,'travello/about.html')
def contact(request):
    return render(request,'travello/contact.html')
def destinations(request):
    return render(request,'travello/destinations.html')
def elements(request):
    return render(request,'travello/elements.html')
def news(request):
    return render(request,'travello/news.html')


