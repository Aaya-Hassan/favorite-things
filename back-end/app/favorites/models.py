from django.db import models


class Category(models.Model):
    """
      Represent a Category model.
      """
    title = models.CharField(max_length=10, null=False)


class Favorite(models.Model):
    """
      Represent a Favorite model.
      """
    title = models.CharField(max_length=255, null=False, blank=False,
                             unique=True)
    description = models.CharField(max_length=300, null=False)
    ranking = models.IntegerField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # history = AuditlogHistoryField()