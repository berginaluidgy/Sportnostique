from.views import home,RegisterApi,loginApi,Userpage,payment,paymentmoncash,getpronos,adm,updatechecking,updating,admin_get_Unique_user
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',home ),
    path('signup',RegisterApi.as_view()),
    path('login',loginApi.as_view()),
    path('Users',Userpage),
    path('payment',payment),
    path('pay',paymentmoncash),
    path('Pronos/<int:id>/<int:idleague>',getpronos),
    path('Superuser',adm),
    path('checking/<str:data>',updatechecking),
    path('updating/<int:pk>',updating.as_view()),
    path('getuser/<str:name>',admin_get_Unique_user),
    # path('login',login)
]

urlpatterns +=staticfiles_urlpatterns()