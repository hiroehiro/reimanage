from django.urls import path
from .views import TopView,MemoView,deletememo

urlpatterns=[
    path('', TopView.as_view(), name="top"),
    path('memolist', MemoView.as_view(), name="memolist"),
    path('deletememo/<int:pk>', deletememo, name="deletememo"),
]