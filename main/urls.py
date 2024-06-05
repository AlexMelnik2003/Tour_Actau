from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  path('', views.index, name='main'),
                  path('tour_list/', views.tour_list, name='tour_list'),
                  path('tour_detail/<int:pk>/', views.tour_detail, name='tour_detail'),
                  path('contact/', views.contact, name='contact'),
                  path('faq/', views.faq_view, name='faq'),
                  path('faq_success/', views.faq_success, name='faq_success'),
                  path('tour/<int:pk>/book/', views.book_tour, name='book_tour'),
                  path('booking_success/', views.booking_success, name='booking_success'),
                  path('category/<int:category_id>/', views.tours_by_category, name='tours_by_category'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
