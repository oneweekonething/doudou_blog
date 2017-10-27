from django.views.generic.edit import FormView
from .forms import CommentForm
from .models import Comment
from django import forms
from blog.models import Article
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect


# Create your views here.


class CommentPostView(FormView):
    form_class = CommentForm
    template_name = 'blog/article_detail.html'

    def form_valid(self, form):
        """提交的数据验证合法后的逻辑"""
        user = self.request.user

        article_id = self.kwargs['article_id']
        article = Article.objects.get(pk=article_id)

        if not self.request.user.is_authenticated():
            email = form.cleaned_data['email']
            username = form.cleaned_data['name']
            user = get_user_model().objects.get_or_create(username=username, email=email)[0]

        comment = form.save(False)
        comment.article = article
        comment.author = user

        if form.cleaned_data['parent_comment_id']:
            parent_comment = Comment.objects.get(pk=form.cleaned_data['parent_comment_id'])
            comment.parent_comment = parent_comment
        comment.save(True)

        return HttpResponseRedirect("%s#div-comment-%d" % (article.get_absolute_url(), comment.pk))
