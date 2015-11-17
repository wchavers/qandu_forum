from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
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

    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)
        question = Forum.objects.get(id=self.kwargs['pk'])
        answers = Answer.objects.filter(question=question)
        context['answers'] = answers
        user_answers = Answer.objects.filter(question=question, user=self.request.user)
        context['user_answers'] = user_answers
        return context

class ForumUpdateView(UpdateView):
    model = Forum
    template_name = 'forum/forum_form.html'
    fields = ['title', 'description']

    def get_object(self, *args, **kwargs):
        object = super(ForumUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class ForumDeleteView(DeleteView):
    model = Forum
    template_name = 'forum/forum_confirm_delete.html'
    success_url = reverse_lazy('forum_list')

    def get_object(self, *args, **kwargs):
        object = super(ForumDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class AnswerCreateView(CreateView):
    model = Answer
    template_name = "answer/answer_form.html"
    fields = ['text']

    def get_success_url(self):
        return self.object.question.get_absolute_url()

    def form_valid(self, form):
      question = Forum.objects.get(id=self.kwargs['pk'])
      if Answer.objects.filter(question=question, user=self.request.user).exists():
          raise PermissionDenied()
      form.instance.user = self.request.user
      form.instance.question = Forum.objects.get(id=self.kwargs['pk'])
      return super(AnswerCreateView, self).form_valid(form)

class AnswerUpdateView(UpdateView):
    model = Answer
    pk_url_kwarg = 'answer_pk'
    template_name = 'answer/answer_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.question.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(AnswerUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class AnswerDeleteView(DeleteView):
    model = Answer
    pk_url_kwarg = 'answer_pk'
    template_name = 'answer/answer_confirm_delete.html'

    def get_success_url(self):
        return self.object.question.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(AnswerDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object
