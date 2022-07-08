from django.core.management.base import BaseCommand
from src.profiles.models import CustomUser
from src.followers.models import Follower
from src.wall.models import Post


class Command(BaseCommand):
    # Наполнение БД фейковыми данными

    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout.write('Success')

    def create_user(self):
        for i in range(10):
            user = CustomUser.objects.create(
                username=f'test {i+2}',
                email=f'test{i}@mail.com',
                is_active=True,
                middle_name=f'test {i}',
                phone=f'8900{i}123456',
                gender=1
            )
            user.set_password('scuu7gk')
            user.save()

    def create_follower(self):
        user_list = CustomUser.objects.order_by()[2:]
        for user in user_list:
            Follower.objects.create(user=user, subscriber_id=1)

    def create_post(self):
        user_list = CustomUser.objects.all()
        for user in user_list:
            for i in range(10):
                Post.objects.create(text=f'Test post{i}', user=user)
