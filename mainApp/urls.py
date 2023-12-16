
# mainApp urls

from django.urls import path
from .views import *

urlpatterns = [
    path('student', StudentView.as_view()),
    path("student/<int:id>", StudentView.as_view()),
    path('teachers/', TeacherList.as_view()),
    path("teachers/<int:pk>/", TeacherDetails.as_view())
]
