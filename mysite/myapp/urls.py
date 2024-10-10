from django.urls import path
from myapp.views import index, index_item

app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('<int:id>/', index_item,name='detail'),
]

