from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Index, name="index"),
    path("register", Register, name="register"),
    path("registration", registeration, name="registration"),
    path("user_login", user_login , name="user_login"),
    path("add_book", add_book, name="add_book"),
    path("book_list", book_list, name="book_list"),
    path("borrow", add_borrower ,name="borrow"),
    path('return_book/<int:pk>/', return_book, name='return_book'),
    path("view_pdf/<int:pk>", view_pdf, name="view_pdf"),
    path("signout", signout, name="signout")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)