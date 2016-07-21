from django.db import models
from django.utils import timezone

class VersusFinder(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	match_date = models.DateTimeField()
	team_photo_path = models.TextField()
	manager_phone_number = models.TextField()
	invite_playground_name = models.TextField()

	def PostTeamFind(self):
		self.create_date = timezone.now()

	def __str__(self):
		return self.title