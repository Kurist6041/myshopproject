from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView
from django.views.generic  import CreateView
from django.urls import reverse_lazy
from .forms import ItemPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ItemPost
from django.views.generic import DetailView
from django.template.defaultfilters import floatformat

class PriceFormatMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formatted_prices = []

        for item in context['object_list']:
            formatted_price = f'{floatformat(item.price, -2)}円'
            formatted_prices.append(formatted_price)

        context['items_and_prices'] = list(zip(context['object_list'], formatted_prices))
        return context
    
class IndexView(PriceFormatMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'items'
    queryset = ItemPost.objects.order_by('-id')
    paginate_by = 9   


class ItemListView(PriceFormatMixin, ListView):
    model = ItemPost
    template_name = 'item_list.html'
    context_object_name = 'items'
    queryset = ItemPost.objects.all()
    

    
@method_decorator(login_required, name='dispatch')
class CreateItemView(CreateView):
    
    form_class = ItemPostForm
    
    template_name = 'post_item.html'
    
    success_url = reverse_lazy('shop:post_done')
    
    def form_valid(self, form):
        
        postdata = form.save(commit=False)
        
        postdata.user = self.request.user
        
        postdata.save()
        
        return super().form_valid(form)   
    
class PostSuccessView(TemplateView):
    
    template_name ='post_success.html'
    
class MypageView(ListView):
    model = ItemPost
    template_name = 'mypage.html'
    
    
def get_queryset(self):
    queryset = ItemPost.objects.filter(user=self.request.user)
    return queryset

class UserView(ListView):
    
    template_name = 'index.html'
    
    def get_queryset(self):
        
        
        user_id = self.kwargs['user']
        
        user_list = ItemPost.objects.filter(
            user=user_id).order_by('-posted-at')
        
        return user_list


class BuySuccessView(TemplateView):
    
    template_name = 'item_success.html'
    


    
    
        
    

    
        
    




  

    
    
