from django.db import models

# Create your models here.
class Feature:
    id: int
    name: str
    details: str
    image_path: str
    is_legal: bool