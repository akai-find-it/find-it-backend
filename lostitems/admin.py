from django.contrib import admin

from .models import Answer, LostItem , Question
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer

class LostItemAdmin(admin.ModelAdmin):
    inlines = [
            AnswerInline
            ]


admin.site.register(LostItem, LostItemAdmin)
