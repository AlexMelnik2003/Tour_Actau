from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to='destination/')

    def __str__(self):
        return self.name


class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tour_detail_imаge/')
    book_data = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.destination.name} - {self.price}'


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tour_detail_imаge/')


class TourVideo(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='tour_videos/')


class Book_list(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    book_data = models.DateField()
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    number_phone = models.IntegerField()

    def __str__(self):
        return f'{self.tour} - {self.user.username}'


class Booking(models.Model):
    book = models.OneToOneField(Book_list, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)


class Faq(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    questions = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.questions}'
