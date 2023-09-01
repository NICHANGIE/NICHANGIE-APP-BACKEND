from django.db import models

from users.models import CustomUser


class FundraisingCampaign(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(
        help_text='Number of days the campaign will run'
    )
    targeted_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Targeted fundraising amount'
    )
    document_proof = models.FileField(
        upload_to='campaigns/',
        help_text='Document proof for the campaign'
    )
    description = models.TextField(
        help_text='Description of the fundraising campaign'
    )
    # photo_image = models.ImageField(
    #     upload_to='campaigns/',
    #     help_text='Photo image for the campaign'
    # )
    hospital_account_details = models.TextField(
        help_text='Hospital account details for donations'
    )
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text='User who created the campaign'
    )

    def __str__(self):
        return self.name
    
