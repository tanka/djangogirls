from django.contrib import admin
from .models import Tourgroup, Guestcategory, Guest, Expense, People, TourgroupPeople

admin.site.register(Tourgroup)
admin.site.register(Guestcategory)
admin.site.register(Guest)
admin.site.register(Expense)
admin.site.register(People)
admin.site.register(TourgroupPeople)