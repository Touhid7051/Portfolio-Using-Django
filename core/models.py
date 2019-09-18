from django.db import models




# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"



# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    #description = models.TextField(verbose_name="About service")
    area = models.TextField(verbose_name="Working Area")
    Charge = models.CharField(max_length=10,verbose_name="Charges")

    def __str__(self):
        return self.name

    def area_as_list(self):
        return self.area.split(',')



# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name

#contact info
class Contact(models.Model):
    description = models.TextField(verbose_name="Contact/Address info")

    def __str__(self):
        return self.description

#All Tittles

class aboutTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter About Title")

    def __str__(self):
        return self.name

class serviceTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Service Title")

    def __str__(self):
        return self.name

class portfolioTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Portfolio Title")

    def __str__(self):
        return self.name

class testimonialTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Testimonial Title")

    def __str__(self):
        return self.name

class adressTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Enter Address bar Title")

    def __str__(self):
        return self.name



class contactTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Contact Title")

    def __str__(self):
        return self.name


