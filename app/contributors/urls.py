from django.urls import path
from contributors.views import TopContributorsView

urlpatterns = [
    path('', TopContributorsView.as_view())
]
