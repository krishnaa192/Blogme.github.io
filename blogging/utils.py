import imp
from .models import Tags,Blog
from user.models import Profile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

def searchProject(request):
  search_query=''
  if request.GET.get('search_query'):
    search_query=request.GET.get('search_query')
  tag=Tags.objects.filter(name__icontains=search_query)
  authors=Profile.objects.filter(Name__icontains=search_query)
  blogs=Blog.objects.distinct().filter(
    Q(blog_title__icontains=search_query)|Q(Pen_name__icontains=search_query)|Q(tags__in=tag)|Q(Author__in=authors)
    )

  return search_query, blogs





def Paginationpage(request,blogs,results):

   
    page=request.GET.get('page')
    paginator=Paginator(blogs,results)
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        page=paginator.num_pages
        blogs=paginator.page(page)
    leftIndex=(int(page)-3)
    if leftIndex<1:
        leftIndex=1

    rightIndex=(int(page)+3)
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1
    custom_ranges=range(leftIndex,rightIndex)


    return custom_ranges,blogs