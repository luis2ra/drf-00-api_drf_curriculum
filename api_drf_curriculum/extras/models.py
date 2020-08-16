from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Extra(models.Model):
    """Extra model."""
    user = models.ForeignKey(User, 
                            on_delete=models.CASCADE,
                            related_name='extra_education')
    expedition = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField(null=True)

    def __str__(self):
        """Return extra academic education and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'