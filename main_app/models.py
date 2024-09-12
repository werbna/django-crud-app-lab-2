from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

def user_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
		return 'user_{0}/{1}'.format(instance.user.id, filename)

#Create mode for recipes
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    instructions = models.TextField()
    servings = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to ='user_directory_path')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
						return self.name