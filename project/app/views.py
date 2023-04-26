from django.shortcuts import render,HttpResponse
from .models import Post
from django.views import generic 
from .forms import RegistrationForm
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class PostList(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = 'index.html'


class DetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'

def contact(request):
  if request.method=='POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('<h1>Register Successfully</h1>')
  else:
    form=RegistrationForm()
  return render(request,'contact.html',{'form':form})
  
