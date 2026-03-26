from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import FileResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Borrower
from datetime import datetime, date, timedelta
from django.utils import timezone

def Index(request):
    return render(request, "app/login.html")

def Register(request):
    return render(request, "app/register.html")

def registeration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('index')

    return render(request, 'registration.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('book_list')
    return render(request, 'app/login.html')

@login_required(login_url="index")
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publication_date = request.POST['publication_date']
        image = request.FILES.get('image')
        book_upload = request.FILES.get('book_upload')

        book = Book.objects.create(
            user=request.user,
            title=title,
            author=author,
            publication_date=publication_date,
            image=image,
            book_upload=book_upload
        )
        return redirect('book_list')
    return render(request, 'app/add_book.html')

@login_required(login_url="index")
def book_list(request):
    books = Book.objects.all()
    query = request.GET.get('search')
    
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    return render(request, 'app/home.html', {'books': books})

# @login_required(login_url="index")
# def add_borrower(request):
#     if request.method == 'POST':
#         book_select = request.POST['book_select']
#         name = request.POST['name']
#         department = request.POST['department']

#         borrow_date = date.today()
#         fine = calculate_fine(borrow_date)

#         book_entry = Borrower.objects.create(
#             book_id=book_select,
#             name=name,
#             department=department,
#             borrow_date=borrow_date,
#             fine=fine
#         )

#         return redirect('borrow')
    
#     books = Book.objects.all()
#     borrows = Borrower.objects.all()

#     return render(request, 'app/showed_borrowed_mgmt.html', {"books": books, "borrows": borrows})

@login_required(login_url="index")
def add_borrower(request):
    if request.method == 'POST':
        book_select = request.POST['book_select']
        name = request.POST['name']
        department = request.POST['department']

        borrow_date = date.today()
        fine = calculate_fine(borrow_date)

        Borrower.objects.create(
            book_id=book_select,
            name=name,
            department=department,
            borrow_date=borrow_date,
            fine=fine
        )

        return redirect('borrow')

    books = Book.objects.all()
    borrows = Borrower.objects.all()
    return render(request, 'app/showed_borrowed_mgmt.html', {
        "books": books,
        "borrows": borrows
    })



# @login_required(login_url="index")
# def calculate_fine(borrow_date):
#     fine_per_day = 5
#     days_difference = (date.today() - borrow_date).days

#     if days_difference > 5:
#         fine = fine_per_day * (days_difference - 5)
#     else:
#         fine = 0

#     return fine

def calculate_fine(borrow_date):
    fine_per_day = 5
    days_difference = (date.today() - borrow_date).days

    if days_difference > 5:
        fine = fine_per_day * (days_difference - 5)
    else:
        fine = 0

    return fine


@login_required(login_url="index")
def return_book(request, pk):
    borrower = get_object_or_404(Borrower, pk=pk)

    if request.method == 'POST':
        if borrower.returned == 'No': 
            borrower.fine = 0
            borrower.returned = 'Yes'
            borrower.save()

    return redirect('borrow')

@login_required(login_url="index")
def view_pdf(request, pk):
    book = get_object_or_404(Book, pk=pk)
    file_path = book.book_upload.path
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

@login_required(login_url="index")
def signout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
        


