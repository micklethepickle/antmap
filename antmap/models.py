from django.db import models
from datetime import datetime

class Species(models.Model):
	family = models.CharField(_('Family'), max_length=128, blank=True)
	genus = models.CharField(_('Genus'), max_length=200, blank=True)
	species = models.CharField(_('Species'), max_length=128, blank=True)

	def __unicode__():
		return self.species

class Ant(models.Model):
	date = models.DateField(_('Date'), default=datetime.date.min, blank=True))
	owner = models.CharField(_('Owner'), max_length=128, blank=True)
	
	#location info
	country = models.CharField(_('Country'), max_length=128, blank=True)
        state_province = models.CharField(_('State or Province'), max_length=200, blank=True)	
	city = models.CharField(_('City'), max_length=128, blank=True)	
	landmark = models.CharField(_('Landmark of Location'), max_length=128, blank=True)
	description = models.CharField(_('Habitat Description'), max_length=500, blank=True)
        GPS_lat = models.CharField(_('Latitude'), default='0', blank=True)
        GPS_long = models.CharField(_('Longitude'), default='0', blank=True))
        ID_date = models.DateField(_('ID Date'), default=datetime.date.min, blank=True)
        ID = models.CharField(_('ID'), max_length=128, blank=True)
	
	discoverery = models.CharField(_('Discoverer'), max_length=128, blank=True)
	species = models.ForeignKey(Species, blank=True)
	specimen_ID = models.CharField(_('Specimen ID'), max_length=128, blank=True) 
		
	def __unicode__(self):
		return self.species
	

