from django.shortcuts import render,redirect
from .models import assset_tracker_activity,Location,assset_tracker_activity,staff_contractor_company,history_order
from .forms import LocationForm,assset_tracker_activityForm,staff_contractor_companyForm
from cart.cart import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from shop.models import Product
from login.models import staff_contractor

@login_required(login_url='/login')
def order_create(request):
    cart = Cart(request)
    form = staff_contractor_companyForm()
    asset = assset_tracker_activityForm()
    if request.method == 'POST':
        form  = staff_contractor_companyForm(request.POST)
        asset = assset_tracker_activityForm(request.POST)
        if form.is_valid() and asset.is_valid():
            scc = form.cleaned_data
            obj = staff_contractor_company(
                user = request.user,
                company_name = scc['company_name'],
                company_description = scc['company_description'],
                email_address = scc['email_address'],
                location = scc['location'],
                work_phone = scc['work_phone'],
                mobile_phone = scc['mobile_phone'],
                emergency_phone = scc['emergency_phone'],
                emergency_contact = scc['emergency_contact'],
                emergency_contact_note = scc['emergency_contact_note'],
                fax_number = scc['fax_number'],
                addressline_1 = scc['addressline_1'],
                addressline_2 = scc['addressline_2'],
                city = scc['city'],
                province_state = scc['province_state'],
                postal_code = scc['postal_code'],
                country_region = scc['country_region'],
                website = scc['website']
            )
            obj.save()
            try:
                obj1 = staff_contractor.objects.get(user = request.user)
                obj1.save()
            except:
                obj1 = staff_contractor(user = request.user)
                obj1.save()
            obj1.staff_contractor_company_id.add(obj)
            obj1.save()
            ata = asset.cleaned_data    
            for i in cart:
                shopitem = Product.objects.get(name = i['product'])
                shopitem.active_item = False
                shopitem.save()
                shopitem1 = assset_tracker_activity()
                shopitem1.asset_tracking_id = shopitem
                shopitem1.user = request.user.username
                shopitem1.note = ata['note']
                shopitem1.location_being_moved_to = ata['location_being_moved_to']
                shopitem1.move_date = ata['move_date']
                shopitem1.due_for_pickup = ata['due_for_pickup']
                shopitem1.item_status = ata['item_status']
                shopitem1.detailed_note = ata['detailed_note']
                shopitem1.save()
                a = history_order()
                a.user = request.user
                a.item = i['product']
                a.save()
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': obj})
    else:
        form = staff_contractor_companyForm()
        asset= assset_tracker_activityForm() 
    return render(request, 'orders/order/create.html', {'form': form,'asset':asset})



@login_required(login_url='/login')
def Borrowed_items(request):
    items=assset_tracker_activity.objects.all()
    a = []
    print(items)
    for i in items:
        print(i.returned)
        if i.returned == False and i.user == request.user.username:
            a.append(i)
    print(a)
    context={
        'item':a,
        'check':2
    }
    return render(request,'borrowed.html',context)

@login_required(login_url='/login')
def borrow_detail(request,id):
    product = assset_tracker_activity.objects.get(id=id)
    location= Location.objects.filter(product=product)
    form= LocationForm()
    if request.method=='POST':
        form=LocationForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product=product
            new_comment.save()
            form.save()
            return HttpResponseRedirect(reverse('orders:borrow_detail', args=[id]))
    print(product)
    context = {
        'product': product,
        'form':form,
        'location':location,
        'check':2
       
    }
    return render(request, 'borrow_detail.html', context)

@login_required(login_url='/login')
def staff_contractor_companyView(request):
    if request.method=='POST':
        form=assset_tracker_activityForm(request.POST)
        if form.is_valid():
           asset= form.save()
           print(asset)
    context={
        'form1':asset
    }

    return render(request, 'orders/order/create.html', context)

@login_required(login_url='/login')
def returning_items(request,i_d):
    obj = assset_tracker_activity.objects.all()
    for i in obj:
        if i.user == request.user.username and i.id == int(i_d):
            i.returned = True
            i.save()
            a = i.asset_tracking_id
            a.active_item = True
            a.save()
    return redirect('/')