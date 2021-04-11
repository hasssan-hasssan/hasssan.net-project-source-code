from blog import views
from blog.feeds import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'
urlpatterns = [
    path('contact_me/', views.About_Me.as_view(), name='about_me'),
    path('', views.Post_list.as_view(), name='post_list'),
    path('teaches-list', views.Teaches_List.as_view(), name='teaches_list'),
    path('teach/<slug:slug>/', views.teach_detail, name='teach_detail'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.post_detail, name='post_detail'),
    path('post-<int:post_id>/sharing/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('projects/', views.Pro_list.as_view(), name='pro_list'),
    path('<slug:project>/', views.pro_detail, name='pro_detail'),
    path('search-engine', views.search_engine, name='search_engine'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
