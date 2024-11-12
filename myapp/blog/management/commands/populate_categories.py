from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "This commands inserts category data"

    def handle(self, *args: Any,**options: Any):
        # delete existing data
        Category.objects.all().delete()
        
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE blog_category AUTO_INCREMENT = 1;")
            
        categories = ['Sports','Technology','Science',"Art","Food"]

        for category_name in categories:
            Category.objects.create(name = category_name)

