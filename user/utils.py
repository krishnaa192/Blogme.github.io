
from django.db.models import Q
from .models import Profile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def searchAuthors(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    profiles = Profile.objects.distinct().filter(
        Q(Name__icontains=search_query) 
        
    )

    return profiles, search_query





def PaginationProfile(request,author,results):

   
    page=request.GET.get('page')
    paginator=Paginator(author,results)
    try:
        author=paginator.page(page)
    except PageNotAnInteger:
        author=paginator.page(1)
    except EmptyPage:
        page=paginator.num_pages
        author=paginator.page(page)


    leftIndex=(int(page)-3)
    if leftIndex<1:
        leftIndex=1

    rightIndex=(int(page)+3)
    if rightIndex>paginator.num_pages:
        rightIndex=paginator.num_pages+1
    custom_ranges=range(leftIndex,rightIndex)


    return custom_ranges,author