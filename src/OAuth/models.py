from django.db                     import models
from django.core.mail              import send_mail
from django.contrib.auth           import models as auth_models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation      import ugettext_lazy as _

from OAuth.managers import UserManager

class Group(auth_models.Group):
    pass

class PermissionsMixin(auth_models.PermissionsMixin):
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )

class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(_('email address'), unique=True)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active   = models.BooleanField(_('active'), default=True)
    is_staff    = models.BooleanField(_('is staff'), default=False)
    avatar      = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)