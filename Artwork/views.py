from django.shortcuts import render
from .models import Artwork
from .forms import ArtworkForm
# Create your views here.
def showArtwork(request):
    artwork = Artwork.objects.all()

    context = {
        'all_artwork': artwork
    }
    return render(request, 'Artwork/showArtwork.html', context)

def insertArtwork(request):
    message = ""
    form = ArtworkForm()

    if request.method == "POST":
        form = ArtworkForm(request.POST,request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            artwork= form.save(commit=False)

            artwork.user = request.user
            artwork.save()
            message = "Artwork is submitted to DB. You can submit a new artwork now"
            form = ArtworkForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Artwork/insertArtwork.html', context)