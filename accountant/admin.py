from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django.template.defaultfilters import mark_safe
from accountant.models import Title, Services, AboutUs, Specialization, Advantages, HowWeWork, ComplexServices, \
    Contacts, Applications, Activities, OrganizationalForm, TaxSystem


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


class HowWeWorkAdmin(TabbedTranslationAdmin):
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


class ComplexServicesAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title_uk', 'subtitle_uk', 'additionally_uk', 'enabled']
    list_display_links = ['id', 'title_uk', 'subtitle_uk', 'additionally_uk']
    list_editable = ['enabled']


class ContactsAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'time_of_work_uk', 'street_uk', 'email', 'phones', 'map', 'company_footer_uk', 'enabled']
    list_display_links = ['id', 'time_of_work_uk', 'street_uk', 'email', 'phones']
    list_editable = ['enabled']


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'activity', 'organizational_form', 'tax_system', 'created']
    list_display_links = ['id', 'name', 'phone', 'email', 'activity', 'organizational_form', 'tax_system']
    readonly_fields = ['created']


class ActivitiesAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title_uk', 'created']
    list_display_links = ['id', 'title_uk', 'created']
    readonly_fields = ['created']


class OrganizationalFormAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title_uk', 'created']
    list_display_links = ['id', 'title_uk', 'created']
    readonly_fields = ['created']


class TaxSystemAdmin(TabbedTranslationAdmin):
    list_display = ['id', 'title_uk', 'created']
    list_display_links = ['id', 'title_uk', 'created']
    readonly_fields = ['created']


admin.site.register(Title, TitleAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Advantages, AdvantagesAdmin)
admin.site.register(HowWeWork, HowWeWorkAdmin)
admin.site.register(ComplexServices, ComplexServicesAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(OrganizationalForm, OrganizationalFormAdmin)
admin.site.register(TaxSystem, TaxSystemAdmin)
