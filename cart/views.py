from django.shortcuts import render, redirect
from .models import CartItem
from django.template.defaultfilters import floatformat
from django.views.generic import ListView
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import ItemPost
from django.db import transaction

class CartView(ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def intcomma(self, value):
        orig = str(value)
        new = ""
        while orig != "":
            orig, r = orig[:-3], orig[-3:]
            new = f"{r},{new}" if new else r
        return f"{new}円"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formatted_prices = []

        for item in context['object_list']:
            formatted_price = self.intcomma(item.price)
            formatted_prices.append(formatted_price)

        context['items_and_prices'] = list(zip(context['object_list'], formatted_prices))
        return context




class AddToCartView(View):
    def post(self, request, item_id):
        try:
            with transaction.atomic():
                # 商品情報をItemPostから取得
                item = get_object_or_404(ItemPost, id=item_id)

                # カートにアイテムを追加する処理を実装
                cart_item, created = CartItem.objects.get_or_create(item=item, user=request.user)

                # カート内のアイテム数を取得
                cart_count = CartItem.objects.filter(user=request.user).count()

                # 保存を忘れていた場合、ここで保存する
                cart_item.save()

                # JSONレスポンスを返す（カートのアイテム数を含む）
                return JsonResponse({'cart_count': cart_count})
        except Exception as e:
            # エラーをキャッチしてログなどに記録する
            print(str(e))
            return JsonResponse({'error': 'An error occurred'}, status=500)











