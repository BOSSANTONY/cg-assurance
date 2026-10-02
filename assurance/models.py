from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        default="Congo"
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class InsuranceProduct(models.Model):

    TYPE_CHOICES = [
        ("auto", "Assurance automobile"),
        ("health", "Assurance santé"),
        ("home", "Assurance habitation"),
        ("travel", "Assurance voyage"),
        ("life", "Assurance vie"),
        ("business", "Assurance entreprise"),
    ]

    name = models.CharField(max_length=150)

    slug = models.SlugField(
        unique=True
    )

    type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    coverage = models.TextField(
        help_text="Une garantie par ligne."
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class QuoteRequest(models.Model):

    STATUS_CHOICES = [
        ("pending", "En attente"),
        ("reviewing", "En étude"),
        ("accepted", "Accepté"),
        ("rejected", "Refusé"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quotes"
    )

    product = models.ForeignKey(
        InsuranceProduct,
        on_delete=models.CASCADE,
        related_name="quotes"
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Devis #{self.id} - {self.user.username}"


class Policy(models.Model):

    STATUS_CHOICES = [
        ("active", "Active"),
        ("pending", "En attente"),
        ("expired", "Expirée"),
        ("cancelled", "Annulée"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="policies"
    )

    product = models.ForeignKey(
        InsuranceProduct,
        on_delete=models.CASCADE
    )

    policy_number = models.CharField(
        max_length=50,
        unique=True
    )

    start_date = models.DateField()

    end_date = models.DateField()

    premium = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.policy_number


class Claim(models.Model):

    STATUS_CHOICES = [
        ("submitted", "Déclaré"),
        ("reviewing", "En étude"),
        ("approved", "Accepté"),
        ("rejected", "Refusé"),
        ("paid", "Indemnisé"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="claims"
    )

    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        related_name="claims"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    incident_date = models.DateField()

    location = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="submitted"
    )

    amount_requested = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Sinistre #{self.id}"


class Document(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=200
    )

    file = models.FileField(
        upload_to="documents/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Payment(models.Model):

    STATUS_CHOICES = [
        ("pending", "En attente"),
        ("paid", "Payé"),
        ("failed", "Échoué"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    reference = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.reference


class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    answered = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.subject