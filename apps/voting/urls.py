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
router.register(r'votings', views.VotingViewSet, basename='votings')
router.register(r'characters', views.CharacterViewSet, basename='characters')
router.register(r'make_vote', views.MakeVoteViewSet, basename='make_vote')
router.register(r'winners', views.WinnerViewSet, basename='winners')



urlpatterns = [
    path('', include(router.urls))
]
