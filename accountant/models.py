from django.db import models


class Title(models.Model):
	class Meta:
		verbose_name = 'Title'
		verbose_name_plural = 'Titles'

	title = models.CharField(max_length=255, blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return self.title

