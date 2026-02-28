from django.db import models

class Category(models.Model):
    name = models.CharField("Категория атауы", max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Жаңалықтың тақырыбы", max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name="Категория")
    description = models.TextField("Жаңалықтың сипаттамасы")
    image_url = models.CharField("Жаңалықтың сурет URL-і", max_length=500)
    created_at = models.DateTimeField("Жаңалықтың жариялану уақыты", auto_now_add=True)

    def __str__(self):
        return self.title

class Advertising(models.Model):
    name = models.CharField("Жарнаманың атауы", max_length=255, default="Жарнама")
    image_url = models.CharField("Жарнаманың сурет URL-і", max_length=500)

    def __str__(self):
        return self.name
