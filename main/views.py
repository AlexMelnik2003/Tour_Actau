from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_date

from .forms import BookingForm, FaqForm
from .models import Tour, Book_list, TourImage, Category, TourVideo


def index(request):
    tours = Tour.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/main.html', {'tours': tours, 'categories': categories})


def tour_list(request):
    tours = Tour.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/tour_list.html', {'tours': tours, 'categories': categories})


def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    is_booked = False
    if request.user.is_authenticated:
        is_booked = Book_list.objects.filter(user=request.user, tour=tour).exists()
    tour_images = TourImage.objects.filter(tour=tour)
    tour_videos = TourVideo.objects.filter(tour=tour)
    return render(request, 'main/tour_detail.html',
                  {'tour': tour, 'is_booked': is_booked, 'tour_images': tour_images, 'tour_videos': tour_videos})


def contact(request):
    return render(request, 'main/contact.html')




def faq_view(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()
            return redirect('tour_list')
    else:
        form = FaqForm()
    return render(request, 'main/faq.html', {'form': form})


def book_tour(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.tour = tour
            booking.is_paid = False

            # Обрабатываем поле даты
            book_data = request.POST.get('book_data')
            if book_data:
                booking.book_data = parse_date(book_data)

            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/book_tour.html', {'form': form, 'tour': tour})


def booking_success(request):
    return render(request, 'booking/booking_success.html')


def tours_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tours = Tour.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'main/tour_list.html',
                  {'tours': tours, 'categories': categories, 'selected_category': category})
