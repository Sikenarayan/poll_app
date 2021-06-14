from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), 
                 
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


# admin.site.register(Question)
# admin.site.register(Choice)
