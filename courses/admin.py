from django.contrib import admin
from .models import Subject, Course,Module
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}

class ModuleInline(admin.StackedInline):
    model = Module
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepupulated_fields = {'slug': ('title', )}
    inlines = [ModuleInline]


# python manage.py dumpdata courses --indent=2  --output=courses/fixtures/subjects.json

admin.site.index_template = 'memcache_status/admin_index.html'