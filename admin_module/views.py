from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Student, BorrowedBook



# Custom authorization check for admin users
def admin_check(user):
    return user.is_superuser


def main(request):
    return render(request, 'main.html')


def admin_dashboard(request):
    borrowed_books = BorrowedBook.objects.all()
    all_books = Book.objects.all()
    all_users = Student.objects.all()
    context = {
        'borrowed_books': borrowed_books,
        'all_books': all_books,
        'all_users': all_users,
    }
    return render(request, './main.html', context)


@user_passes_test(admin_check)
def search_student(request):
    results = []
    student_name = request.GET.get('student_name', '').strip()

    if student_name:  # Only perform the search if there's a name provided
        # Search by first name or last name
        results = Student.objects.filter(
            username__icontains=student_name
        )

    return render(request, 'search_results.html', {'results': results, 'student_name': student_name})


@user_passes_test(admin_check)
def find_student(request):
    return render(request, 'search_student.html')


def about(request):
    return render(request,'/about.html')

def contact(request):
    return render(request,'/contact.html')