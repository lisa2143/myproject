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
    # try:
    #     object = BoardModel.objects.get(pk=pk)
    # except models.BoardModel.DoesNotExist:
    #     raise Http404
    # if request.method == "POST":
    #     BoardModel.Comment.objects.create(to=BoardModel, text=request.POST["text"],object=object)
    # context ={'object':object}
    # return render(request, 'detail.html', {'object':object})


@login_required
def logoutfunc(request):
    logout(request)
    return redirect('login')

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def updatefunc(request, pk):
    if request.method == 'POST':
        boardmodel = get_object_or_404(Boardmodel, pk=id)
        CommentForm = CommentForm(request.POST, instance=content)
        if commentForm.is_valid():
            commentForm.save()

    context = {
        'content': 'Update content' + str(id),
    }
    return render(request, 'detail.html', context)

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')


# class BoardUpdate(UpdateView):
    # model = BoardModel
    # fields = ('content', 'images')
    # success_url = reverse_lazy('detail')
    #
    # def get_success_url(self):
    #     return reverse('inputs:boardmodel', kwargs={'pk': self.object.id})
    # model = BoardModel
    # template_name = 'update.html'
    # fields = '__all__'
    # success_url = reverse_lazy('detail')
    # model = BoardModel
    # form_class = CommentForm
    # template_name = 'update.html'
    # success_url = reverse_lazy('detail')
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     messages.success(
    #         self.request, '「{}」を更新しました'.format(form.instance))
    #     return result
    # def get_form(self):
    #     form = super(BoardUpdate, self).get_form()
    #     form.fields['content'].object = '内容'
    #     form.fields['images'].object = '画像'
    #     return form
    #
    # def get_success_url(self):
    #     return reverse('detail', kwargs={'pk': self.object.id})

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
