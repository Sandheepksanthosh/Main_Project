from django.urls import path
from Frontend import views
urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
    path('aboutuspage/', views.aboutuspage, name="aboutuspage"),
    path('bikespage/', views.bikespage, name="bikespage"),
    path('servicespage/', views.servicespage, name="servicespage"),
    path('bikesingle/<int:proid>/', views.bikesingle, name="bikesingle"),
    path('savetrip/', views.savetrip, name="savetrip"),
]