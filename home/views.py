from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Project, ProgressStat, Publication, TeamMember, LabInformation, ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    recent_projects = Project.objects.all()[:3]
    progress_stats = ProgressStat.objects.all()
    recent_pubs = Publication.objects.all()[:2]
    return render(request, 'index.html', {'projects': recent_projects,'progress_stats': progress_stats,'recent_pubs': recent_pubs})

def projects_view(request):
    all_projects = Project.objects.all()
    return render(request, 'ongoingproject.html', {'projects': all_projects})

def research(request): return render(request, 'base.html')

def publications(request):
    query = request.GET.get('q', '')
    pub_type = request.GET.get('type', '')
    year = request.GET.get('year', '')

    pubs = Publication.objects.all()

    if query:
        pubs = pubs.filter(Q(title__icontains=query) | Q(authors__icontains=query))

    if pub_type:
        pubs = pubs.filter(pub_type=pub_type)

    if year:
        pubs = pubs.filter(date__year=year)

    featured_pubs = pubs.filter(is_featured=True)
    all_pubs = pubs.filter(is_featured=False)

    available_years = Publication.objects.dates('date', 'year', order='DESC')
    available_types = Publication.objects.values_list('pub_type', flat=True).distinct()

    context = {
        'featured_pubs': featured_pubs,
        'all_pubs': all_pubs,
        'total_count': pubs.count(),
        'query': query,
        'current_type': pub_type,
        'current_year': year,
        'available_years': available_years,
        'available_types': available_types,
    }
    return render(request, 'publications.html', context)

def resources(request): return render(request, 'base.html')

def team(request):
    members = TeamMember.objects.all()
    
    context = {
        'advisors': members.filter(lab_designation='Advisor'),
        'investigators': members.filter(lab_designation__in=['PI', 'Investigator']),
        'mentors': members.filter(lab_designation='Mentor'),
        'ras': members.filter(lab_designation='RA'),
        'uras': members.filter(lab_designation='URA'),
    }
    return render(request, 'team.html', context)

def contact(request):
    lab_info = LabInformation.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        new_contact = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        admin_email = settings.EMAIL_HOST_USER
        email_body = f"New message from {name} ({email})\n\nSubject: {subject}\n\nMessage:\n{message}"
        
        send_mail(
            subject=f"DiL Portal Alert: New Contact Submission - {subject}",
            message=email_body,
            from_email=admin_email,
            recipient_list=[admin_email],
            fail_silently=True,
        )

        messages.success(request, "Your message has been sent successfully. Our team will get back to you shortly.")
        return redirect('contact')

    return render(request, 'contact.html', {'lab_info': lab_info})
