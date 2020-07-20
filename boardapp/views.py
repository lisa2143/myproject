from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel, Comment, Reply
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import CommentForm

# Create your views here.
def index(request):
    object_list = BoardModel.objects.order_by('-id')
    keyword = request.GET.get('keyword')
    if keyword:
        object_list = object_list.filter(
                 Q(title__icontains=keyword) | Q(content__icontains=keyword)
               )
    return render(request, 'list.html', {'object_list':object_list})

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup_done.html')
    return render(request, 'signup.html')


def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

@login_required
def logoutfunc(request):
    logout(request)
    return redirect('login')

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def editfunc(request, id):
    boardmodel = get_object_or_404(Article, pk=id)
    CommentForm = CommentForm(instance=content)

    context = {
        'message': 'Edit Content',
        'content': contents,
        'CommentForm': CommentForm,
    }
    return render(request, 'edit.html', context)

class UpdateView(generic.edit.UpdateView):
    template_name = 'update.html'
    model = BoardModel
    fields = ('content', 'images')
    success_url = reverse_lazy('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list') 

class BoardDelete(DeleteView):
    template_name = 'delete.html'
    model = BoardModel
    success_url = reverse_lazy('list')

class CommentView(CreateView):
    model = Comment
    fields = ('name', 'text')
    template_name = 'comment.html'

    def form_valid(self, form):
        boardmodel_pk = self.kwargs['pk']
        boardmodel = get_object_or_404(BoardModel, pk=boardmodel_pk)

        comment = form.save(commit=False)
        comment.target = boardmodel
        comment.save()
        print("OK")
        # 記事の設定
        return redirect('detail', pk=boardmodel_pk)
        # 記事の詳細にリダイレクト

class ReplyView(CreateView):
    model = Reply
    fields = ('name', 'text')
    template_name = 'comment.html'

    def form_valid(self, form):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)

        reply = form.save(commit=False)
        reply.target = comment
        reply.save()
        # 記事の設定
        return redirect('detail', pk=reply.target.pk)
        # 記事の詳細にリダイレクト
