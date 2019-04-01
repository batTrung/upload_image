from django.shortcuts import render, redirect
from .models import Profile 
from .forms import ProfileForm

def upload_file(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, files = request.FILES)
		if form.is_valid():
			user = form.save()
			return redirect('upload_file')
	else:
		form = ProfileForm()

	users = Profile.objects.all()
	
	return render(request,'account/home.html',{'form':form,'users':users})