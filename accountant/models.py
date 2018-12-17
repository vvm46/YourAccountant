from django.db import models


class Title(models.Model):
	class Meta:
		verbose_name = 'Головна'
		verbose_name_plural = 'Головна'

	title = models.CharField(max_length=255, blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, blank=True)

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

	def __str__(self):
		return self.title
