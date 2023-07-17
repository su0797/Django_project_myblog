from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post, Comment

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('No!!!')


###Post
class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            "posts" : posts,
            "title" : "Blog"
        }
        return render(request, "blog/post_list.html", context)
    


class DetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        # comments = Comment.objects.filter(post=post)
        context = {
            "title" : "Blog",
            "post_id" : pk,
            "post_title" : post.title,
            "post_writer" : post.writer,
            "post_content" : post.content,
            "post_created_at" : post.created_at,
        }
        return render(request, 'blog/post_detail.html', context)
