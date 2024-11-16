from django.db import models


class ProductQuery(models.Model):
    query = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
