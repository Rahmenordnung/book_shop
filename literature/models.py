from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import redirect, reverse

# Maestro 
#     Opera
#       Part     
#         Text       
#           Essay1            
#           Essay2 

LITERATURE_CATEGORY  = (
  ('HORROR', 'Horror' ),
  ('LOVE', 'Love' ),
  ('REALITY', 'Reality' ),
  ('ADVENTURE', 'Adventure' ),
)

def get_categorie_display_value(value):
  for v in LITERATURE_CATEGORY:
    if v[0] == value:
      return v[1]
  return 'unknown category value'

class UserLibrary(models.Model):
  works_owned = models.ManyToManyField('Work', blank=True)
  user = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
      return self.user.username

  def work_list(self):
      return self.works_owned.all()

  class Meta:
      verbose_name = 'User Library'
      verbose_name_plural = 'User Library'

def post_user_signup_receiver(sender, instance, created, *args, **kwargs):
  if created:
      UserLibrary.objects.get_or_create(user=instance)
      
post_save.connect(post_user_signup_receiver, sender=settings.AUTH_USER_MODEL)

      
class Maestro(models.Model):
  complete_name = models.CharField(max_length=50)
  country_maestro = models.CharField(max_length=50)
  category= models.CharField(choices=LITERATURE_CATEGORY, max_length=8)
  slug = models.SlugField()
  
  def __str__(self):
    return f"{self.complete_name} {self.country_maestro} {get_categorie_display_value(self.category)}"
    
  
class Work(models.Model):
  maestros = models.ManyToManyField(Maestro)
  title = models.CharField(max_length=50)
  publication_date = models.DateTimeField()
  description = models.CharField(max_length=630)
  slug = models.SlugField() #work description
  cover = models.ImageField()
  price = models.FloatField()
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("literature:work_detail", kwargs={'slug': self.slug })
  
class Part(models.Model):
  work = models.ForeignKey(Work, on_delete=models.CASCADE)
  part_number = models.IntegerField()
  title = models.CharField(max_length=50)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("literature:part-detail", kwargs={'work_slug': self.work.slug, 'part_number': self.part_number }) 

class Text(models.Model):
  part = models.ForeignKey(Part, on_delete=models.CASCADE)
  text_number = models.IntegerField()
  text_page_number = models.IntegerField()
  title = models.CharField(max_length=50)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("literature:text_detail", kwargs={'work_slug': self.part.work.slug, 'part_number': self.part.part_number, 'text_number': self.text_number })

class Essay(models.Model):
  text = models.ForeignKey(Text, on_delete = models.CASCADE)
  title = models.CharField(max_length=50)
  essay_number = models.IntegerField()
  image = models.ImageField()
  
  
  def __str__(self):
    return f"{self.text.title}-{self.pk}"
  
     
            
