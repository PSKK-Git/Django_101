from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
from django.shortcuts import render, get_object_or_404
from .models import Product, SubProduct, SubPost, Banner

from .models import Post


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    

# class BannerHomePageView(TemplateView):
#     template_name = "home.html"

#     def get_banner_data(self, **kwargs):
#         bannercontext = super().get_context_data(**kwargs)
#         bannercontext['banners'] = Banner.objects.all()
#         return bannercontext


def home(request):
    banner = Banner.objects.first() # get the first banner object
    return render(request, 'home.html', {'banner': banner})

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class SubPostDetailView(DetailView):
    template_name = "detail.html"
    model = SubPost

def subpost_detail(request, pk):
    subpost = get_object_or_404(SubPost, pk=pk)
    return render(request, 'subpost.html', {'subpost': subpost})
# def home(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {'products': products})

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