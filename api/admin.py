from django.contrib import admin
from .models import User,Location,Store,StoreCategory,Reviews,Country,Category
# Register your models here.
admin.site.register(User)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Store)
admin.site.register(Location)
admin.site.register(StoreCategory)