from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from django.shortcuts import render, get_object_or_404
from .models import Product, SubProduct, SubPost,Baner

from .models import Post,Banner, About

from django.views import View
from django.shortcuts import render
from django.db.models import Q
from .models import Post

class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            results = Post.objects.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) | 
                Q(type__icontains=query)
            ).distinct()
        else:
            results = Post.objects.all()
        context = {'results': results}
        return render(request, 'search_results.html', context)




class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        context['banners'] = Banner.objects.all()
        context['about'] = About.objects.all()
        return context

    
class BanerView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baners'] = Baner.objects.all()
        return context
    





def home(request):
    return render(request, 'feed/home.html')

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class SubPostDetailView(DetailView):
    template_name = "detail.html"
    model = SubPost

def subpost_detail(request, pk):
    subpost = get_object_or_404(SubPost, pk=pk)
    return render(request, 'subpost.html', {'subpost': subpost})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    subproduct = get_object_or_404(SubProduct, pk=pk)
    return render(request, 'product.html', {'product': product, 'subproduct': subproduct})

def subproduct_detail(request, pk):
    subproduct = get_object_or_404(SubProduct, pk=pk)
    return render(request, 'subproduct.html', {'subproduct': subproduct})




# class AddPostView(FormView):
#     template_name = "new_post.html"
#     form_class = PostForm
#     success_url = "/"

#     def dispatch(self, request, *args, **kwargs):
#         self.request = request
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         # Create a new Post
#         new_object = Post.objects.create(
#             text=form.cleaned_data['text'],
#             image=form.cleaned_data['image']
#         )
#         messages.add_message(self.request, messages.SUCCESS, 'Your post was successful')
#         return super().form_valid(form)