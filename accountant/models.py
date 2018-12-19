from django.db import models


class Title(models.Model):
    class Meta:
        verbose_name = 'Головна'
        verbose_name_plural = 'Головна'

    title = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class Services(models.Model):
    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'

    title = models.CharField(max_length=255, blank=False, null=False)
    img = models.ImageField(max_length=255, default='', blank=True, null=True)
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'

    title = models.CharField(max_length=255, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class Specialization(models.Model):
    class Meta:
        verbose_name = 'Наша спеціалізація'
        verbose_name_plural = 'Наша спеціалізація'

    img = models.ImageField(max_length=255, default='', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class Advantages(models.Model):
    class Meta:
        verbose_name = 'Перевага співпраці'
        verbose_name_plural = 'Переваги співпраці'

    img = models.ImageField(max_length=255, default='', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class HowWeWork(models.Model):
    class Meta:
        verbose_name = 'Як ми працюємо'
        verbose_name_plural = 'Як ми працюємо'

    img = models.ImageField(max_length=255, default='', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class ComplexServices(models.Model):
    class Meta:
        verbose_name = 'Комплексне обслуговування'
        verbose_name_plural = 'Комплексне обслуговування'

    title = models.CharField(max_length=555, blank=False, null=False)
    subtitle = models.TextField(blank=False, null=False, default=None)
    additionally = models.TextField(blank=False, null=False, default=None)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.title


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакти'
        verbose_name_plural = 'Контакти'

    time_of_work = models.CharField(max_length=255, blank=False, null=False, default=None)
    street = models.CharField(max_length=255, blank=False, null=False, default=None)
    email = models.EmailField()
    phones = models.CharField(max_length=255, blank=False, null=False, default=None)
    company_footer = models.CharField(max_length=455, blank=False, null=False, default=None)
    map = models.URLField(blank=False, null=False)
    enabled = models.BooleanField(default=False, help_text='Дозволити відображати на сайті')

    def __str__(self):
        return self.time_of_work


class Applications(models.Model):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    name = models.CharField(max_length=155, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    activity = models.CharField(max_length=555, blank=True, null=True)
    organizational_form = models.CharField(max_length=555, blank=True, null=True)
    tax_system = models.CharField(max_length=555, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Activities(models.Model):
    class Meta:
        verbose_name = 'Вид діяльності'
        verbose_name_plural = 'Види діяльності'

    title = models.CharField(max_length=555, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class OrganizationalForm(models.Model):
    class Meta:
        verbose_name = 'Організаційна форма'
        verbose_name_plural = 'Організаційні форми'

    title = models.CharField(max_length=555, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class TaxSystem(models.Model):
    class Meta:
        verbose_name = 'Система опадаткування'
        verbose_name_plural = 'Системи опадаткування'

    title = models.CharField(max_length=555, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
