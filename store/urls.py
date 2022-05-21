from django.urls import re_path

from .views import (
    create_email,
)

app_name = 'store'

urlpatterns = [

    re_path(r'^email_send/', create_email, name='create_book_normal'),

]
