from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'  # Optional: to namespace the app's URLs
urlpatterns = [
    # path('home', views.home, name='home'),
    # path('about', views.about, name='about'),
    # path('<int:pageNumber>', views.pageNumber, name='pageNumber'),
    # path('<str:var>', views.index, name='index'),
    # path('<int:num1>/<int:num2>', views.math, name='math'),
    # path('home', views.homeTemplate, name='home'),
    # function-based views.
    # path('about', views.aboutTemplate, name='about'),
    path('books', views.books, name='books'),
    path('create-book', views.CreateBook.as_view(), name='createBook'),
    path('detail-book/<int:pk>', views.BookDetails.as_view(), name='detailsBook'),

    # class-based view
    path('about', views.AboutTemplate.as_view(), name='about'),
    path('users', views.users, name='users'),
    path('add', views.addUser, name='addUser'),
    path('delete', views.deleteUser, name='deleteUser'),
    path('', views.homeTemplate, name='home'),
    # function-based view
    # path('form', views.form, name='form'),
    # class-based view
    # path('form', views.Form.as_view(), name='form'),
    # class-based view for handling form submission, and create a user at database
    path('form', views.UserModelFormView.as_view(), name='form'),
    # class-based view for rendering users from database
    path('list', views.UserList.as_view(), name='list'),
    path('user-details/<int:pk>', views.UserDetail.as_view(), name='userDetails'),
    path('user-update/<int:pk>', views.UserUpdate.as_view(), name='userUpdate'),
    path('user-delete/<int:pk>', views.UserDelete.as_view(), name='userDelete'),
    path('accounts/register', views.Register.as_view(), name='register'),
    path('accounts/change-password', auth_views.PasswordChangeView.as_view(template_name='registration/changePassword.html', success_url='/accounts/login'), name='changePassword'),

]
