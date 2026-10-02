from django.urls import path
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),
        path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": {"static": StaticViewSitemap}},
    name="django.contrib.sitemaps.views.sitemap",
),
    path(
    "robots.txt",
    views.robots_txt,
    name="robots_txt"
),

    path(
        "services/",
        views.services,
        name="services"
    ),

    path(
        "tarifs/",
        views.pricing,
        name="pricing"
    ),

    path(
        "faq/",
        views.faq,
        name="faq"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),

    path(
        "inscription/",
        views.register,
        name="register"
    ),

    path(
        "connexion/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login"
    ),

    path(
        "deconnexion/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),

    path(
        "espace-client/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "espace-client/contrats/",
        views.policies,
        name="policies"
    ),

    path(
        "espace-client/devis/",
        views.quotes,
        name="quotes"
    ),

    path(
        "espace-client/devis/nouveau/",
        views.quote_create,
        name="quote_create"
    ),

    path(
        "espace-client/sinistres/",
        views.claims,
        name="claims"
    ),

    path(
        "espace-client/sinistres/nouveau/",
        views.claim_create,
        name="claim_create"
    ),

    path(
        "espace-client/documents/",
        views.documents,
        name="documents"
    ),

    path(
        "espace-client/profil/",
        views.profile,
        name="profile"
    ),
]
