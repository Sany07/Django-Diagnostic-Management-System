from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration,Vision,Mission,Center

admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Vision, SingletonModelAdmin)
admin.site.register(Mission, SingletonModelAdmin)
admin.site.register(Center, SingletonModelAdmin)