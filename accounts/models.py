from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
import re


class User(AbstractBaseUser, PermissionsMixin):
    """
    Create the base of django standart user profile and allows us to
    add permission to our user model.
    """

    # Username with regex validators
    username = models.CharField(
        _('User'),
        max_length=30,
        unique=True,
        help_text='Short name that will be used uniquely on the platform.',
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a valid username'),
                _('This value should only contain letters, numbers, \
                  and characters @/./+/-/_.'),
                'invalid'
            )
        ]
    )

    email = models.EmailField(
        _('E-mail'),
        help_text=_("Email that will be used as username."),
        unique=True
    )

    name = models.CharField(
        _('Name'),
        help_text=_("Full user name."),
        max_length=150,
        blank=True
    )

    institution = models.CharField(
        _('Institution'),
        help_text=_("University or School in which the user is inserted."),
        max_length=100,
        blank=True
    )

    course = models.CharField(
        _('Course'),
        help_text=_("Course of university or Period of school."),
        max_length=100,
        blank=True
    )

    photo = models.ImageField(
        upload_to='accounts',
        help_text=_("Photo of user."),
        verbose_name=_('Photo'),
        blank=True,
        null=True
    )

    is_teacher = models.BooleanField(
        _('Is Teacher?'),
        help_text=_("Verify if the user is teacher or student"),
        default=False
    )

    last_login = models.DateTimeField(
        _('Last Login'),
        help_text=_("Last moment the user logged in."),
        blank=True,
        null=True
    )

    # Use to determine if this user is currently active in the system
    # You can use it to disable user accounts
    is_active = models.BooleanField(
        _('Is Active?'),
        help_text=_("Verify if the user is active."),
        default=True
    )

    # Transform the user to staff members that can manage de users
    is_staff = models.BooleanField(
        _('Is Staff?'),
        help_text=_("Verify if the user is a staff."),
        default=False
    )

    # Create a date when the user is created
    created_at = models.DateTimeField(
        _('Created at'),
        help_text=_("Date that the user is created."),
        auto_now_add=True
    )

    # Create or update the date after the user is updated
    updated_at = models.DateTimeField(
        _('Updated at'),
        help_text=_("Date that the user is updated."),
        auto_now=True
    )

    # Help manager the user profile
    objects = UserManager()

    # Is the field that going to be used as the username for this user
    USERNAME_FIELD = 'username'

    # Is a list of fields that are required for all users, the username don't
    # need to be passed.
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        """
        Returns the object as a string, the attribute that will represent
        the object.
        """

        return self.email

    def get_full_name(self):
        """
        Used to get the user full name.
        """

        return self.name or self.username

    def get_short_name(self):
        """
        Used to get the user short name.
        """
        LAST_NAME = -1
        FIRST_NAME = 0

        if len(self.name.split(" ")) >= 2:
            return str(
                self.name.split(" ")[FIRST_NAME] +
                " " +
                self.name.split(" ")[LAST_NAME]
            )
        else:
            return str(self.name)

    class Meta:
        """
        Some information about user class.
        """

        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ('email',)


class Teacher(User):
    """
    Create the specific user Teacher that will manage the TBL sessions and
    class
    """

    class Meta:
        """
        Some information about teacher class
        """

        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


class Student(User):
    """
    Create the specific user Student that will use the TBL sessions and
    class
    """

    class Meta:
        """
        Some information about teacher class
        """

        verbose_name = _("Student")
        verbose_name_plural = _("Students")