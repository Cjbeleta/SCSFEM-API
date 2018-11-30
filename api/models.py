from django.db import models

# Create your models here.

class Token(models.Model):
    token = models.CharField(max_length=2000)
    ttl = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.token, self.ttl)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    token_id = models.ForeignKey(Token, null=True, on_delete=models.CASCADE)
    usertype = models.IntegerField(null=False, default=2)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.email, self.usertype)

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
    description = models.TextField(default='None')
    image = models.TextField(default='https://images.unsplash.com/photo-1522165078649-823cf4dbaf46?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=756f069c98c96a701453b1e27630e961&auto=format&fit=crop&w=750&q=80')
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.borrower_id)

class Equipment(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(default='None')
    image = models.TextField(default='https://images.unsplash.com/photo-1531988042231-d39a9cc12a9a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a562d48d64fd49e7cd0419f70806d696&auto=format&fit=crop&w=750&q=80')
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    quantity = models.IntegerField(default=1)
    borrower_id = models.ForeignKey(Borrower, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.status, self.quantity, self.borrower_id)

class Reservation(models.Model):
    borrower_id = models.ForeignKey(Borrower, null=False, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Facility, null=False, on_delete=models.CASCADE)
    reservation_type = models.IntegerField()
    date_application = models.DateField(auto_now_add=True)
    date_reservation_start = models.DateField()
    date_reservation_end = models.DateField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.borrower_id, self.item_id, self.date_application, self.status)
