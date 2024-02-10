from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from .models import *
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def reg(request):
    context = {}
    return render(request, 'add_new_tenant/reg.html', context)
@csrf_exempt
def main(request):
    context = {}
    if request.method == 'POST':
        shopping_center1 = request.POST.get("shopping_center")
        number_contract1 = request.POST.get("number_contract")
        start_contract1 = request.POST.get("start_contract")
        data_to1 = request.POST.get("data_to")
        data_contract1 = request.POST.get("data_contract")
        landlord1 = request.POST.get("landlord")
        tenant1 = request.POST.get("tenant")
        landlordPC1 = request.POST.get("landlordPC")
        type_contract1 = request.POST.get("type_contract")
        advertising_tax1 = request.POST.get("advertising_tax")
        working1 = request.POST.get("working")
        closed1 = request.POST.get("closed")
        comment1 = request.POST.get("comment")
        number_contract_count1 = request.POST.get("number_contract_count")
        main_contract1 = request.POST.get("main_contract")
        main_lot1 = request.POST.get("main_lot")
        client_info = Client.objects.create(shopping_center=shopping_center1, 
                                            number_contract=number_contract1,
                                            start_contract=start_contract1,
                                            data_to= data_to1,
                                            data_contract=data_contract1,
                                            landlord=landlord1, 
                                            tenant=tenant1, 
                                            landlordPC=landlordPC1,  
                                            type_contract= type_contract1,
                                            advertising_tax = advertising_tax1,
                                            working=working1,
                                            closed=closed1,
                                            comment=comment1,
                                            number_contract_count=number_contract_count1,
                                            main_lot=main_lot1,
                                            main_contract=main_contract1)
        client_info.save()
        # if 'logout' in request.POST:
        #     logout(request)
        #     return redirect('reg')

    return render(request, 'add_new_tenant/main.html', context)
@csrf_exempt
def ajax(request):
    
    context = {}
    
    if request.method == 'POST':
        username1 = request.POST.get('login')
        password1 = request.POST.get('password')

        
        if request.POST.get('type') == 'reg':
            username = request.POST.get('login')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            if username and password and first_name:
                try:
                    User.objects.create_user(username=username, password=password, first_name=first_name)
                    
                except IntegrityError:
                    context['error'] = 'Користувач з такими даними вже існує!'
            else:
                context['error'] = 'Заповніть всі поля!'
                
        elif request.POST.get('type') == 'log':
            if username1 and password1:
                user = authenticate(username=username1, password=password1)
                if user:
                    login(request, user)
                else:
                    context['error'] = 'Такого користувача не знайдено!'
            else:
                context['error'] = 'Заповніть всі поля!'
    
    return JsonResponse(context)