from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from common_util import common_method, constant
from common_util.common_method import status_fab_form, status_sub_assembly, status_assembly, fetch_role_by_username
from data_store.models import SubAssembly, Assembly, Fabrication, Item, Machine, User


def login_index(request):
    logout(request)
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            get_role = common_method.fetch_role_by_username(username)
            parameter = {'status': True, 'msg': 'Login successful', 'username': username, 'role': get_role}
            messages.success(request, parameter.get('msg'))
            return redirect('dashboard')
        else:
            messages.error(request, "Wrong credential")
            return redirect('login')
    else:
        messages.error(request, "Wrong credential")
        return redirect('login')


def dashboard(request):
    print(request.user.username)
    username = request.user.username  # Assuming the user is authenticated
    role = fetch_role_by_username(username)
    return render(request, 'dashboard.html',
                  {'role': role, 'username': username, 'output': common_method.common_form_data()})


def logout_view(request):
    logout(request)
    return JsonResponse({'status': True, 'msg': 'Logout successful'})


def operator_fab_form_res(request):
    print(request)
    if request.method == 'POST':
        item_name = request.POST.get('item')
        machine = request.POST.get('machine')
        worker_name = request.POST.get('worker_name')

        try:
            # Fetch the Item instance based on the item_name
            item = Item.objects.get(item_name=item_name)
            machine = Machine.objects.get(machine_name=machine)
            worker_name = User.objects.get(username=worker_name)


            fab_id = "FAB_" + machine + "_" + common_method.get_datetime_string() + '_' + item.item_id

            status = bool(
                Fabrication.objects.get_or_create(fabrication_id=fab_id, item=item, machine=machine,
                                                  worker_name=worker_name,
                                                  approved_by=" "))

            if status:
                response = {'status': True, 'msg': 'Fabrication entry saved'}
                messages.success(request, response.get('msg'))
                return redirect('dashboard')
            else:
                response = {'status': False, 'msg': 'Fabrication entry not saved'}
                messages.error(request, response.get('msg'))
                return redirect('login')

        except Item.DoesNotExist:
            response = {'status': False, 'msg': 'Invalid item selected'}
            messages.error(request, response.get('msg'))
            return redirect('login')


def operator_subassembly_form_res(request):
    if request.method == 'POST':
        sub_process = request.POST.get('sub_process')
        machine = request.POST.get('machine')
        worker_name = request.POST.get('worker_name')

        subassembly_id = "SAM" + machine + "_" + common_method.get_datetime_string() + '_' + sub_process

        status = bool(
            SubAssembly.objects.get_or_create(subassembly_id=subassembly_id, sub_process=sub_process, machine=machine,
                                              worker_name=worker_name,
                                              approved_by=" "))

        if status:
            response = {'status': True, 'msg': 'SubAssembly entry saved'}
            messages.success(request, response.get('msg'))
            return redirect('dashboard')
        else:
            response = {'status': False, 'msg': 'SubAssembly entry not saved'}
            messages.error(request, response.get('msg'))
            return redirect('login')


def operator_assembly_form_res(request):
    if request.method == 'POST':
        process = request.POST.get('process')
        machine = request.POST.get('machine')
        worker_name = request.POST.get('worker_name')

        assembly_id = "ASM" + machine + "_" + common_method.get_datetime_string() + '_' + process

        status = bool(
            Assembly.objects.get_or_create(assembly_id=assembly_id, process=process, machine=machine,
                                           worker_name=worker_name,
                                           approved_by=" "))

        if status:
            response = {'status': True, 'msg': 'Assembly entry saved'}
            messages.success(request, response.get('msg'))
            return redirect('dashboard')
        else:
            response = {'status': False, 'msg': 'Assembly entry not saved'}
            messages.error(request, response.get('msg'))
            return redirect('login')


def pending_request_status(request):
    username = request.user.username
    get_role = common_method.fetch_role_by_username(username)

    if get_role == "Fabricator Manager":
        return JsonResponse(status_fab_form(constant.pending_key))
    elif get_role == "Assembly Manager":
        return JsonResponse(status_sub_assembly(constant.pending_key))
    elif get_role == "Assembly Manager":
        JsonResponse(status_assembly(constant.pending_key))

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def approved_request_status(request):
    username = request.user.username
    get_role = common_method.fetch_role_by_username(username)

    if get_role == "Fabricator Manager":
        return JsonResponse(status_fab_form(constant.approved_key))
    elif get_role == "Assembly Manager":
        return JsonResponse(status_sub_assembly(constant.approved_key))
    elif get_role == "Assembly Manager":
        JsonResponse(status_assembly(constant.approved_key))

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


