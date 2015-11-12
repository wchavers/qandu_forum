from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
     template_name = 'home.html'

class ForumCreateView(CreateView):
    model = Forum
    template_name = "forum/forum_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('forum_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ForumCreateView, self).form_valid(form)

class ForumListView(ListView):
    model = Forum
    template_name = "forum/forum_list.html"

class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forum/forum_detail.html'

class ForumUpdateView(UpdateView):
    model = Forum
    template_name = 'forum/forum_form.html'
    fields = ['title', 'description']

class ForumDeleteView(DeleteView):
    model = Forum
    template_name = 'forum/forum_confirm_delete.html'
    success_url = reverse_lazy('forum_list')

class AnswerCreateView(CreateView):
    model = Answer
    template_name = "answer/answer_form.html"
    fields = ['text']

    def get_success_url(self):
        return self.object.question.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = Forum.objects.get(id=self.kwargs['pk'])
        return super(AnswerCreateView, self).form_valid(form)
