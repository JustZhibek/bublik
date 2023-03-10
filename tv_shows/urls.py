from django.urls import path
from tv_shows import views

urlpatterns = [
    # path('tvshow/', views.tv_showview, name='show'),
    path("tvshow/", views.TvShowView.as_view(), name="show"),
    # path('tvshow/<int:id>/', views.tv_show_detailview, name='details'),
    path("tvshow/<int:id>/", views.TvShowDetailViev.as_view(), name="detail"),
    path("tvshow/<int:id>/update/", views.TvShowUpdateView.as_view(), name="update"),
    path("tvshow/<int:id>/delete/", views.TvShowDeleteView.as_view(), name="delete"),
    # path('add-tv/', views.create_tv_show_view, name='create'),
    path("add-tv/", views.TvShowCreateView.as_view(), name="create"),
]
