from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Picture
from django.shortcuts import render, get_object_or_404
from .forms import PictureForm
from django.contrib.auth.decorators import login_required

@login_required
def pic_list(request):
    """
    リクエストがGETの場合、削除されていない写真の一覧を取得
    リクエストがPOSTの場合、写真を投稿
    """
    if request.method == 'GET':
      pics = Picture.objects.filter(deleted=False)
      return render(request, 'pics/pic_list.html', {'pics': pics, 'form': PictureForm()})
    elif request.method == 'POST':                                                     
        form = PictureForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        picuture = Picture()
        picuture.image = form.cleaned_data['image']
        picuture.deleted = False
        picuture.save()
        pics = Picture.objects.filter(deleted=False)
        return render(request, 'pics/pic_list.html', {'pics': pics, 'form': PictureForm()})

@login_required
def pic_detail(request, pk):
    """
    写真詳細画面へ遷移

    Parameters
    ----------
    pk：int
    主キー　写真を一意にするためのキー
    """
    pic = get_object_or_404(Picture, pk=pk)
    return render(request, 'pics/pic_detail.html', {'pic': pic})

@login_required
def pics_update(request):
    """
    選択した写真を論理削除する
    """
    mypk = request.POST.get('pk')
    pic = Picture.objects.filter(pk=mypk).update(deleted = True)
    pics = Picture.objects.filter(deleted=False)
    return render(request, 'pics/pic_list.html', {'pics': pics, 'form': PictureForm()})
