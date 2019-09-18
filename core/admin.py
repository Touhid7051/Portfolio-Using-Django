from django.contrib import admin

from .views import *

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
admin.site.register(Contact)

#Regiatering tittlefield

admin.site.register(aboutTitle)
admin.site.register(serviceTitle)
admin.site.register(portfolioTitle)
admin.site.register(testimonialTitle)
admin.site.register(contactTitle)
admin.site.register(adressTitle)





