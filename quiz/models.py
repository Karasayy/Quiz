from django.db import models

class Theme(models.Model):
    theme_name = models.CharField(max_length=100, blank=True, null=True)
    theme_img = models.ImageField(blank=True)

    def __str__(self):
        return self.theme_name

class QuizModel(models.Model):

    question = models.CharField(max_length=200, null=True, blank=True)
    op1 = models.CharField(max_length=200, null=True, blank=True)
    op2 = models.CharField(max_length=200, null=True, blank=True)
    op3 = models.CharField(max_length=200, null=True, blank=True)
    op4 = models.CharField(max_length=200, null=True, blank=True)
    ans = models.CharField(max_length=200, null=True, blank=True)
    theme = models.ForeignKey(Theme, null=True, on_delete=models.CASCADE, related_name='theme')
    
    def __str__(self):
        return self.question


    