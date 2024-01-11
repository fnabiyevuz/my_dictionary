from celery import shared_task

from celery import shared_task

from apps.dictionary.models import Unit, Word


@shared_task
def send_to_channel():
    random_word = Word.objects.filter(
        is_delete=False,
        unit__in=Unit.objects.filter(is_delete=False)
    ).order_by('?').first()

    if random_word:
        pass
