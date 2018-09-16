from django.conf.urls import url
from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name = 'index'),
    # /polls/5/
    path('<int:pk>', views.DetailView.as_view(), name = 'detail'),
    # /5/vote/
    path('<int:question_id>/vote', views.vote, name = 'vote'),
    # /polls/5/results
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    # /polls/owner
    path('owner', views.owner, name='owner')
]
