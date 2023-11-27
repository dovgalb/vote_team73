from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# urlpatterns = [
#     path('', views.VotingList.as_view()),
#     path('<int:pk>', views.VotingDetail.as_view()),
#     path('<int:pk>/participants/', views.VotingParticipants.as_view()),
#     path('<int:pk>/winners/', views.VotingWinners.as_view()),
# ]

router = DefaultRouter()

# модернизированные
router.register(r'make_vote', views.MakeVoteViewSet, basename='make_vote')



urlpatterns = [
    path('', include(router.urls))
]
