from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Project(models.Model):
    image = CloudinaryField(
        'image',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'bmp'])]
    )

    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contributors = models.CharField(max_length=300, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title if self.title else "Untitled Project"
    

class ProgressStat(models.Model):
    icon_class = models.CharField(
        max_length=100, 
        help_text="FontAwesome icon class (e.g., 'fas fa-user-graduate')"
    )
    value = models.CharField(
        max_length=50, 
        help_text="The number or text to display (e.g., '40+')"
    )
    label = models.CharField(
        max_length=100, 
        help_text="The label below the number (e.g., 'Active Researchers')"
    )
    order = models.IntegerField(
        default=0, 
        help_text="Controls the display order (lower numbers appear first)"
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.label} ({self.value})"
    

class Publication(models.Model):
    TYPE_CHOICES = [
        ('Conference', 'Conference'),
        ('Journal', 'Journal'),
        ('Preprint', 'Preprint'),
        ('Workshop', 'Workshop'),
    ]
    
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Under Review', 'Under Review'),
        ('Upcoming', 'Upcoming'),
        ('Published', 'Published'),
        ('Accepted with minor revision', 'Accepted with minor revision'),
    ]

    image = CloudinaryField(
        'image',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]
    )
    
    title = models.CharField(max_length=300, blank=True, null=True)
    authors = models.CharField(max_length=300, blank=True, null=True)
    paper_link = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)

    pub_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Conference')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Published')
    is_featured = models.BooleanField(default=False, help_text="Show in the Featured Publications section")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title if self.title else "Untitled Publication"
    


class TeamMember(models.Model):
    DESIGNATION_CHOICES = [
        ('Advisor', 'Advisory Panel'),
        ('PI', 'Principal Investigator'),
        ('Investigator', 'Investigator'),
        ('Mentor', 'Research Mentor'),
        ('RA', 'Research Assistant'),
        ('URA', 'Undergraduate Research Assistant'),
    ]
    image = CloudinaryField(
        'image',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        blank=True, 
        null=True
    )
    
    name = models.CharField(max_length=200)
    lab_designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    self_designation = models.CharField(max_length=200, help_text="e.g., Professor of CSE, Data Scientist")

    email = models.EmailField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    order = models.IntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.get_lab_designation_display()}"
    

class LabInformation(models.Model):
    email = models.EmailField(default="contact@dipanchallab.org")
    phone = models.CharField(max_length=20, default="+880 1234-567890")
    address = models.TextField(default="Sylhet, Bangladesh")
    office_hours = models.CharField(max_length=100, default="Mon-Fri, 9:00 AM - 5:00 PM (Asia/Dhaka)")

    class Meta:
        verbose_name_plural = "Lab Information"

    def __str__(self):
        return "Primary Lab Contact Information"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    admin_reply = models.TextField(blank=True, null=True, help_text="Write your reply here and click 'Save'. An email will be sent directly to the user.")
    is_replied = models.BooleanField(default=False, help_text="Automatically checked when a reply is sent.")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"