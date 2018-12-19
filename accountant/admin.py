from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django.template.defaultfilters import mark_safe
from accountant.models import Title, Services, AboutUs, Specialization, Advantages, HowWeWork, ComplexServices, \
	Contacts, Applications


class TitleAdmin(TabbedTranslationAdmin):
	list_display = ['id', 'title_uk', 'created', 'updated', 'enabled']
	list_display_links = ['id', 'title_uk']
	list_editable = ['enabled']
	readonly_fields = ['created', 'updated']


class ServicesAdmin(TabbedTranslationAdmin):
	list_display = ['id', 'title_uk', 'text_uk', 'created', 'updated', 'enabled']
	list_display_links = ['id', 'title_uk', 'text_uk']
	list_editable = ['enabled']
	readonly_fields = ['picture_priview', 'created', 'updated']

	def picture_priview(self, obj):
		try:
			return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
				url=obj.img.url,
				width=obj.img.width,
				height=obj.img.height,
			)
			)
		except FileNotFoundError as e:
			return e


class AboutUsAdmin(TabbedTranslationAdmin):
	list_display = ['id', 'title_uk', 'text_uk', 'description_uk', 'created', 'updated', 'enabled']
	list_display_links = ['id', 'title_uk', 'text_uk', 'description_uk']
	list_editable = ['enabled']
	readonly_fields = ['created', 'updated']


class SpecializationAdmin(TabbedTranslationAdmin):
	list_display = ['id', 'title_uk', 'created', 'updated', 'enabled']
	list_display_links = ['id', 'title_uk']
	list_editable = ['enabled']
	readonly_fields = ['picture_priview', 'created', 'updated']

	def picture_priview(self, obj):
		try:
			return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
				url=obj.img.url,
				width=obj.img.width,
				height=obj.img.height,
			)
			)
		except FileNotFoundError as e:
			return e


class AdvantagesAdmin(TabbedTranslationAdmin):
	list_display = ['id', 'title_uk', 'text_uk', 'created', 'updated', 'enabled']
	list_display_links = ['id', 'title_uk', 'text_uk']
	list_editable = ['enabled']
	readonly_fields = ['picture_priview', 'created', 'updated']

	def picture_priview(self, obj):
		try:
			return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
				url=obj.img.url,
				width=obj.img.width,
				height=obj.img.height,
			)
			)
		except FileNotFoundError as e:
			return e


admin.site.register(Title, TitleAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Advantages, AdvantagesAdmin)
