from django.contrib import admin
from .models import Question,Choice

admin.site.site_header="Pollster Admin"
admin.site.site_title="Polster Admin Area "
admin.site.index_title = "Welcome to pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [(None,{'fields':['questions_txt']}),
    ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines=[ChoiceInline]
#admin.site.register(Choice)
#admin.site.register(Question)
admin.site.register(Question,QuestionAdmin)