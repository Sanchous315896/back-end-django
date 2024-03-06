from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('update/', views),
    # path('movies/<str:id>/', views),
    path('showList/createAction/<str:pk>', views.createAction),
    path('showList/createAction/create/<str:pk>', views.create),
    path('showList/updateAction/<str:pk>', views.updateAction, name='update-action'),
    path('showList/updateAction/update/<str:pk>', views.update, name='update'),
    path('', views.main),

    path('showList/<str:pk>', views.showlist),
    path('showList/done/<str:pk>', views.done),

    path('createList/', views.createList),
    path('createList/create/', views.createListTotal),
    path('updateList/<str:pk>', views.updateList),
    path('updateList/update/<str:pk>', views.updateListTotal),
    path('doneList/<str:pk>', views.doneList),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
