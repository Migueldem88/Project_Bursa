from django.db import models

class ProductTable(models.Model):
    column2 = models.IntegerField('Unnamed: 0.1',blank=True,null=True)
    column3 = models.IntegerField('Unnamed: 0', blank=True,null=True)
    name = models.CharField('pname', max_length=100,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    store = models.CharField(max_length=100,blank=True,null=True)
    pcode = models.IntegerField(blank=True,null=True)
    ru_pname = models.CharField(max_length=200,blank=True,null=True)
    en_pname = models.CharField(max_length=200, blank=True, null=True)
    conames = models.CharField(max_length=300, blank=True, null=True)


    class Meta:
        verbose_name = 'Product List'
        verbose_name_plural = 'Product Lists'
        ordering = ['-name']


    def __str__(self):
        return str(self.id) + '-'+self.en_pname + '-' + str(self.price)