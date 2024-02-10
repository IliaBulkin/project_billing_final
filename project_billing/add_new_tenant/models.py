from django.db import models

# Create your models here.
class Client(models.Model):
    shopping_center = models.CharField(max_length = 255) # под торговый комплекс
    number_contract = models.CharField(max_length = 255, default=None) # под номер договора
    start_contract = models.DateField() # под начало договора
    data_to = models.DateField() # под дата по
    data_contract = models.DateField() # под дата договора
    landlord = models.CharField(max_length = 255) # под арендодатель
    tenant = models.CharField(max_length = 255) # под арендатор
    landlordPC = models.CharField(max_length = 255, null=True, blank=True, default=None) # под арендодатель пс
    type_contract = models.CharField(max_length = 255) # под тип договора
    advertising_tax = models.CharField(max_length = 255, null=True, blank=True, default=None) # под налог на рекламу
    working = models.CharField(max_length = 255, null=True, blank=True, default=None) # под в работе
    closed = models.CharField(max_length = 255, null=True, blank=True, default=None) # под закрыт(архив)
    comment = models.CharField(max_length = 255, default=None) # под комментарий
    number_contract_count = models.CharField(max_length = 255, default=None) # под номер договора в счете
    main_contract = models.CharField(max_length = 255) # под основной договор
    main_lot = models.CharField(max_length = 255, default=None) # под основной лот