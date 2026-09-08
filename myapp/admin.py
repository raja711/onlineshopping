from django.contrib import admin
from .models import registertbl  # अपने मॉडल का सही नाम यहाँ लिखें

# मॉडल को एडमिन पैनल में रजिस्टर करें
admin.site.register(registertbl)

from django.contrib import admin
from .models import Product

# एडमिन पैनल में दिखाने के लिए रजिस्टर करें
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

    from django.contrib import admin
    from .models import Contact

    @admin.register(Contact)
    class ContactAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'subject', 'created_at')
        search_fields = ('name', 'email', 'subject')