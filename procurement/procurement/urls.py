from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'procurement.views.home', name='home'),
    url(r'^all/$', 'orders.views.all_orders', name='all_orders'),
    #url(r'^add_company/$', 'customers.views.add_company_details', name='add_company_details'),
    url(r'^subscribe/$', 'customers.views.subscribe', name='subscribe'),
    url(r'^account_type/$', 'customers.views.account_type', name='account_type'),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^bid/(?P<order_slug>.*)/$', 'bids.views.bid', name='bid'),
    url(r'^view_order/(?P<slug>.*)/$', 'orders.views.view_order', name='view_order'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += patterns('',) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

