from django.db import models

from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', message="Not an valid number")

GENDER_CHOICES =(
    ("10","Male"),
    ("20","Female"),
)

class EmployeeDetails(models.Model):
    regid = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[phone_regex])
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    hno = models.CharField(max_length=10)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    image = models.ImageField(upload_to="employee")

    class Meta:
        db_table = 'employee'
        verbose_name = ('employee')
        verbose_name_plural = ('employee')
        ordering = ('-id', )

    def __str__(self):
        return str(self.name)


class WorkingExperiences(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=128)
    from_date = models.DateField()
    to_date = models.DateField()
    address = models.TextField()

    class Meta:
        db_table = 'working_experience'
        verbose_name = ('Working Experience')
        verbose_name_plural = ('Working Experience')
        ordering = ('-id', )

    def __str__(self):
        return str(self.company_name)


class Qualifications(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    qualification_name = models.CharField(max_length=128)
    percentage = models.PositiveIntegerField()

    class Meta:
        db_table = 'qualifications'
        verbose_name = ('qualifications')
        verbose_name_plural = ('qualifications')
        ordering = ('-id', )

    def __str__(self):
        return str(self.qualification_name)


class Projects(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField(upload_to="project")

    class Meta:
        db_table = 'projects'
        verbose_name = ('projects')
        verbose_name_plural = ('projects')
        ordering = ('-id', )

    def __str__(self):
        return str(self.title)