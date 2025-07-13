from django.shortcuts import render, redirect
from django.urls import reverse
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseNotFound,Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here. 
context = {
    'home': 'Hello, Django!',
    'about': 'About Page!'
}
def home(request):
    return HttpResponse(context['home'])
def about(request):
    return HttpResponse(context['about'])

def index(request, var):
    try:
       result=context[var]
       return HttpResponse(result)
    except:
        return HttpResponseNotFound("Page not found test")   
        # you can also raise an Http404 error to handle not found pages
        # raise Http404("Page not found")    
 
def math(request, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        eg= f"{num1} + {num2} = {result}"
        # return HttpResponse(f"The sum of {num1} and {num2} is {result}.")
        return HttpResponse(eg)

def pageNumber(request, pageNumber):
   listOfPages = list(context.keys())
   print(f"Requested page number: {pageNumber}")
   print(f"context.keys(): {context.keys()}")
   print(f"List of pages: {listOfPages}")
   # reverse depend on the url name, but redirect depends on the url path
   webPage= reverse('app:index', args=[listOfPages[pageNumber]])
   print(f"Web page URL: {webPage}")
   return HttpResponseRedirect(webPage)
   # return HttpResponseRedirect(listOfPages[pageNumber])
def homeTemplate(request):
    data = {
        'title': 'Home Page',
        'message': 'welcome to the Home Page!',
        'list': ['Item 1', 'Item 2', 'Item 3'],
        'grads':{
            'ar': 90,
            'cs': 85,
        } ,
        'value': 200,
    }
    return render(request, 'app/homeTemplate.html', {'context': data})
# class-based views.
from django.views import generic
class AboutTemplate(generic.TemplateView):
    template_name = 'app/aboutTemplate.html'  
# function-based views.       
def aboutTemplate(request):    
    return render(request, 'app/aboutTemplate.html')
def users(request):
    data = models.User.objects.all()
    return render(request, 'app/usersTemplate.html', {'users': data})
def addUser(request):
    print("Add User View Called", request,'method', request.method)
    if request.method == 'POST':
        user = models.User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], age=request.POST['age'])
        user.save() # Save the user to the database
        return redirect('app:users')
    else:
        return render(request, 'app/addUserTemplate.html')
def deleteUser(request):
    print("delete User View Called", request,'method', request.method)
    if request.method == 'POST':
        try:
           models.User.objects.get(id=request.POST['id']).delete()  # Delete the user with the given ID
           return redirect('app:users')
        except:
           return redirect('app:users')  # Redirect to users page if user not found or any error occurs
    else:
        return render(request, 'app/deleteUserTemplate.html')
# class-based view for handling form submission
class Form(generic.FormView):
    template_name = 'app/formTemplate.html'
    form_class = forms.UserForm
    success_url = '/app/users'  # Redirect to users page after successful form submission

    def form_valid(self, form):
        print("formData",form.cleaned_data) # print the cleaned data from the form
        return super().form_valid(form)  # Redirect to success_url
# function-based view for handling form submission
def form (request):
    print("Form View Called", request,'method', request.method)
    if request.method == 'POST':
        # form = forms.UserForm(request.POST)
        form = forms.UserModelForm(request.POST)
        if form.is_valid():
         print("Form is valid", form.cleaned_data)
        # to Save the form data to the database, use with ModelForm
         form.save()
        #  first_name = form.cleaned_data['first_name']
        #  last_name = form.cleaned_data['last_name']
        #  age = form.cleaned_data['age']
        #  number = form.cleaned_data['number']        
        #  print(f"First Name: {first_name}, Last Name: {last_name}, Age: {age}, Number: {number}")
         return redirect('app:users')
        else:
            print("Form is not valid", form.errors)
            return render(request, 'app/formTemplate.html', {'form': form})
    else:
        # form = forms.UserForm()
        form = forms.UserModelForm()
        return render(request, 'app/formTemplate.html', {'form': form})
# class-based view for handling ModelForm submission, and inserting data into the database     
class UserModelFormView(generic.CreateView):
    template_name = 'app/formTemplate.html'
    form_class = forms.UserModelForm
    success_url = '/app/users'  # Redirect to users page after successful form submission

    def form_valid(self, form):
        print("Form Data:", form.cleaned_data)  # Print the cleaned data from the form
        return super().form_valid(form)  # Redirect to success_url
# use class based view to list users    
class UserList (generic.ListView):
    template_name= 'app/usersLists.html'
    model= models.User
    context_object_name= 'users'    
    queryset= models.User.objects.all().order_by('age') # order by age
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderById'] = models.User.objects.all().order_by('id')
        return context

# use class based view to display user details
class UserDetail(generic.DetailView):
    template_name = 'app/userDetails.html'
    model = models.User
    context_object_name = 'user'  # This will be used in the template to access the user object
    # you can also override get_context_data method to add more context if needed
class UserUpdate (generic.UpdateView):
    model= models.User
    fields='__all__'
    template_name= 'app/formTemplate.html'
    context_object_name='user'
    success_url='/app/users'
class UserDelete (generic.DeleteView):
    model= models.User
    template_name= 'app/deleteUserTemplate.html'
    context_object_name='user'
    success_url='/app/users'
# for book app
def books(request):
    numberOfBooks = models.Book.objects.all().count()
    numberOfBooksInstances = models.BookInstance.objects.all().count()
    numberOfAvailableBooks = models.BookInstance.objects.filter(status__exact='a').count()  # Assuming 'a' is the status for available books
    print(f"Number of Books: {numberOfBooks}, Number of Book Instances: {numberOfBooksInstances}, Number of Available Books: {numberOfAvailableBooks}")
    return render(request, 'app/booksTemplate.html',  {'numberOfAvailableBooks': numberOfAvailableBooks, 'numberOfBooks': numberOfBooks, 'numberOfBooksInstances': numberOfBooksInstances})
# @login_required used with function-based views
# LoginRequiredMixin is used with class-based views, and has same effect as @login_required decorator, will prevent
# unauthenticated users from accessing the view, and redirect them to the login page.
class CreateBook(LoginRequiredMixin, generic.CreateView):
    model = models.Book
    fields = '__all__'
    template_name = 'app/formTemplate.html'
    success_url = '/app/books'  # Redirect to books page after successful form submission

    def form_valid(self, form):
        print("Form Data:", form.cleaned_data)  # Print the cleaned data from the form
        return super().form_valid(form)  # Redirect to success_url

class BookDetails(generic.DetailView):
    template_name = 'app/bookDetails.html'
    model = models.Book
    context_object_name = 'book'  # This will be used in the template to access the user object
    # you can also override get_context_data method to add more context if needed
class Register( generic.CreateView):
    form_class = UserCreationForm  # Use Django's built-in UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login'  # Redirect to books page after successful form submission
