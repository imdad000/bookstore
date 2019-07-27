from django.shortcuts import render
import requests
import json
import random
from .models import Book
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


def details(request,id):
	print(id)
	baseurl='https://www.googleapis.com/books/v1/volumes/'+str(id)
	print(baseurl)
	data=requests.get(baseurl)
	data=data.json()
	print(data)
	for r in data.values():
		print(r)
	frontend={
	"description":data.volumeInfo.description,
	"title":data.volumeInfo.title,
	"author":data.volumeInfo.author,
	"rating":data.averageRating,
	"imagesrc":data.imageLinks.large,
	"publisher":data.publisher
	}

	return render(request, "details.html", frontend)

