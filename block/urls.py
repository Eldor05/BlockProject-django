from django.urls import path

from .views import BlockListView, BlockDetailView, BlockCreateView, BlockUpdateView, BlockDeleteView

urlpatterns=[
    path('post/<int:pk>/delete/', BlockDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlockUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlockCreateView.as_view(), name='post_new'),
    path('', BlockListView.as_view(), name='home'),
    path('post/<int:pk>/', BlockDetailView.as_view(), name='post_detail'),
]