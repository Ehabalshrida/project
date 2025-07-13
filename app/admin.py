from django.contrib import admin
from . import models
# Customize the admin interface
admin.site.site_header = "My Django App Admin"

# Register your models here. to show on admin dashboard
# admin.site.register(models.User)

# to customize the admin interface for the User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'number')
    search_fields = ('first_name', 'last_name')
    list_filter = ('age','number')  # Add filters for age and number fields
    ordering = ('-age',)  # Order by age descending
    list_per_page = 10  # Number of items per page in the admin list view
admin.site.register(models.User, UserAdmin)

admin.site.register(models.Genre)
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Language)
admin.site.register(models.BookInstance)
