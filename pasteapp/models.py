from django.db import models

# Create your models here.
class Paste(models.Model):
	content=models.TextField()
	url=models.CharField(max_length=32,blank=False)
	title=models.CharField(max_length=32,blank=False)
	created_on = models.DateTimeField(auto_now_add=True)
	user=models.CharField(max_length=32,editable=False)
	
	

	def __unicode__(self):
		return self.content or str(self.id)


