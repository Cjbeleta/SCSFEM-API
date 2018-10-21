from django.db import models

# Create your models here.

class Token(models.Model):
    token = models.CharField(max_length=2000)
    ttl = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.token, self.ttl)

class Superadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Subadmin(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Borrower(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.token_id)

class Facility(models.Model):
    name = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.borrower_id)

class Equipment(models.Model):
    name = models.CharField(max_length=70)
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField(default=1)
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.quantity, self.borrower_id)