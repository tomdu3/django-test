from django.db import models
from datetime import date

class Student(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name="First Name"
        )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Last Name"
        )
    date_of_birth = models.DateField(
        verbose_name="Date of Birth"
        )
    gender = models.CharField(
        max_length=1,
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Other"),
        ],
        verbose_name="Gender"
        )
    student_bio = models.TextField(
        verbose_name="Student Bio",
        blank=True,
        null=True,
        )
    email = models.EmailField(
        verbose_name="Email"
        )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Joined"
        )
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = date.today()
        return (
            today.year - self.date_of_birth.year - (
                (today.month, today.day) < (
                    self.date_of_birth.month, self.date_of_birth.day
                    )
                )
            )
    
    def __str__(self):
        return f"{self.full_name} ({self.email}): {self.age} years old"
    
    
    
