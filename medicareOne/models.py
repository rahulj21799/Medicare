from django.db import models

# Create your models here.
class contactUs(models.Model):
    name=models.CharField('Full Name',default='',max_length=50)
    email=models.EmailField('Email',default='',max_length=100)
    mobile=models.IntegerField('Mobile Number',default=0)
    course=models.CharField('Selected Course',default='',max_length=20)
    def __str__(self):
        return self.name
class Highlights(models.Model):
    course=models.CharField(default='',max_length=20) 
    hig= models.CharField('highlights',default='',max_length=5000)
    eli=models.CharField('eligibility',default='',max_length=5000)
    adm=models.CharField('Admission',default='',max_length=5000)
    def __str__(self):
        return self.course
class Faculty(models.Model):
    image=models.ImageField(default='',upload_to="Faculty/images")
    name=models.CharField('Full Name',default='',max_length=50)
    post=models.CharField('Post',default='',max_length=20)
    degree=models.CharField('Degree',default='',max_length=50)
    def __str__(self):
        return self.name
class Elite(models.Model):
    image=models.ImageField(default='',upload_to="Elite/images")
    name=models.CharField('Full Name',default='',max_length=50)
    degree=models.CharField('Degree',default='',max_length=50)
    year=models.CharField('Year',default='',max_length=20)
    percentage=models.CharField('Percentage',default='',max_length=20)
    def __str__(self):
        return self.name
class Infrasturcture(models.Model):
        cat=models.ForeignKey('Category',on_delete=models.CASCADE,default='')
        image=models.ImageField('Image',upload_to='Infrastructure/images',default='')
        title=models.CharField('Title',max_length=100,default='')
        description=models.CharField('Description',max_length=50000,default='',blank=True)
        def __str__(self):
            return self.title
class Category(models.Model):
    cat=models.CharField('Category',max_length=50,default='')
    image=models.ImageField('Image',upload_to="Category/Images",default='')
    def __str__(self):
        return self.cat
class Downloads(models.Model):
    dwn=models.FileField('File',upload_to='Downloads',default='')
    
            


