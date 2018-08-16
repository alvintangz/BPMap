from django.db import models

class Trip(models.Model):
	name = CharField('trip name', max_length=200)
	start_date = DateField('start of trip')
	end_date = DateField('end of trip')

class City(models.Model):
	name = CharField('city name', max_length=200)
	description = TextField('description', null=True)
	cover_photo = ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	longitude = DecimalField('longitude', max_digits=9, decimal_places=6)
	latitude = DecimalField('latitude', max_digits=9, decimal_places=6)

class Blog(models.Model):
	trip = ForeignKey(Trip, on_delete=models.PROTECT)
	city = ForeignKey(City, on_delete=models.PROTECT)
	title = CharField('title', max_length=500)
	author = ForeignKey(Author, on_delete=models.PROTECT)
	body_text = TextField('body')
	views = IntegerField('number of views')
	cover_photo = ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	creation_date = DateTimeField('creation time and date')
	last_update = DateTimeFIeld('last updated')

class Video(models.Model):
	trip = ForeignKey(Trip, on_delete=models.PROTECT)
	city = ForeignKey(City, on_delete=models.PROTECT)
	title = CharField('title', max_length=500)
	author = ForeignKey(Author, on_delete=models.PROTECT)
	video = URLField('video', help_text="Add the embedded player URL (https://www.youtube.com/embed/VIDEO_ID)")
	views = IntegerField('number of views')
	cover_photo = ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	creation_date = DateTimeField('creation time and date')
	last_update = DateTimeFIeld('last updated')

class PhotoGroup(models.Model):
	trip = ForeignKey(Trip, on_delete=models.PROTECT)
	city = ForeignKey(City, on_delete=models.PROTECT)
	title = CharField('title', max_length=500)
	author = ForeignKey(Author, on_delete=models.PROTECT)
	views = IntegerField('number of views')
	cover_photo = ImageField('cover photo', height_field=500, width_field=500, help_text="Add a cover photo that is 500x500 in size")
	creation_date = DateTimeField('creation time and date')
	last_update = DateTimeFIeld('last updated')

class Photo(models.Model):
	photo = ImageField('photo')
	caption = TextField('caption')
	photo_group = ForeignKey(PhotoGroup, on_delete=models.CASCADE)
