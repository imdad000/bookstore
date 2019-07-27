from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'bookapp'
urlpatterns = [
	path('',views.home_page,name='home_page'),
	path('details/<int:pk>', views.update_book, name='update_book'),
	path('delete/<int:pk>', views.delete_book, name='delete_book'),

]