from django.contrib import admin

from .models import Choice, Question

admin.site.site_header = "Pollester Admin"
admin.site.site_title = "Polling Admin Area"
admin.site.index_title = "Welcome to Pollester Area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information',
                                                         {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
