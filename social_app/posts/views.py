from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})


