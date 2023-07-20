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
    

class EditView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title' : post.title, 'content' : post.content, 'category' : post.category})

        context = {
            'form' : form,
            'post' : post,
            'title' : 'Blog' 
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.category = form.cleaned_data['category']
            post.save()
            return redirect('blog:detail', pk=pk )

        context = {
            'form' : form,
            'post' : post,
            'title' : 'Blog'
        } 
        
        return render(request, 'blog/post_edit.html', context)
    

class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')


# class SearchView(View):
#     def get(self, request):
#         selected_
#         pass

#     def post():
#         pass


# def search(request):
#         if request.method == 'POST':
#             searched = request.POST['searched']  
#             posts = Post.objects.filter(title__contains=searched) or Post.objects.filter(writer__contains=searched) or Post.objects.filter(category__contains=searched)
#             return render(request, 'blog/post_search.html', {'searched': searched, 'posts': posts})
#         else:
#             return render(request, 'blog/post_search.html', {})

#나중에 검색 기능 추가하기#
class PostSearch(View):
    def get(self, request, tag):
        print(f'request.GET: {request.GET}')
        post_objs = Post.objects.filter(category=tag)
        print(f'tag: {tag}')
        context = {
            'title': 'Main Page',
            'posts': post_objs,
        }
        return render(request, 'blog/post_list.html', context)