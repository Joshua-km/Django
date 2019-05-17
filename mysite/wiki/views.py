from django.views import generic
from .models import Page, UserFileUpload
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .form import UploadFileForm


class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all().order_by('title')

class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'

    
def view_page(request, pk):
    try:
        page = Page.objects.get(pk = pk)
        return render(request, 'wiki/detail.html', {"page": page})
    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {"page_name": pk})

@login_required(login_url='wiki:login')#This line of code is making sure that there is a password in place meaning that you have to loging before you can edit a page
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content = ''
    return render(request,'wiki/edit_page.html',
                    {
                        'page_name': pk,
                        'content': content
                    })
@login_required(login_url='wiki:login')#This line of code is making sure that there is a password in place meaning that you have to loging before you can edit a page
def save_page(request, pk):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=pk)
        page.content = content
    except Page.DoesNotExist: #This is erro that will be pop up if the page they are looking does not exist
        page = Page(title=pk, content=content)
    page.save()#this is so thast user can save the page once they have made it.
    return redirect ('wiki:detail', pk=pk)

@login_required(login_url='wiki:login')#This line of code is making sure that there is a password in place meaning that you have to loging before you can edit a page
def upload_file(request):# this is so the user of the wiki page can have way so they can upload there owne files.
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)