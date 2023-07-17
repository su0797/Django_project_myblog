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
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]
