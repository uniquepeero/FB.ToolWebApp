from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'


class AdAcc(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} of {self.user}'


class Campaign(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128, db_index=True)
    clicks = models.IntegerField()
    spend = models.FloatField()
    cost_per_click = models.FloatField()
    installs = models.IntegerField()
    cost_per_install = models.FloatField()
    regs = models.IntegerField()
    cost_per_reg = models.FloatField()
    purchases = models.IntegerField()
    cost_per_purchase = models.FloatField()
    adacc = models.ForeignKey(AdAcc, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} of {self.adacc}'


class AdSet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128, db_index=True)
    clicks = models.IntegerField()
    spend = models.FloatField()
    cost_per_click = models.FloatField()
    installs = models.IntegerField()
    cost_per_install = models.FloatField()
    regs = models.IntegerField()
    cost_per_reg = models.FloatField()
    purchases = models.IntegerField()
    cost_per_purchase = models.FloatField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} of {self.campaign}'


class Ad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128, db_index=True)
    clicks = models.IntegerField()
    spend = models.FloatField()
    cost_per_click = models.FloatField()
    installs = models.IntegerField()
    cost_per_install = models.FloatField()
    regs = models.IntegerField()
    cost_per_reg = models.FloatField()
    purchases = models.IntegerField()
    cost_per_purchase = models.FloatField()
    adset = models.ForeignKey(AdSet, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} of {self.adset}'
