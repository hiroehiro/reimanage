from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView
from .models import MemoModel


class TopView(TemplateView):
    template_name = "top.html"

class MemoView(ListView):
    template_name = "memolist.html"
    model = MemoModel

class MemoCreate(CreateView):
    template_name="memocreate.html"
    model=MemoModel
    fields=('goods',"goods_number")
    success_url=reverse_lazy("memolist")


@require_POST #削除ボタンが押された時＝POSTメゾットの時のみ削除する
def deletememo(request,pk):
    post = MemoModel.objects.get(pk=pk)
    post.delete()
    return redirect('memolist')

