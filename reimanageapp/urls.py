from django.urls import path
from .views import TopView,MemoView,deletememo,MemoCreate

urlpatterns=[
    path('', TopView.as_view(), name="top"),
    path('memolist', MemoView.as_view(), name="memolist"),
    path('deletememo/<int:pk>', deletememo, name="deletememo"),
    path('memocreate', MemoCreate.as_view(), name="memocreate")
]