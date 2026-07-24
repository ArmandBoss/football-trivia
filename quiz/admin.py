from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question
from .models import Donation


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "question",
        "category",
        "difficulty",
        "correct_answer",
    )

    list_filter = (
        "category",
        "difficulty",
    )

    search_fields = (
        "question",
    )

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "amount_display",
        "currency",
        "status",
        "customer_email",
        "created_at",
    )

    list_filter = (
        "status",
        "currency",
        "created_at",
    )

    search_fields = (
        "stripe_session_id",
        "payment_intent_id",
        "customer_email",
    )

    readonly_fields = (
        "stripe_session_id",
        "payment_intent_id",
        "amount",
        "currency",
        "customer_email",
        "created_at",
        "updated_at",
    )

    def amount_display(self, obj):

        return f"€{obj.amount / 100:.2f}"

    amount_display.short_description = "Amount"