from django.contrib import admin

# Register your models here.
from .models import House, Community

class CommunityAdmin(admin.ModelAdmin):

    
    list_display = ('name', 'city', )

    
    list_per_page = 10

   
    list_editable = ('city',)

    
    ordering = ('-mod_date',)



class HouseAdmin(admin.ModelAdmin):

  
    fields = ('description', 'community', 'bedroom', 'direction', 'floor', 'area', 'price', )


    list_display = ('description', 'community', 'price', 'bedroom', 'direction', 'floor', 'area', 'area_class', )

  
    list_filter = ('bedroom', 'direction', 'floor', 'area_class')

   
    list_per_page = 10

    
    list_editable = ('bedroom', 'direction', 'floor', 'area_class',)

   
    raw_id_fields = ('community',)

    
    ordering = ('-mod_date',)


admin.site.register(Community, CommunityAdmin)
admin.site.register(House, HouseAdmin)