from django.urls import path
from . import views

urlpatterns = [
    path('',           views.get_issues,   name='get_issues'),
    path('submit/',    views.submit_issue, name='submit_issue'),
    path('<int:issue_id>/vote/', views.vote_issue, name='vote_issue'),
]