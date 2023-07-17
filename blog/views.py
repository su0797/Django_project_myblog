from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Post, Comment
from .forms import PostForm

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
    

class WriteView(View):
    def get(self, request):
        form = PostForm()
        context = {
            "form": form,
            "title": "Blog"
        }
        return render(request, "blog/post_form.html", context)
    
    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect("blog:list")
        
        context = {
            'form': form
        }

        return render(request, "blog/post_form.html", context)

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
            "post_category" : post.category,
            "post_created_at" : post.created_at,
        }
        return render(request, 'blog/post_detail.html', context)
