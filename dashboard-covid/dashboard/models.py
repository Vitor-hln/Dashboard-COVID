from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    population = models.BigIntegerField()

    def __str__(self):
        return self.name

class CovidData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    total_cases = models.IntegerField()
    new_cases = models.IntegerField()
    total_deaths = models.IntegerField()
    new_deaths = models.IntegerField()
    people_vaccinated = models.IntegerField(null=True, blank=True)
    people_fully_vaccinated = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.country.name} - {self.date}"

class VaccineApproval(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    approval_date = models.DateField()

    def __str__(self):
        return f"{self.country.name} - {self.vaccine_name}"