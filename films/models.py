from django.db import models


class Film(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return f'{self.description[:50]}...'


class Screening(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	date_time = models.DateTimeField()

	def __str__(self):
		return f'{self.film.title} at {self.date_time: %I:%M %p} on {self.date_time: %d/%m/%y }'
