from django_faker import Faker
from api.models import Dog

populator = Faker.getPopulator()
populator.addEntity(Dog, 30)

insertedPks = populator.execute()