from django.contrib import admin

from todos.models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    '''Admin View for Todo'''

    list_display = ('name','description','isFinished')