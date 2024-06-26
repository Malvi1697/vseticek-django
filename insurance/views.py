from django.shortcuts import render
from insurance.models import InsuranceSubject
from insurance.forms import InsuranceSubjectForm



def insurance_home(request):
    context = {}
    form = InsuranceSubjectForm()
    all_subjects = InsuranceSubject.objects.all()
    context['all_subjects'] = all_subjects
    context['page_title'] = "Insurance Home"
    context['form'] = form
    return render(request, 'insurance/index.html', context)
