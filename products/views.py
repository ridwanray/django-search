from django.shortcuts import render,redirect # redirect
from django.db.models import Q
from .models import * 
# Create your views here.
def query(request):
	query = request.GET.get('query')
	if query is None:	# new
		return redirect('home') # new
	else:
		results = Product.objects.filter(
            Q(name__icontains=query) | Q(price__icontains=query)| Q(category__title__icontains=query))
		return render(request, 'search_results.html',{ 'results':results, })

def home(request):
	products = Product.objects.all()
	return render(request, 'home.html',
     {  'products':products })

