import uuid
from django.db import models
from stdimage import StdImageField
from profiles.utils import get_images_path

from profiles.enums import PlanTypeEnum


# Create your models here.
class Plan(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Plan",
        blank=False
    )
    type_plan = models.CharField(
        max_length=10,
        verbose_name="Modalidad",
        choices=[(tag.name, tag.value) for tag in PlanTypeEnum],
        default=PlanTypeEnum.MONTHLY
    )
    image =StdImageField(
        upload_to=get_images_path,
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        verbose_name='Monto',
        max_digits=6,
        decimal_places=2
    )
    max_suscriptors = models.SmallIntegerField(
        verbose_name='Máximo de suscriptores',
        default=0
    )
    is_selected = models.BooleanField(
        verbose_name="Selección",
        default=False    
    )

    class Meta:
        db_table = "plan"
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.name