import os
#import sys
from antmap.models import Ant, Species

def populate(main_dict):
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ants.settings')
	species = add_species(main_dict)
	add_ant(species, main_dict)

def add_species(main_dict):
	species = Species.objects.get_or_create(family=main_dict["family"], genus=main_dict["genus"],species=main_dict["species"])[0]
	return species
	
def add_ant(species, main_dict):
	ant = Ant.objects.get_or_create(date=main_dict["date"], owner=main_dict["owner"], collection=main_dict["collection"], country=main_dict["country"], state=main_dict["state"], landmark=main_dict["landmark"], description=main_dict["description"], GPS_lat=main_dict["GPS_lat"], GPS_long=main_dict["GPS_long"], ID_date=main_dict["ID_date"], aID=main_dict["aID"], discovery=main_dict["discovery"], species=species, specimen_ID=main_dict["specimen_ID"])
	return ant


if __name__ == '__main__':
	print "Starting population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ants.settings')
	populate()
