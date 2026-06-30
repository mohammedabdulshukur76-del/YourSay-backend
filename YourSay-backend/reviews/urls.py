from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.get_reviews,    name='get_reviews'),
    path('submit/',             views.submit_review,  name='submit_review'),
    path('<int:review_id>/helpful/', views.mark_helpful, name='mark_helpful'),
]