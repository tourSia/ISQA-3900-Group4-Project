from .models import Category, Product, Review, Order
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
def index(request):
    """View function for home page of site."""
    num_products = Product.objects.all().count()
    num_reviews = Review.objects.all().count()

    # session data for number of visits to website
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_products': num_products,
        'num_reviews': num_reviews,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product

class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product

class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category

class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Category

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'price', 'category']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('product_list'))

class CategoryCreate(CreateView):
    model = Category
    fields = ['name']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('category_list'))

class ProductUpdate(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'price', 'category']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('product_list'))

class CategoryUpdate(CreateView):
    model = Category
    fields = ['name']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('category_list'))

