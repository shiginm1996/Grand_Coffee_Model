from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(sregmodelview)
admin.site.register(itemup)
admin.site.register(buyerregmodel)
admin.site.register(wishlist)
admin.site.register(cart)
admin.site.register(delivery)
admin.site.register(confirmmodel)
admin.site.register(cart_details)
admin.site.register(cardmodel)
admin.site.register(place_order)

