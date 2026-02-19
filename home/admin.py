from django.contrib import admin
from .models import Project, ProgressStat, Publication, TeamMember, LabInformation, ContactMessage
from django.core.mail import send_mail
from django.conf import settings

admin.site.register(Project)
admin.site.register(ProgressStat)
admin.site.register(Publication)
admin.site.register(TeamMember)

admin.site.register(LabInformation)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_replied', 'created_at')
    list_filter = ('is_replied', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at', 'is_replied')
    search_fields = ('name', 'email', 'subject')

    def save_model(self, request, obj, form, change):
        if change and obj.admin_reply and not obj.is_replied:
            send_mail(
                subject=f"Re: {obj.subject} - Dipanchal Innovation Lab",
                message=obj.admin_reply,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[obj.email],
                fail_silently=False,
            )
            obj.is_replied = True
            
        super().save_model(request, obj, form, change)