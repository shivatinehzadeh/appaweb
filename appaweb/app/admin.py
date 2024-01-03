from django.contrib import admin
from .models import Post,Order,Package,OnlineLearn,Profile,Sell,SellOnline,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
   list_display = ('title',)
   list_filter = ('title',)
   search_fields = ('title','content')
admin.site.register(Post,PostAdmin)



class PostAdmin(admin.ModelAdmin):
   list_display = ('name',)
   list_filter = ('name',)
   search_fields = ('name',)
admin.site.register(Order,PostAdmin)



class PostAdmin(admin.ModelAdmin):
   list_display = ('title',)
   list_filter = ('title',)
   search_fields = ('title',)
admin.site.register(Comment,PostAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('title',)
   list_filter = ('title',)
   search_fields = ('title',)
admin.site.register(Package,PostAdmin)


class PostAdmin(admin.ModelAdmin):
   list_display = ('title',)
   list_filter = ('title',)
   search_fields = ('title',)
admin.site.register(OnlineLearn,PostAdmin)


class PostAdmin(admin.ModelAdmin):
 list_display=('user',)
admin.site.register(Profile,PostAdmin)

class PostAdmin(admin.ModelAdmin):
 list_display=('username','pub_date')
admin.site.register(Sell,PostAdmin)

class PostAdmin(admin.ModelAdmin):
 list_display=('username','pub_date')
admin.site.register(SellOnline,PostAdmin)