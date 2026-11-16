import factory

from apps.core.tests.testapp.models import Note


class NoteFactory(factory.django.DjangoModelFactory[Note]):
    class Meta:
        model = Note

    title = factory.Sequence(lambda n: f"Synthetic note {n}")
