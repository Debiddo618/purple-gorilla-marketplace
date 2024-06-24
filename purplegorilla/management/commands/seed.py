from django.core.management.base import BaseCommand
from purplegorilla.models import Product
import logging
import requests
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

MODE_REFRESH = 'refresh'
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(options['mode'])
        self.stdout.write('done.')

def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Product instances")
    Product.objects.all().delete()

def create_product():
    api_url = 'https://fakestoreapi.com/products'
    dummy_user, created = User.objects.get_or_create(
        username='dummy_user', 
        defaults={'email': 'dummy@example.com', 'password': 'password123'}
    )

    if created:
        logger.info("Created dummy user")

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        for product in data:
            if product['category'] in ["men's clothing", "women's clothing", "jewelery"]:
                category = 'F'
            elif product['category'] == 'electronics':
                category = 'E'
            else:
                category = 'G'

            Product.objects.create(
                name=product['title'],
                price=product['price'],
                image=product['image'],
                description=product['description'],
                category=category,
                user=dummy_user
            )
            logger.info(f"Created product: {product['title']}")

    except requests.exceptions.RequestException as err:
        logger.error(f"An error occurred: {err}")

def run_seed(mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    clear_data()
    if mode == MODE_CLEAR:
        return
    create_product()
