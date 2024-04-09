from django.contrib import admin
from .models import Booking, Menu
# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
# Path: littelemon\restaurant\models.py
# Compare this snippet from littelemon\restaurant\views.py:
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import menu
#
# # Create your views here.
#   
# def index(request):
#     return HttpResponse("Hello, world. You're at the restaurant index.")


# def menu(request):
#     menu_list = menu.objects.all()

#     context = {

#         'menu_list': menu_list
#     }

#     return render(request, 'restaurant/menu.html', context)
# Path: littelemon\restaurant\views.py
# Compare this snippet from littelemon\restaurant\urls.py:
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('menu/', views.menu, name='menu'),
# ]
# Path: littelemon\restaurant\urls.py
# Compare this snippet from littelemon\restaurant\templates\restaurant\menu.html:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Menu</title>
# </head>
# <body>
#     <h1>Menu</h1>
#     <ul>
#         {% for item in menu_list %}
#             <li>{{ item.Tittle }} - {{ item.Price }}</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>
# Path: littelemon\restaurant\templates\restaurant\menu.html
# Compare this snippet from littelemon\littelemon\urls.py:
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('restaurant/', include('restaurant.urls')),
#     path('admin/', admin.site.urls),
# ]
# Path: littelemon\littelemon\urls.py
# Compare this snippet from littelemon\restaurant\templates\restaurant\menu.html:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Menu</title>
# </head>
# <body>
#     <h1>Menu</h1>
#     <ul>
#         {% for item in menu_list %}
#             <li>{{ item.Tittle }} - {{ item.Price }}</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>
# Path: littelemon\restaurant\templates\restaurant\menu.html
# Compare this snippet from littelemon\restaurant\views.py:
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import menu
#
# # Create your views here.
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the restaurant index.")

# def menu(request):
#     menu_list = menu.objects.all()

#     context = {

#         'menu_list': menu_list
#     }

#     return render(request, 'restaurant/menu.html', context)
# Path: littelemon\restaurant\views.py
# Compare this snippet from littelemon\restaurant\urls.py:
# from django.urls import path

# from . import views
