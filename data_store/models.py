from django.db import models


class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('fab_manager', 'Fabricator Manager'),
        ('sub_assembly_manager', 'Sub Assembly Manager'),
        ('assembly_manager', 'Assembly Manager'),
        ('fab_operator', 'Fabricator Operator'),
        ('sub_assembly_operator', 'Sub Assembly Operator'),
        ('assembly_operator', 'Assembly Operator'),
    ]

    ROLE_ID = [
        ('admin', 'a1R'),
        ('user', 'u1R'),
        ('fab_manager', 'fm1R'),
        ('sub_assembly_manager', 'sam1R'),
        ('assembly_manager', 'am1R'),
        ('fab_operator', 'fo1R'),
        ('sub_assembly_operator', 'sao1R'),
        ('assembly_operator', 'ao1R'),
    ]
    role_id = models.CharField(primary_key=True, choices=ROLE_ID, max_length=50)
    role_name = models.CharField(max_length=50, choices=ROLE_CHOICES, )


class Item(models.Model):
    ITEM_CHOICES = [
        ('tub', 'Tub'),
        ('pump', 'Pump'),
        ('spintube', 'Spin Tub'),
        ('washtube', 'Wash Tub'),
        ('balancering', 'Balance Ring'),
        ('transmissiongear', 'Transmission Gears'),
        ('plasticbracket', 'Plastic Brackets'),

    ]

    ITEM_ID = [
        ('tub', 't1I'),
        ('pump', 'p1I'),
        ('spintube', 'st1I'),
        ('washtube', 'wt1I'),
        ('balancering', 'br1I'),
        ('transmissiongear', 'tg1I'),
        ('plasticbracket', 'pb1I'),
    ]

    item_id = models.CharField(primary_key=True, max_length=50, choices=ITEM_ID)
    item_name = models.CharField(max_length=50, choices=ITEM_CHOICES)


class User(models.Model):
    user_id = models.CharField(primary_key=True, null=False, default="", max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Machine(models.Model):
    machine_id = models.CharField(primary_key=True, max_length=50)
    machine_name = models.CharField(max_length=50)


class Fabrication(models.Model):
    fabrication_id = models.CharField(primary_key=True, max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    sdate = models.DateField(auto_now_add=True)
    edate = models.DateField(auto_now=True)
    approval_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default="",
                                    related_name='fabrication_approvals')
    approval_status = models.CharField(max_length=50, default='Pending')
    worker_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='fabrication_worker')


class SubAssembly(models.Model):
    subassembly_id = models.CharField(primary_key=True, max_length=50)
    sub_process = models.ForeignKey('SubProcess', on_delete=models.CASCADE, default="")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    sdate = models.DateField(auto_now_add=True)
    edate = models.DateField(auto_now=True)
    approval_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default="",
                                    related_name='subassembly_approvals')
    approval_status = models.CharField(max_length=50, default='Pending')
    worker_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='subassembly_worker')


class Assembly(models.Model):
    assembly_id = models.CharField(primary_key=True, max_length=50)
    process = models.ForeignKey('AssemblyProcess', on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    sdate = models.DateField(auto_now_add=True)
    edate = models.DateField(auto_now=True)
    approval_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default="",
                                    related_name='assembly_approvals')
    approval_status = models.CharField(max_length=50, default='Pending')
    worker_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='assembly_worker')


class AssemblyProcess(models.Model):
    PROCESS_CHOICES = [
        ('componentintegration', 'Component Integration'),
        ('electricaltesting', 'Electrical Testing'),
        ('compliance', 'Complaince'),
        ('certificationstandard', 'Certification Standards'),
        ('pivotdome', 'Pivot Dome'),
        ('powdercoatingprocess', 'Powder Coating Process'),
        ('testingandinspection', 'Testing and Inspection'),

    ]

    PROCESS_ID = [
        ('componentintegration', 'ca1AP'),
        ('electricaltesting', 'et1AP'),
        ('compliance', 'c1AP'),
        ('certificationstandard', 'cs1AP'),
        ('pivotdome', 'pd1AP'),
        ('powdercoatingprocess', 'pcp1AP'),
        ('testingandinspection', 'tai1AP'),
    ]

    process_id = models.CharField(primary_key=True, choices=PROCESS_ID, max_length=50)
    process = models.CharField(max_length=50, choices=PROCESS_CHOICES, )


class SubProcess(models.Model):
    SUBPROCESS_CHOICES = [
        ('transmissionassembly', 'Transmission Assembly'),
        ('electricalassembly', 'Electrical Assembly'),
        ('tubassemblies', 'Tub assemblies'),
        ('mechanicalassembly', 'Mechanical assembly'),
        ('weldassembly', 'Weld Assembly'),
        ('sportweldassembly', 'Spot Weld Assembly'),

    ]

    SUBPROCESS_ID = [
        ('transmissionassembly', 'ta1P'),
        ('electricalassembly', 'ea1P'),
        ('tubassemblies', 'ta2P'),
        ('mechanicalassembly', 'ma1P'),
        ('weldassembly', 'wa1P'),
        ('sportweldassembly', 'swa1P'),
    ]

    sub_process_id = models.CharField(primary_key=True, choices=SUBPROCESS_ID, max_length=50, default="val")
    sub_process = models.CharField(max_length=50, choices=SUBPROCESS_CHOICES, default="val")
