from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "my_Category"

    name = models.CharField(max_length=20, null=False)
    Explanation = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Article(models.Model):
    class Meta:
        db_table = "my_blog"

    title = models.CharField(max_length=20, null=False)
    Contents = models.CharField(max_length=256, null=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



