from django.contrib import admin

# Register your models here.

from .models import Role, Item, Machine, User, Fabrication, SubAssembly, Assembly, SubProcess, AssemblyProcess

admin.site.register(Role)
admin.site.register(Item)
admin.site.register(User)
admin.site.register(Machine)
admin.site.register(Fabrication)
admin.site.register(SubAssembly)
admin.site.register(Assembly)
admin.site.register(SubProcess)
admin.site.register(AssemblyProcess)
