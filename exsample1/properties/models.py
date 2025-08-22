from django.db import models

# Create your models here.


class DealRequest(models.Model):
    STATUSES=(('pending','pending'),('approved','approved'),('requested','requested'))
    seeaker = models.ForeingnKey(settings.AUTH_USER, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    message=models.TextField(null=True,blank=True)
    status=models.CharField(max_lenght=20,choices=STATUSES,)

    def __str__(self):
        return f'Deal request {self.pk} for {self.property}'