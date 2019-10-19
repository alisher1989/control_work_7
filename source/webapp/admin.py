from django.contrib import admin
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created_at']
    list_filter = ['question']
    list_display_links = ['pk', 'question']
    search_fields = ['question', 'created_at']
    fields = ['question', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)