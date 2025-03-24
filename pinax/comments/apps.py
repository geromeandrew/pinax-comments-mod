from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.comments"
    label = "pinax_comments"
    verbose_name = _("Pinax Comments")
