from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)

from .forms import (
    RegisterForm,
    QuoteForm,
    ClaimForm,
    ContactForm,
    ProfileForm
)

from .models import (
    InsuranceProduct,
    Policy,
    Claim,
    QuoteRequest,
    Document
)


def home(request):

    products = InsuranceProduct.objects.filter(
        active=True
    )[:6]

    return render(
        request,
        "home.html",
        {
            "products": products
        }
    )


def services(request):

    products = InsuranceProduct.objects.filter(
        active=True
    )

    return render(
        request,
        "services.html",
        {
            "products": products
        }
    )


def pricing(request):

    products = InsuranceProduct.objects.filter(
        active=True
    )

    return render(
        request,
        "pricing.html",
        {
            "products": products
        }
    )


def faq(request):

    return render(
        request,
        "faq.html"
    )


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Votre message a bien été envoyé."
            )

            return redirect("contact")

    else:

        form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "form": form
        }
    )


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.first_name = form.cleaned_data["first_name"]

            user.last_name = form.cleaned_data["last_name"]

            user.email = form.cleaned_data["email"]

            user.save()

            from .models import Profile

            Profile.objects.create(
                user=user
            )

            login(
                request,
                user
            )

            messages.success(
                request,
                "Votre compte CG-Assurance a été créé."
            )

            return redirect(
                "dashboard"
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


@login_required
def dashboard(request):

    policies = Policy.objects.filter(
        user=request.user
    )

    claims = Claim.objects.filter(
        user=request.user
    )

    quotes = QuoteRequest.objects.filter(
        user=request.user
    )

    documents = Document.objects.filter(
        user=request.user
    )

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "policies": policies,
            "claims": claims,
            "quotes": quotes,
            "documents": documents,
        }
    )


@login_required
def policies(request):

    data = Policy.objects.filter(
        user=request.user
    )

    return render(
        request,
        "dashboard/policies.html",
        {
            "policies": data
        }
    )


@login_required
def quotes(request):

    data = QuoteRequest.objects.filter(
        user=request.user
    )

    return render(
        request,
        "dashboard/quotes.html",
        {
            "quotes": data
        }
    )


@login_required
def quote_create(request):

    if request.method == "POST":

        form = QuoteForm(
            request.POST
        )

        if form.is_valid():

            quote = form.save(
                commit=False
            )

            quote.user = request.user

            quote.save()

            messages.success(
                request,
                "Votre demande de devis a été envoyée."
            )

            return redirect(
                "quotes"
            )

    else:

        form = QuoteForm()

    return render(
        request,
        "dashboard/quote_form.html",
        {
            "form": form
        }
    )


@login_required
def claims(request):

    data = Claim.objects.filter(
        user=request.user
    )

    return render(
        request,
        "dashboard/claims.html",
        {
            "claims": data
        }
    )


@login_required
def claim_create(request):

    if request.method == "POST":

        form = ClaimForm(
            request.POST
        )

        if form.is_valid():

            claim = form.save(
                commit=False
            )

            claim.user = request.user

            claim.save()

            messages.success(
                request,
                "Votre sinistre a été déclaré."
            )

            return redirect(
                "claims"
            )

    else:

        form = ClaimForm(
            initial={
                "policy": request.GET.get(
                    "policy"
                )
            }
        )

        form.fields["policy"].queryset = Policy.objects.filter(
            user=request.user
        )

    return render(
        request,
        "dashboard/claim_form.html",
        {
            "form": form
        }
    )

@login_required
def documents(request):

    data = Document.objects.filter(
        user=request.user
    )

    return render(
        request,
        "dashboard/documents.html",
        {
            "documents": data
        }
    )


@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            form.save()

            request.user.first_name = request.POST.get(
                "first_name"
            )

            request.user.last_name = request.POST.get(
                "last_name"
            )

            request.user.email = request.POST.get(
                "email"
            )

            request.user.save()

            messages.success(
                request,
                "Votre profil a été mis à jour."
            )

            return redirect(
                "profile"
            )

    else:

        form = ProfileForm(
            instance=profile,
            initial={
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
            }
        )

    return render(
        request,
        "dashboard/profile.html",
        {
            "form": form
        }
    )



from django.http import HttpResponse
def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://cg-assurance.vercel.app/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")
