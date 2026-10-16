from django.db import models

# Create your models here.
# schema:QuestionDB
# fields:title,language,notes,difficulty_level,sample_input.....
class QuestionDB(models.Model):
    title = models.CharField(max_length=200)
    LANGUAGE_CHOICES = (
        ("python","Python"),
        ("java","Java"),
        ("javascript","Javascript")

    )
    language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="Python")

    DIFFICULTY_CHOICES = (
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )
    difficulty_level = models.CharField(max_length=100,choices=DIFFICULTY_CHOICES,default = "python")
    topic = models.CharField(max_length=100)
    notes = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)





