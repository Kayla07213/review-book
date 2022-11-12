from django.shortcuts import render
from django.shortcuts import redirect
from reviews.forms import ReviewForm 


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name') 
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating') 
            with open('data.csv', 'a') as file:
                file.write(f'{name}|{email}|{review}|{rating}\n') 
                return redirect('reviews')
    with open('data.csv') as file:
        reviews = file.readlines() 
        if len(reviews) > 0:
            review_data_1 = reviews[0]
            name_1 = review_data_1.split('|')[0]
            email_1 = review_data_1.split('|')[1]
            review_1 = review_data_1.split('|')[2]
        else:
            name_1 = ""
            email_1 = ""
            review_1 = "" 

    form = ReviewForm()
    return render(request, 'reviews.html', {'form': form, 'name_1': name_1, 'email_1': email_1, 'review_1': review_1})
