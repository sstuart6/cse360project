from django.db import models
from django.utils.encoding import smart_unicode
from django.core.files.storage import FileSystemStorage
from django.core.validators import validate_email
from django.conf import settings

photos_location = FileSystemStorage(location=settings.FILE_SYSTEM)
profile_pic_location = FileSystemStorage(location=settings.PROFILE_PICTURE_FILE_SYSTEM)

class User(models.Model):
    full_name = models.CharField(max_length = 120, null = False, blank = False)
    password = models.CharField(max_length = 120, null = False, blank = False)
    email = models.EmailField(validators=[validate_email], null = False, blank = False, unique = True)
    def __unicode__(self) :
        return smart_unicode(self.email)

class Picture(models.Model):
    user_id = models.ForeignKey(User, null=False, related_name='pictures')
    photo = models.ImageField(storage= photos_location)
    def __unicode__(self):
        return "{0} {1}".format(self.user_id, self.photo)
    
    
def get_profile_pic_name(instance, filename):
        return "{0}".format(instance.user.id)

class Settings(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, related_name='settings')
    profile_pic = models.ImageField(storage=profile_pic_location, upload_to=get_profile_pic_name, null=False)
    def __unicode__(self):
        return "{0} {1}".format(self.user, self.profile_pic)