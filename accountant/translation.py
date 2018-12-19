from modeltranslation.translator import register, TranslationOptions
from accountant.models import Title, Services, AboutUs, Specialization, Advantages, HowWeWork, ComplexServices, \
	Contacts, Applications


@register(Title)
class TitleTranslationOptions(TranslationOptions):
	fields = ('title',)


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
	fields = ('title', 'text',)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
	fields = ('title', 'text', 'description',)


@register(Specialization)
class SpecializationTranslationOptions(TranslationOptions):
	fields = ('title',)


@register(Advantages)
class AdvantagesTranslationOptions(TranslationOptions):
	fields = ('title', 'text',)


@register(HowWeWork)
class HowWeWorkTranslationOptions(TranslationOptions):
	fields = ('title', 'text',)


@register(ComplexServices)
class ComplexServicesTranslationOptions(TranslationOptions):
	fields = ('title', 'subtitle', 'additionally')


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
	fields = ('time_of_work', 'street', 'company_footer')


