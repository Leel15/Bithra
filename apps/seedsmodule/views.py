from django.shortcuts import render , get_object_or_404 , redirect
from .models import Seed 
import datetime

def home(request):
    return render(request, 'seedsmodule/home.html')

def store(request):
    all_seeds = Seed.objects.all()
    return render(request, 'seedsmodule/store.html', {'seeds': all_seeds})

def seed_detail(request, seed_id):
    seed = get_object_or_404(Seed, id=seed_id)
    return render(request, 'seedsmodule/seed_detail.html', {'seed': seed})


def planting_calendar(request):
    current_month_num = datetime.datetime.now().month
    current_month_name = datetime.datetime.now().strftime('%B')
    
    seeds_now = Seed.objects.filter(planting_month=current_month_num)
    
    months_list = [
        (1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'),
        (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'),
        (9, 'Sep'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')
    ]
    
    all_seeds = Seed.objects.all().order_by('planting_month')

    return render(request, 'seedsmodule/calendar.html', {
        'seeds': seeds_now,
        'month_name': current_month_name,
        'current_month_num': current_month_num,
        'months_list': months_list,
        'all_seeds': all_seeds
    })

def add_to_cart(request, seed_id):

    cart = request.session.get('cart', [])
    cart.append(seed_id)
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'store'))

def cart_page(request):

    cart_ids = request.session.get('cart', [])
    cart_items = Seed.objects.filter(id__in=cart_ids)
    total_price = sum(seed.price for seed in cart_items)
    
    return render(request, 'seedsmodule/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart')