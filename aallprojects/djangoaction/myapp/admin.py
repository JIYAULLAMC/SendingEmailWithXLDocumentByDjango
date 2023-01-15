from django.contrib import admin

# Register your models here.
from myapp.models import Article
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib.auth.forms import AuthenticationForm, UsernameField



@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

from django.core import serializers
from django.http import HttpResponse

@admin.action(description='export as json')
def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

@admin.action(description='export_selected_objects')
def export_selected_objects(modeladmin, request, queryset):
    selected = queryset.values_list('pk', flat=True)
    ct = Article.objects.get_for_model(queryset.model)
    return HttpResponseRedirect('/export/?ct=%s&ids=%s' % (
        ct.pk,
        ','.join(str(pk) for pk in selected),
    ))


# class MyAction():
#     def action(self, *args, **kwargs):
#         print("hiii")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published, 'make_draft', export_as_json, export_selected_objects,]

    @admin.action(description='Mark selected stories as draft')
    def make_draft(self, request, queryset):
        updated = queryset.update(status='d')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    


admin.site.disable_action('delete_selected')
admin.site.register(Article, ArticleAdmin)