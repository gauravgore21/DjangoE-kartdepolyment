from ecomapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product',views.product),
    path('login',views.Login),
    path('ragister',views.ragister),
    path('logout',views.user_logout),
    path('product_detail/<id>',views.product_detail),
    path('catfilter/<cid>',views.catfilter),
    path('sortfilter/<sv>',views.sortfilter),
    path('pricefilter',views.pricefilter),
    path('search',views.search),
    path('addtocart/<id>',views.addtocart),
    path('viewcart',views.viewcart),
    path('remove/<cid>',views.removecart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('pay_success',views.pay_success),
    path('about',views.about),
    path('contact',views.contact),

]
#image url
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
