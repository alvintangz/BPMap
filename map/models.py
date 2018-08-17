from django.db import models
from accounts.models import Author

class Trip(models.Model):
	name = models.CharField('trip name', max_length=200)
	start_date = models.DateField('start of trip')
	end_date = models.DateField('end of trip')

class City(models.Model):
	name = models.CharField('city name', max_length=200)
	description = models.TextField('description', null=True)
	cover_photo = models.ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	longitude = models.DecimalField('longitude', max_digits=9, decimal_places=6)
	latitude = models.DecimalField('latitude', max_digits=9, decimal_places=6)

class Blog(models.Model):
	trip = models.ForeignKey(Trip, on_delete=models.PROTECT)
	city = models.ForeignKey(City, on_delete=models.PROTECT)
	title = models.CharField('title', max_length=500)
	author = models.ForeignKey(Author, on_delete=models.PROTECT)
	body_text = models.TextField('body')
	views = models.IntegerField('number of views')
	cover_photo = models.ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	creation_date = models.DateTimeField('creation time and date')
	last_update = models.DateTimeField('last updated')

class Video(models.Model):
	trip = models.ForeignKey(Trip, on_delete=models.PROTECT)
	city = models.ForeignKey(City, on_delete=models.PROTECT)
	title = models.CharField('title', max_length=500)
	author = models.ForeignKey(Author, on_delete=models.PROTECT)
	video = models.URLField('video', help_text="Add the embedded player URL (https://www.youtube.com/embed/VIDEO_ID)")
	views = models.IntegerField('number of views')
	cover_photo = models.ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	creation_date = models.DateTimeField('creation time and date')
	last_update = models.DateTimeField('last updated')

class PhotoGroup(models.Model):
	trip = models.ForeignKey(Trip, on_delete=models.PROTECT)
	city = models.ForeignKey(City, on_delete=models.PROTECT)
	title = models.CharField('title', max_length=500)
	author = models.ForeignKey(Author, on_delete=models.PROTECT)
	views = models.IntegerField('number of views')
	cover_photo = models.ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	creation_date = models.DateTimeField('creation time and date')
	last_update = models.DateTimeField('last updated')

class Photo(models.Model):
	photo = models.ImageField('photo')
	caption = models.TextField('caption')
	photo_group = models.ForeignKey(PhotoGroup, on_delete=models.CASCADE)
