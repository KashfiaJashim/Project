from django.shortcuts import render
from .models import Artwork
# Create your views here.
def showArtwork(request):
    artwork = Artwork.objects.all()

    context = {
        'all_artwork': artwork
    }
    return render(request, 'Artwork/showArtwork.html', context)