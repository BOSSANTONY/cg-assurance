from django.contrib import admin

from .models import (
    Profile,
    InsuranceProduct,
    QuoteRequest,
    Policy,
    Claim,
    Document,
    Payment,
    ContactMessage
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "phone",
        "city",
        "country",
    )

    search_fields = (
        "user__username",
        "user__email",
        "phone",
    )


@admin.register(InsuranceProduct)
class InsuranceProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "type",
        "price",
        "active",
    )

    list_filter = (
        "type",
        "active",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "product",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "user__username",
        "user__email",
    )


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):

    list_display = (
        "policy_number",
        "user",
        "product",
        "start_date",
        "end_date",
        "status",
        "premium",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "policy_number",
        "user__username",
        "user__email",
    )


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "policy",
        "title",
        "status",
        "amount_requested",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "title",
        "user__username",
        "policy__policy_number",
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "policy",
        "uploaded_at",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "reference",
        "user",
        "policy",
        "amount",
        "status",
        "payment_date",
    )

    list_filter = (
        "status",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "answered",
        "created_at",
    )

    list_filter = (
        "answered",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )