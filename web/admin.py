from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django import forms
from .models import posts,requests,font
# Register your models here.



class postsForm(forms.ModelForm):
    quickdes = forms.CharField(label="quickDescription(max :30 hint: antivirus softwear)",max_length=60, widget=forms.Textarea(attrs={"cols":50,"rows":2}) )
    class Meta:
        model = posts
        fields ="__all__"

class PostsAdmin(admin.ModelAdmin):
    form = postsForm
    list_display = ('username_id','catagorye','title','version','date_and_time',)
    fieldsets = (
        (None, {
            'fields': ('username_id', 'title','image', 'catagorye','quickdes')
        }),
        ('Advanced options', {
            'classes': ('wide',),
            'fields': ('description',),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget':CKEditorWidget()},
        
    }
    list_filter = ("username_id",)

class RequestsAdmin(admin.ModelAdmin):
    list_display = ('username_id','product_name')
    list_display_links = ('product_name',)
    list_filter = ("username_id",)




admin.site.register(posts,PostsAdmin)
admin.site.register(requests,RequestsAdmin)
admin.site.register(font)
admin.site.site_header = 'Welcome Admin pannel (this is only staf users)'
admin.site.site_title= "Admin Pannel"

