from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Food)
admin.site.register(Table)

