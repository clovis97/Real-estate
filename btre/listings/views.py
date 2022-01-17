from django.shortcuts import render
from listings import models
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'templates/home.html')
def listings(request):
    listings = models.Listings.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    paged_listings = paginator.get_page('page')
    context = {
        'listings': paged_listings
    }
    return render(request, 'listing.html', context)
def listing(request, listing_id):
    return render(request, 'single_listing.html')

def search(request):
    return render(request, 'search.html')