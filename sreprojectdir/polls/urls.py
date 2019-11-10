"lsreprojectdir/polls/urls.py"

from django.conf.urls import url

from . import views




app_name = 'polls'
urlpatterns = [ 
            url('', views.IndexView.as_view(), name='index'),
            url('/', views.IndexView.as_view(), name='index'),
            url('int:pk/detail/', views.DetailView.as_view(), name='detail'),
            url('<int:question_id>/vote/', views.vote, name='vote'),
            url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
            ]



"""
app_name = 'polls'
    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:question_id>/', views.detail, name='detail'
        ),
        path('<int:question_id>/results/', views.results, name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
            ]

"""
