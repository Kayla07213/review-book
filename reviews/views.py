from django.shortcuts import render
from django.shortcuts import redirect
from reviews.forms import ReviewForm 
from reviews.models import Review


def reviews(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name') 
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating') 
            Review.objects.create(name=name, email=email, review=review, rating=rating)
            
    
    form = ReviewForm()
    reviews=Review.objects.all()
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})