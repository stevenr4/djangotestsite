# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserAddress


class UserAddressAdmin(admin.ModelAdmin):
    model = UserAddress
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
    ordering = ("-created_at", )

    def get_name(self, obj):
        return obj.author.name
    get_name.admin_order_field  = 'address'  #Allows column order sorting
    get_name.short_description = 'Registrated Address'  #Renames column head


# Register your models here.
admin.site.register(UserAddress, UserAddressAdmin)
