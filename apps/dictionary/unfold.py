from django.conf import settings


# Unfold Methods
def environment_callback(request):
    """
    Callback has to return a list of two values represeting text value and the color
    type of the label displayed in top right corner.
    """

    if settings.DEBUG:
        return ["Development", "warning"]

    return ["Production", "danger"]  # info, danger, warning, success
