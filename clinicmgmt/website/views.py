from django.shortcuts import render
from clinicmgmt import settings as conf
# Create your views here.
def home_page(request):
    cname=conf.cname
    context={"company":cname}
    return render(request,'websiteviews/index.html',context)