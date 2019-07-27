from django.shortcuts import render,redirect, get_object_or_404
import requests
import json
import random
from .models import Book
from django.forms import ModelForm
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['book_id', 'book_quantity']


def home_page(request):
	# api=https://www.googleapis.com/books/v1/volumes?q=python
	query = str(request.GET.get('query', ''))
	if query != '':
		baseurl='https://www.googleapis.com/books/v1/volumes?q='+query
		data=requests.get(baseurl)
		data=data.json()
		print(data['totalItems'])
		if data['totalItems']==0:
			context={
			"hello":"Please enter the book you are searching"
			}
			return render(request,'book.html',context)
		else:

			if len(data)>0:
				result=True
			else:
				result=False

			all_inventory=Book.objects.all()
			frontend = {
			"search_result": data,
			"mydata":all_inventory,
			"has_result": result
			}


	
			for r in data['items']:
				quantity=random.randint(0,2)
				book_id=r['id']
				try:
					Book.objects.get(book_id=book_id)
				except Book.DoesNotExist:
					Book.objects.create(book_id=book_id, book_quantity=quantity)	
				# print(r['id'])
				#print(r)
		
			return render(request,'book.html',frontend)
	else:
		context={
		"hello":"Please enter the book you are searching"
		}
		return render(request,'book.html',context)


def update_book(request,pk, template_name='edit.html'):
	print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",pk)
	book= get_object_or_404(Book, pk=pk)
	form = BookForm(request.POST or None, instance=book)
	if form.is_valid():
		form.save()
		return redirect('bookapp:home_page')
	return render(request, template_name, {'form':form})

def delete_book(request,pk,template_name='delete.html'):
	book= get_object_or_404(Book, pk=pk)
	if request.method=='POST':
		book.delete()
		return redirect('bookapp:home_page')
	return render(request, template_name, {'object':book})



