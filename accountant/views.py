
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.generic import TemplateView, ListView, FormView, DetailView
from accountant.models import Title, Services, AboutUs, Specialization, Advantages, HowWeWork, ComplexServices, \
	Contacts, Applications
from accountant.forms import ApplicationsForm


class TitleView(TemplateView):
	template_name = ''

	def get_context_data(self, **kwargs):
		context = super(TitleView, self).get_context_data(**kwargs)
		context['title'] = Title.objects.last()
		return context


class ServicesView(ListView):
	template_name = ''
	model = Services

	def get_context_data(self, **kwargs):
		context = super(ServicesView, self).get_context_data(**kwargs)
		context['services'] = Services.objects.filter(enabled=True)
		return context


class AboutUsView(TemplateView):
	template_name = ''

	def get_context_data(self, **kwargs):
		context = super(AboutUsView, self).get_context_data(**kwargs)
		context['about_us'] = AboutUs.objects.last()
		return context


class SpecializationView(ListView):
	template_name = ''
	model = Specialization

	def get_context_data(self, **kwargs):
		context = super(SpecializationView, self).get_context_data(**kwargs)
		context['specializations'] = Specialization.objects.filter(enabled=True)
		return context


class AdvantagesView(ListView):
	template_name = ''
	model = Advantages

	def get_context_data(self, **kwargs):
		context = super(AdvantagesView, self).get_context_data(**kwargs)
		context['advantages'] = Advantages.objects.filter(enabled=True)
		return context


class HowWeWorkView(ListView):
	template_name = ''
	model = HowWeWork

	def get_context_data(self, **kwargs):
		context = super(HowWeWorkView, self).get_context_data(**kwargs)
		context['how_we_works'] = HowWeWork.objects.filter(enabled=True)
		return context


class ComplexServicesView(TemplateView):
	template_name = ''
	model = ComplexServices

	def get_context_data(self, **kwargs):
		context = super(ComplexServicesView, self).get_context_data(**kwargs)
		context['complex_service'] = ComplexServices.objects.last()
		return context


class ContactsView(TemplateView):
	template_name = ''
	model = Contacts

	def get_context_data(self, **kwargs):
		context = super(ContactsView, self).get_context_data(**kwargs)
		context['complex_service'] = Contacts.objects.last()
		return context


class ApplicationsView(FormView):
	template_name = ''
	form_class = ApplicationsForm

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
		return super(ApplicationsView, self).get(request, *args, **kwargs)
