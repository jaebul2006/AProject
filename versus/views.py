from django.shortcuts import render

def post_list(request):
	return render(request, 'versus/post_list.html', {})