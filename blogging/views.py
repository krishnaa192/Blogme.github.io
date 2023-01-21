
from calendar import c
from operator import le
from django.shortcuts import render,redirect
from blogging.models import Blog
from user.models import Profile
from blogging.models import Tags
from django.contrib.auth.decorators import login_required
from .forms import SubmitForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .utils import Paginationpage,searchProject
from django.db.models import Q
# Create your views here.

def Home(request):
  tag= Tags.objects.all()
  love=Tags.objects.filter(name="Love")
  work=Blog.objects.order_by('-upload')
  params={'work':work,'tag':tag,'love':love}
  return render(request,"main.html", params)

# view for author
@login_required(login_url="login")
def authors(request):
    author=Profile.objects.all()
    tag=Tags.objects.all()
    a_pms={'author':author,'tag':tag}
    return render(request, "author.html",a_pms)

def Blogpage(request):
  return render(request,'blogpage.html')


#view for signin page
@login_required(login_url="login")
def Read(request,pk):
    profile=request.user.profile
    tags=Tags.objects.all()
    post=Blog.objects.filter(id=pk).first()
    other =Blog.objects.filter()[:4]
    read={'post':post,'other':other,'profile':profile,'tags':tags}
    return render(request,"post.html",read)


@login_required(login_url="login")
def Submit_Form(request):
  profile=request.user.profile
  form=SubmitForm()
  if request.method=='POST':
    # newtags = request.POST.get('newtags').replace(',',  " ").split()
    form=SubmitForm(request.POST,request.FILES)
    if form.is_valid():
      blog=form.save(commit=False)
      blog.Author=profile
      blog.save()
      # for tag in newtags:
      #           tag, created = Tags.objects.get_or_create(name=tag)
      #           blog.tags.add(tag)
      return redirect('/')
  context ={'form':form}
  return render(request,"submitform.html",context)

@login_required(login_url="login")
def update_blog(request,pk):
  profile = request.user.profile
  blog=Blog.objects.get(id=pk)
  form=SubmitForm(instance=blog)
  
  if request.method=='POST':
    # newtags = request.POST.get('newtags').replace(',',  " ").split()

    form=SubmitForm(request.POST, request.FILES,instance=blog)
    if form.is_valid():
      blog=form.save()
    return redirect('Home')
  context ={'form':form,'blog':blog}
  return render(request,"submitform.html",context)

@login_required(login_url="login")
def delete_blog(request,pk):
 profile = request.user.profile
 blog=Blog.objects.get(id=pk)
 if request.user == blog.user:
  if request.method == 'POST':
    blog.delete()
    return redirect('Home')
 context={'blog':blog}
 return render(request,"blog_delete.html",context)




def all_blog(request):
  search_query,blogs=searchProject(request)
  # custom_ranges,blogs=Paginationpage(request,blogs,4)
  context={'blogs':blogs,'search_query':search_query}
  return render(request,'blogpag.html',context)