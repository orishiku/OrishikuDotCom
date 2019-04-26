from django.utils import timezone
from django.contrib import admin
from OBlog.models import Post,Tag, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','status', 'edit_date', 'permalink']
    readonly_fields = ['creation_date', 'edit_date', 'publish_date']
    
    def save_model(self, request, obj, form, change):
        old_obj = Post.objects.filter(pk=obj.pk)
        
        if len(old_obj)>0:
            if obj.status =='p' and (old_obj.last().status !='p' or obj.publish_date==None):
                obj.publish_date = timezone.now()
        else: 
            if obj.status =='p':
                obj.publish_date = timezone.now()
                
        if obj.author is None:
            obj.author = request.user
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']