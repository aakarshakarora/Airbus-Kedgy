import datetime
import json

from data_store.models import Item, Machine, AssemblyProcess, SubProcess, User, Fabrication, SubAssembly, Assembly


def get_datetime_string(format='DDMMYY_HHMMSS'):
    now = datetime.datetime.now()
    return now.strftime(format)


def common_form_data():
    # Assuming you want to fetch the respective fields for all objects in the models

    # Fetching item_name
    item_name = [choice[1] for choice in Item.ITEM_CHOICES]

    # Fetching machine_name
    machine_name = list(Machine.objects.values_list('machine_name', flat=True))

    # Fetching assembly_process
    assembly_process = list(AssemblyProcess.objects.values_list('process', flat=True))

    # Fetching sub_process
    sub_process = list(SubProcess.objects.values_list('sub_process', flat=True))

    mp = {
        'Item': item_name,
        'Machine Name': machine_name,
        'Assembly Process': assembly_process,
        'Sub Process': sub_process
    }

    return json.dumps(mp, indent=2)


def fetch_role_by_username(username):
    try:
        user = User.objects.get(username=username)
        role = user.role.role_name
        return role
    except User.DoesNotExist:
        return None


def status_fab_form(status):
    pending_forms = Fabrication.objects.filter(approval_status=status)

    pending_forms_data = []
    for form in pending_forms:
        form_data = {
            'fabrication_id': form.fabrication_id,
            'item': form.item.item_name,
            'machine': form.machine.machine_name,
            'sdate': form.sdate,
            'edate': form.edate,
            'approval_timestamp': form.approval_timestamp,
            'approved_by': form.approved_by.username if form.approved_by else None,
            'worker_name': form.worker_name.username if form.worker_name else None,
            'approval_status': form.approval_status,
        }
        pending_forms_data.append(form_data)

    if pending_forms_data:
        response = {'status': True, 'msg': "Data Fetched", 'output': pending_forms_data}
        return response
    else:
        response = {'status': False, 'msg': "No Pending request", 'output': pending_forms_data}
        return response


def status_sub_assembly(status):
    pending_forms = SubAssembly.objects.filter(approval_status=status)
    pending_forms_data = []

    for form in pending_forms:
        form_data = {
            'subassembly_id': form.subassembly_id,
            'sub_process': form.sub_process.sub_process,
            'fabrication': form.fabrication.fabrication_id,
            'item': form.item.item_name,
            'machine': form.machine.machine_name,
            'sdate': form.sdate,
            'edate': form.edate,
            'approval_timestamp': form.approval_timestamp,
            'approved_by': form.approved_by.username if form.approved_by else None,
            'worker_name': form.worker_name.username if form.worker_name else None,
            'approval_status': form.approval_status,
        }
        pending_forms_data.append(form_data)

    if pending_forms_data:
        response = {'status': True, 'msg': "Data Fetched for Sub Assembly Process", 'output': pending_forms_data}
        return response
    else:
        response = {'status': False, 'msg': "No Pending request for Sub Assembly Process", 'output': pending_forms_data}
        return response


def status_assembly(status):
    pending_forms = Assembly.objects.filter(approval_status=status)
    pending_forms_data = []

    for form in pending_forms:
        form_data = {
            'assembly_id': form.assembly_id,
            'process': form.process.process,
            'machine': form.machine.machine_name,
            'sdate': form.sdate,
            'edate': form.edate,
            'approval_timestamp': form.approval_timestamp,
            'approved_by': form.approved_by.username if form.approved_by else None,
            'worker_name': form.worker_name.username if form.worker_name else None,
            'approval_status': form.approval_status,
        }
        pending_forms_data.append(form_data)

    if pending_forms_data:
        response = {'status': True, 'msg': "Data Fetched for Assembly Process", 'output': pending_forms_data}
        return response
    else:
        response = {'status': False, 'msg': "No Pending request for Assembly Process", 'output': pending_forms_data}
        return response
