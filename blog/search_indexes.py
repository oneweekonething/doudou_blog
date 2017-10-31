from haystack import indexes
from blog.models import Article

# django-haystack全文检索详细教程
# http://blog.csdn.net/ac_hell/article/details/52875927

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='p')
