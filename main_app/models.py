from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.urls.base import reverse # type: ignore

def user_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
		return 'user_{0}/{1}'.format(instance.user.id, filename)

COMMENTS_RECOMMEND = (
    ('D', 'Not Recommended'),
    ('N', 'Neutral'),
    ('R', 'Recommended')
)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    instructions = models.TextField()
    servings = models.IntegerField()
    imageurl = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
      
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'recipe_id': self.id})
    
    
class Comment(models.Model):
    recommended = models.CharField(
        max_length=1,
        choices=COMMENTS_RECOMMEND,
        default=COMMENTS_RECOMMEND[0][0]
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recipe.name}'
      
    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
    
