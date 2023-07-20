from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path(패턴, 매핑) /blog/
    # path("", views.index), # FBV
    path("", views.Index.as_view(), name='list'),
    # 글 조회
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", views.WriteView.as_view(), name='write'),
    # 글 수정
    path("edit/<int:pk>/", views.EditView.as_view(), name='edit'),
    # 글 삭제
    path("delete/<int:pk>/", views.Delete.as_view(), name='delete'),
    # 글 검색
    path("search/<str:tag>/", views.PostSearch.as_view(), name='search'),
    # 코멘트 작성
    # 코멘트 삭제
]
