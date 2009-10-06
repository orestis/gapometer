from django.conf.urls.defaults import url, patterns
from django.views.generic.list_detail import object_list, object_detail

from promises.models import Promise

urlpatterns = patterns('',
    url(r'^$', object_list,
        {
            "template_name": "promises/promises_list.html",
            "queryset": Promise.objects.all(),
        },
        name="promise_list"),
    
    url(r'^promise/(?P<object_id>\d+)/$', object_detail,
        {
            "template_name": "promises/promise_detail.html",
            "template_object_name": "promise",
            "queryset": Promise.objects.all(),
        },
        name="promise_detail"),
)

