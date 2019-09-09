from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website import views

urlpatterns = [
    url(r'^$', 'website.views.home', name='home'),
    url(r'^clubs/aero_modelling$', 'website.views.amc', name='amc'),
    url(r'^clubs/astronomy$', 'website.views.astro', name='astro'),
    url(r'^clubs/cops$', 'website.views.cops', name='cops'),
    url(r'^clubs/csi$', 'website.views.csi', name='csi'),
    url(r'^clubs/robotics$', 'website.views.robotics', name='robotics'),
    url(r'^clubs/sae$', 'website.views.sae', name='sae'),
    url(r'^clubs/biz$', 'website.views.biz', name='biz'),
    url(r'^clubs/inventory$', 'website.views.inventory', name='inventory'),
    url(r'^tac$', 'website.views.inventory', name='tac'),
    url(r'^others/bigbook$', 'website.views.inventory', name='bigbook'),
    url(r'^others/team$', 'website.views.team', name='team'),
    url(r'^others/learning$', 'website.views.learning', name='learning'),
    url(r'^app/$', 'website.views.app', name='app'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
