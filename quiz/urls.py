from django.urls import path

from . import views


app_name = "quiz"


urlpatterns = [

    # ======================================================
    # MAIN PAGES
    # ======================================================

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "donate/",
        views.donate,
        name="donate"
    ),


    # ======================================================
    # GAME SELECTION
    # ======================================================

    path(
        "choose-game/",
        views.choose_game,
        name="choose_game"
    ),


    # ======================================================
    # QUICK MATCH
    # ======================================================

    path(
        "start/",
        views.start_quiz,
        name="start"
    ),


    # ======================================================
    # CATEGORY QUIZ
    # ======================================================

    path(
        "categories/",
        views.choose_category,
        name="choose_category"
    ),

    path(
        "category/<str:category>/",
        views.start_category_quiz,
        name="start_category"
    ),


    # ======================================================
    # DIFFICULTY CHALLENGE
    # ======================================================

    path(
        "difficulty/",
        views.choose_difficulty,
        name="choose_difficulty"
    ),

    path(
        "difficulty/<str:difficulty>/",
        views.start_difficulty_quiz,
        name="start_difficulty"
    ),


    # ======================================================
    # QUIZ
    # ======================================================

    path(
        "question/",
        views.question,
        name="question"
    ),

    path(
        "answer/",
        views.submit_answer,
        name="answer"
    ),

    path(
        "results/",
        views.results,
        name="results"
    ),


    # ======================================================
    # STRIPE CHECKOUT
    # ======================================================

    path(
        "create-checkout-session/",
        views.create_checkout_session,
        name="create_checkout_session"
    ),

    path(
        "stripe/webhook/",
        views.stripe_webhook,
        name="stripe_webhook"
    ),


    # ======================================================
    # DONATION RESULT PAGES
    # ======================================================

    path(
        "donate/success/",
        views.donate_success,
        name="donate_success"
    ),

    path(
        "donate/cancel/",
        views.donate_cancel,
        name="donate_cancel"
    ),


]