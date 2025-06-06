from django.db import models

from accounts.models import User


class Advertisement(models.Model):
    class PositionTypes(models.TextChoices):
        CENTER = "Center"
        LEFT = "Left"
        RIGHT = "Right"
        BIG_SLIDER = "Big Slider"
        SLIDER_BOX_1 = "Slider Box 1"
        SLIDER_BOX_2 = "Slider Box 2"
        SLIDER_BOX_3 = "Slider Box 3"

    position = models.CharField(choices=PositionTypes.choices, max_length=50)
    link = models.URLField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="advertisements/")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="advertisements"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} - {'Active' if self.is_active else 'Inactive'}"
