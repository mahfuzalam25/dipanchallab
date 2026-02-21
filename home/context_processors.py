from .models import LabInformation

def global_lab_settings(request):
    lab_info = LabInformation.objects.first()
    return {
        'global_lab_info': lab_info
    }