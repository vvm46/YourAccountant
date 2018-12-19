from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.generic import TemplateView, ListView, FormView
from accountant.models import Title, Services, AboutUs, Specialization, Advantages, HowWeWork, ComplexServices, \
    Contacts, Applications, Activities, OrganizationalForm, TaxSystem
from accountant.forms import ApplicationsForm


class MainView(FormView):
    template_name = ''

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['title'] = Title.objects.last()
        context['services'] = Services.objects.filter(enabled=True)
        context['about_us'] = AboutUs.objects.last()
        context['specializations'] = Specialization.objects.filter(enabled=True)
        context['advantages'] = Advantages.objects.filter(enabled=True)
        context['how_we_works'] = HowWeWork.objects.filter(enabled=True)
        context['complex_service'] = ComplexServices.objects.last()
        context['contact'] = Contacts.objects.last()
        context['activities'] = Activities.objects.all()
        context['organizational_form'] = OrganizationalForm.objects.all()
        context['tax_systems'] = TaxSystem.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if request.POST:
            form = ApplicationsForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                description = form.cleaned_data['description']
                text = 'Імя:   {0}\nТелефон:   {1}\nПовідомлення:   {2}'.format(name, phone, description)
                try:
                    mail = EmailMessage(
                        name, text, to=['XXX@gmail.com']  # TODO: MUST CHANGE FOR REAL MAIL!!!
                    )
                    mail.send()
                except Exception as e:
                    print(e)
                return JsonResponse({'status': True})
            else:
                return JsonResponse({'status': False, 'message': form.errors['captcha'][0]})
        return super(MainView, self).get(request, *args, **kwargs)


# class ActivitiesView(ListView):
#     model = Activities
#
#     def get_queryset(self):
#         objects = Activities.objects.all()
#         return objects
#
#
# class OrganizationalFormView(ListView):
#     model = OrganizationalForm
#
#     def get_queryset(self):
#         objects = OrganizationalForm.objects.all()
#         return objects
#
#
# class TaxSystemView(ListView):
#     model = TaxSystem
#
#     def get_queryset(self):
#         objects = TaxSystem.objects.all()
#         return objects
