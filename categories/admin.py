from django.contrib import admin
from .models import Category, Question


# Register your models here.

class QuestionsInline(admin.TabularInline):
    model = Question

class CategoryAdmin(  admin.ModelAdmin):
    inlines = [QuestionsInline]

admin.site.register(Category, CategoryAdmin)



