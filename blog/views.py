from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm

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
    

class WriteView(LoginRequiredMixin,View):
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
        post = Post.objects.prefetch_related('comment_set').get(pk=pk)
        comments = post.comment_set.all()
        comment_form = CommentForm()

        context = {
            "title" : "Blog",
            "post_id" : pk,
            "post_title" : post.title,
            "post_writer" : post.writer,
            "post_content" : post.content,
            "post_category" : post.category,
            "post_created_at" : post.created_at,
            "comments" : comments,
            "comment_form" : comment_form,
        }
        return render(request, 'blog/post_detail.html', context)
    

class EditView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(initial={'title' : post.title, 'content' : post.content, 'category' : post.category})

        context = {
            'form' : form,
            'post' : post,
            'title' : 'Blog' 
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
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
        post = get_object_or_404(Post,pk=pk)
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
    


###Comment
class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user

            try:
                comment = Comment.objects.create(post=post, content=content, writer=writer)
            except ObjectDoesNotExist as e:
                print('게시물이 존재하지 않습니다.', str(e))
            except ValidationError as e:
                print('오류가 발생했습니다.', str(e))
            return redirect('blog:detail', pk=pk)
        
        context = {
            'title':'Blog',
            'post_id':pk,
            'comments':post.comment_set.all(),
            'comment_form':form
        }
        return render(request, 'blog/post_detail.html', context)
    

class CommentDelete(View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)
    
