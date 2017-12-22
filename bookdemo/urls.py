from django.conf.urls import url
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$',views.index),
    url('^(\d+)/$',views.detail)
]