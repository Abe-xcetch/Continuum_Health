import factory

from apps.accounts.models import User

TEST_PASSWORD = "synthetic-Passw0rd!"


class UserFactory(factory.django.DjangoModelFactory[User]):
    """Synthetic staff users only. Never use real names or emails in tests."""

    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Sequence(lambda n: f"user{n}@example.test")
    password = factory.PostGenerationMethodCall("set_password", TEST_PASSWORD)

    @factory.post_generation
    def _save_password(self, create, extracted, **kwargs):
        if create:
            self.save(update_fields=["password"])
