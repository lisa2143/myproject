from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel, Comment, Reply
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.db.models import Q
# from django.contrib import messages


# Create your views here.
def index(request):
    object_list = BoardModel.objects.order_by('-id')
    keyword = request.GET.get('keyword')
    if keyword:
        object_list = object_list.filter(
                 Q(title__icontains=keyword) | Q(content__icontains=keyword)
               )
        # messages.success(request, '「{}」の検索結果'.format(keyword))
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

# class BookList(ListView):
#     model = Book
#     def get_queryset(self):
#         q_word = self.request.GET.get('query')
#
#         if q_word:
#             object_list = Book.objects.filter(
#                 Q(title__icontains=q_word) | Q(content__icontains=q_word))
#         else:
#             object_list = Book.objects.all()
#         return object_list

def detailfunc(request, pk):
    try:
        object = BoardModel.objects.get(pk=pk)
    except models.BoardModel.DoesNotExist:
        raise Http404
    if request.method == "POST":
        BoardModel.Comment.objects.create(to=BoardModel, text=request.POST["text"],object=object)
    context ={'object':object}
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

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')

class BoardUpdate(UpdateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('detail')

    def get_form(self):
        form = super(BoardUpdate, self).get_form()
        form.fields['title'].object = 'タイトル'
        form.fields['content'].object = '内容'
        form.fields['images'].object = '画像'
        return form

class BoardDelete(DeleteView):
    template_name = 'delete.html'
    model = BoardModel
    success_url = reverse_lazy('list')
