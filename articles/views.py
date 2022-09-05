from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView  # new
from django.views.generic.detail import SingleObjectMixin  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse  # new

from .forms import CommentForm  
from .models import Article

class ArticleListView(ListView):
    model=Article
    template_name ='article_list.html'



class CommentGet(LoginRequiredMixin ,DetailView):
    model=Article
    template_name ='article_detail.html'

    def get_context_data(self, **kwargs):  # new
          context = super().get_context_data(**kwargs)
          context['form'] = CommentForm()
          return context

class CommentPost(SingleObjectMixin, FormView):  # new
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk}) 

class ArticleDetailView(LoginRequiredMixin, View):  # new
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class ArticleUpdateView(UpdateView):
    model=Article
    fields = (
        'title',
        'body',
    )
    template_name ='article_update.html'


class ArticleDeleteView(DeleteView):
    model=Article
    template_name ='article_delete.html'
    success_url=reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model=Article
    template_name= 'article_new.html'
    fields=(
        'title',
        'body',
        'author'
    )    