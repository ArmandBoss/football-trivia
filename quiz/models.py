from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    CATEGORY_CHOICES = [
        ("world_cup", "FIFA World Cup"),
        ("champions_league", "Champions League & European Cups"),
        ("euro", "European Championship"),
        ("players", "Players & Legends"),
        ("clubs", "Football Clubs"),
        ("history", "Football History"),
    ]

    question = models.CharField(
        max_length=500
    )

    answer_a = models.CharField(
        max_length=200
    )

    answer_b = models.CharField(
        max_length=200
    )

    answer_c = models.CharField(
        max_length=200
    )

    answer_d = models.CharField(
        max_length=200
    )

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        ]
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    explanation = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.question

class Donation(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    stripe_session_id = models.CharField(
        max_length=255,
        unique=True
    )

    payment_intent_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    amount = models.PositiveIntegerField(
        help_text="Amount stored in cents"
    )

    currency = models.CharField(
        max_length=10,
        default="eur"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    customer_email = models.EmailField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        amount_euros = self.amount / 100

        return (
            f"€{amount_euros:.2f} - "
            f"{self.status} - "
            f"{self.stripe_session_id}"
        )