from django.shortcuts import render

# Create your views here.
from .models import Photo

def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos}) # templates/photo/list.html
                                                                 # default : 'object_list' : photos

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']  # 작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'
    
    def form_valid(self, form): # 저장 전 입력된 데이터가 올바른지 검사 후 저장
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 데이터가 올바르다면 저장
            form.instance.save()
            return redirect('/')    # success URL
        else:
            return self.render_to_response({'form':form})   # 잘못 입력 시 form에 입력된 정보를 그대로 돌려줌

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'