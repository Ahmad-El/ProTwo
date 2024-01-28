import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro_two.settings")

import django
django.setup()

from user_info.models import User
import faker

fakegen = faker.Faker()

def add_fake_data_user(N=5):
    for _ in range(N):
        full_name = fakegen.name().split(' ')
        name = full_name[0]
        surname = full_name[1]
        email = fakegen.email()
        user = User.objects.get_or_create(name=name, surname=surname, email=email)
        

if __name__ == "__main__":
    print("Adding data DB")
    add_fake_data_user(20)
    print("Populating Completed!")