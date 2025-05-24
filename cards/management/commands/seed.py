from django.core.management.base import BaseCommand
from cards.models import Card

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self)
        self.stdout.write('done.')

def run_seed(self):  
       card_list = [
        {"name": "Cyber End Dragon", "rarity": "common", "image": "1546123.jpg", "description": "This is a card"},
        {"name": "Cosmic Cyclone", "rarity": "common", "image": "8267140.jpg", "description": "This is a card"},
        {"name": "Infinite Impermenance", "rarity": "common", "image": "10045474.jpg", "description": "This is a card"},
        {"name": "Raigeki", "rarity": "common", "image": "12580477.jpg", "description": "This is a card"},
        {"name": "Spright Starter", "rarity": "common", "image": "15443125.jpg", "description": "This is a card"},
       ]
       for card in card_list:
        create_card(self,card)
        
def create_card(self, args):
        card = Card(
        name = args["name"],
        rarity = args["rarity"],
        image = args["image"],
        description = args["description"]
        )
        card.save()
    
       
       
print("Seeding cards...")


