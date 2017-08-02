# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import UserAddress


# Adds the useraddress to the admin panel
class UserAddressAdmin(admin.ModelAdmin):

    # Links this to the UserAddress model
    model = UserAddress

    # The list of what needs to be displayed
    list_display = [
        "first_name",
        "last_name",
        "address_1",
        "address_2",
        "city",
        "state",
        "country",
        "created_at",
    ]

    # The order that the items should be listed (By the creation date)
    ordering = ("-created_at", )


    def get_name(self, obj):
        return obj.author.name
    get_name.admin_order_field = 'address'  # Allows column order sorting
    get_name.short_description = 'Registered Address'  # Renames column head


# Register your models here.
admin.site.register(UserAddress, UserAddressAdmin)

# Remove the other default registered items
admin.site.unregister(User)
admin.site.unregister(Group)
