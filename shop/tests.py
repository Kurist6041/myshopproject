from django.test import TestCase

# Create your tests here.
#class ItemListView(ListView):
    model = ItemPost
    template_name = 'item_list.html'
    context_object_name = 'items'
    queryset = ItemPost.objects.all()