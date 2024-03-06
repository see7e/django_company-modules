from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item, OutboundRequest
from .forms import OrderForm


@login_required
def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "inventory.html", context)


@login_required
def orders(request):
    order_list = OutboundRequest.objects.all()
    context = {"order_list": order_list}
    return render(request, "orders.html", context)


@login_required
def new_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.creator = request.user
            order.save()
            return render(request, "order_form.html", {"form": form})

    form = OrderForm(creator=request.user.id)
    return render(request, "order_form.html", {"form": form})
