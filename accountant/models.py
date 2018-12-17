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

	text = models.TextField(blank=False, null=False)

