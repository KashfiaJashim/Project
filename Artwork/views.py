from django.shortcuts import render, redirect, get_object_or_404
from .models import Artwork
from .forms import ArtworkForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def showArtwork(request):
    artwork = Artwork.objects.all()
    if request.method == 'POST':
        title = Artwork.objects.filter(title__icontains=request.POST['search'])
        category = Artwork.objects.filter(category__icontains=request.POST['search'])

        artwork = title | category

    context = {
        'all_artwork': artwork
    }
    return render(request, 'Artwork/showArtwork.html', context)

@login_required
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

def showDetails(request, artwork_id):

    searched_artwork = get_object_or_404(Artwork, id=artwork_id)
    context = {
        'search': searched_artwork,

    }
    return render(request, 'Artwork/show_artwork_details.html', context)
