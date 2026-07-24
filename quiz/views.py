import random

import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views.decorators.http import require_POST

from .models import Question, Donation

from django.views.decorators.csrf import csrf_exempt


# ==========================================================
# STRIPE CONFIGURATION
# ==========================================================

stripe.api_key = settings.STRIPE_SECRET_KEY


# ==========================================================
# QUIZ SETTINGS
# ==========================================================

QUIZ_LENGTH = 10


# ==========================================================
# HOME
# ==========================================================

def home(request):

    return render(
        request,
        "quiz/home.html"
    )


# ==========================================================
# DONATION PAGE
# ==========================================================

def donate(request):

    context = {

        "STRIPE_PUBLISHABLE_KEY":
            settings.STRIPE_PUBLISHABLE_KEY

    }

    return render(
        request,
        "quiz/donate.html",
        context
    )


# ==========================================================
# CHOOSE GAME
# ==========================================================

def choose_game(request):

    return render(
        request,
        "quiz/choose_game.html"
    )


# ==========================================================
# HELPER - CREATE QUIZ SESSION
# ==========================================================

def create_quiz_session(
    request,
    queryset,
    game_mode,
    game_label
):

    question_ids = list(

        queryset.values_list(
            "id",
            flat=True
        )

    )

    # ------------------------------------------------------
    # CHECK IF QUESTIONS EXIST
    # ------------------------------------------------------

    if not question_ids:

        return render(

            request,

            "quiz/choose_game.html",

            {

                "error":
                    "No questions are available "
                    "for this game mode."

            }

        )

    # ------------------------------------------------------
    # DETERMINE NUMBER OF QUESTIONS
    # ------------------------------------------------------

    number_of_questions = min(

        QUIZ_LENGTH,

        len(question_ids)

    )

    # ------------------------------------------------------
    # RANDOMLY SELECT QUESTIONS
    # ------------------------------------------------------

    selected_ids = random.sample(

        question_ids,

        number_of_questions

    )

    # ------------------------------------------------------
    # CREATE SESSION
    # ------------------------------------------------------

    request.session[
        "quiz_questions"
    ] = selected_ids

    request.session[
        "current_question"
    ] = 0

    request.session[
        "score"
    ] = 0

    request.session[
        "answers"
    ] = []

    request.session[
        "game_mode"
    ] = game_mode

    request.session[
        "game_label"
    ] = game_label

    return redirect(
        "quiz:question"
    )


# ==========================================================
# QUICK MATCH
# ==========================================================

def start_quiz(request):

    questions = Question.objects.all()

    return create_quiz_session(

        request,

        questions,

        "quick",

        "Quick Match"

    )


# ==========================================================
# CATEGORY QUIZ
# ==========================================================

def choose_category(request):

    categories = []

    for value, label in Question.CATEGORY_CHOICES:

        count = Question.objects.filter(

            category=value

        ).count()

        categories.append(

            {

                "value":
                    value,

                "label":
                    label,

                "count":
                    count,

            }

        )

    return render(

        request,

        "quiz/choose_category.html",

        {

            "categories":
                categories

        }

    )


def start_category_quiz(
    request,
    category
):

    valid_categories = dict(

        Question.CATEGORY_CHOICES

    )

    # ------------------------------------------------------
    # INVALID CATEGORY
    # ------------------------------------------------------

    if category not in valid_categories:

        return redirect(
            "quiz:choose_category"
        )

    # ------------------------------------------------------
    # FILTER QUESTIONS
    # ------------------------------------------------------

    questions = Question.objects.filter(

        category=category

    )

    label = valid_categories[
        category
    ]

    return create_quiz_session(

        request,

        questions,

        "category",

        label

    )


# ==========================================================
# DIFFICULTY CHALLENGE
# ==========================================================

def choose_difficulty(request):

    difficulties = []

    for value, label in Question.DIFFICULTY_CHOICES:

        count = Question.objects.filter(

            difficulty=value

        ).count()

        difficulties.append(

            {

                "value":
                    value,

                "label":
                    label,

                "count":
                    count,

            }

        )

    return render(

        request,

        "quiz/choose_difficulty.html",

        {

            "difficulties":
                difficulties

        }

    )


def start_difficulty_quiz(
    request,
    difficulty
):

    valid_difficulties = dict(

        Question.DIFFICULTY_CHOICES

    )

    # ------------------------------------------------------
    # INVALID DIFFICULTY
    # ------------------------------------------------------

    if difficulty not in valid_difficulties:

        return redirect(
            "quiz:choose_difficulty"
        )

    # ------------------------------------------------------
    # FILTER QUESTIONS
    # ------------------------------------------------------

    questions = Question.objects.filter(

        difficulty=difficulty

    )

    label = (

        valid_difficulties[
            difficulty
        ]

        + " Challenge"

    )

    return create_quiz_session(

        request,

        questions,

        "difficulty",

        label

    )


# ==========================================================
# QUESTION
# ==========================================================

def question(request):

    question_ids = request.session.get(

        "quiz_questions"

    )

    current_index = request.session.get(

        "current_question",

        0

    )

    # ------------------------------------------------------
    # NO ACTIVE QUIZ
    # ------------------------------------------------------

    if not question_ids:

        return redirect(
            "quiz:home"
        )

    # ------------------------------------------------------
    # QUIZ FINISHED
    # ------------------------------------------------------

    if current_index >= len(
        question_ids
    ):

        return redirect(
            "quiz:results"
        )

    # ------------------------------------------------------
    # GET CURRENT QUESTION
    # ------------------------------------------------------

    question_id = question_ids[
        current_index
    ]

    current_question = get_object_or_404(

        Question,

        id=question_id

    )

    # ------------------------------------------------------
    # TEMPLATE CONTEXT
    # ------------------------------------------------------

    context = {

        "question":
            current_question,

        "question_number":
            current_index + 1,

        "total_questions":
            len(question_ids),

        "score":
            request.session.get(
                "score",
                0
            ),

        "game_label":
            request.session.get(
                "game_label",
                "Quick Match"
            ),

    }

    return render(

        request,

        "quiz/question.html",

        context

    )


# ==========================================================
# SUBMIT ANSWER
# ==========================================================

@require_POST
def submit_answer(request):

    question_ids = request.session.get(

        "quiz_questions"

    )

    current_index = request.session.get(

        "current_question",

        0

    )

    # ------------------------------------------------------
    # NO ACTIVE QUIZ
    # ------------------------------------------------------

    if not question_ids:

        return redirect(
            "quiz:home"
        )

    # ------------------------------------------------------
    # QUIZ ALREADY FINISHED
    # ------------------------------------------------------

    if current_index >= len(
        question_ids
    ):

        return redirect(
            "quiz:results"
        )

    # ------------------------------------------------------
    # GET CURRENT QUESTION
    # ------------------------------------------------------

    question_id = question_ids[
        current_index
    ]

    current_question = get_object_or_404(

        Question,

        id=question_id

    )

    # ------------------------------------------------------
    # GET SELECTED ANSWER
    # ------------------------------------------------------

    selected_answer = request.POST.get(

        "answer"

    )

    valid_answers = {

        "A",
        "B",
        "C",
        "D",

    }

    # ------------------------------------------------------
    # INVALID ANSWER
    # ------------------------------------------------------

    if selected_answer not in valid_answers:

        return redirect(
            "quiz:question"
        )

    # ------------------------------------------------------
    # CHECK ANSWER
    # ------------------------------------------------------

    is_correct = (

        selected_answer

        ==

        current_question.correct_answer

    )

    # ------------------------------------------------------
    # UPDATE SCORE
    # ------------------------------------------------------

    score = request.session.get(

        "score",

        0

    )

    if is_correct:

        score += 1

    request.session[
        "score"
    ] = score

    # ------------------------------------------------------
    # STORE ANSWER HISTORY
    # ------------------------------------------------------

    answers = request.session.get(

        "answers",

        []

    )

    answers.append(

        {

            "question_id":
                current_question.id,

            "selected_answer":
                selected_answer,

            "correct_answer":
                current_question.correct_answer,

            "is_correct":
                is_correct,

        }

    )

    request.session[
        "answers"
    ] = answers

    # ------------------------------------------------------
    # MOVE TO NEXT QUESTION
    # ------------------------------------------------------

    request.session[
        "current_question"
    ] = current_index + 1

    # ------------------------------------------------------
    # ANSWER TEXTS
    # ------------------------------------------------------

    answer_texts = {

        "A":
            current_question.answer_a,

        "B":
            current_question.answer_b,

        "C":
            current_question.answer_c,

        "D":
            current_question.answer_d,

    }

    # ------------------------------------------------------
    # FEEDBACK CONTEXT
    # ------------------------------------------------------

    context = {

        "question":
            current_question,

        "selected_answer":
            selected_answer,

        "selected_answer_text":
            answer_texts[
                selected_answer
            ],

        "correct_answer":
            current_question.correct_answer,

        "correct_answer_text":
            answer_texts[
                current_question.correct_answer
            ],

        "is_correct":
            is_correct,

        "score":
            score,

        "finished":
            current_index + 1
            >= len(question_ids),

    }

    return render(

        request,

        "quiz/feedback.html",

        context

    )


# ==========================================================
# RESULTS
# ==========================================================

def results(request):

    question_ids = request.session.get(

        "quiz_questions"

    )

    # ------------------------------------------------------
    # NO QUIZ SESSION
    # ------------------------------------------------------

    if not question_ids:

        return redirect(
            "quiz:home"
        )

    # ------------------------------------------------------
    # SCORE
    # ------------------------------------------------------

    score = request.session.get(

        "score",

        0

    )

    total = len(
        question_ids
    )

    percentage = (

        round(
            (score / total) * 100
        )

        if total

        else 0

    )

    # ------------------------------------------------------
    # RESULT MESSAGE
    # ------------------------------------------------------

    if percentage == 100:

        message = (
            "Perfect score!"
        )

    elif percentage >= 80:

        message = (
            "Excellent performance!"
        )

    elif percentage >= 60:

        message = (
            "Good job!"
        )

    elif percentage >= 40:

        message = (
            "Not bad. Keep practicing!"
        )

    else:

        message = (
            "Time for another match!"
        )

    # ------------------------------------------------------
    # TEMPLATE CONTEXT
    # ------------------------------------------------------

    context = {

        "score":
            score,

        "total":
            total,

        "percentage":
            percentage,

        "message":
            message,

        "game_label":
            request.session.get(
                "game_label",
                "Quick Match"
            ),

    }

    return render(

        request,

        "quiz/results.html",

        context

    )


# ==========================================================
# STRIPE - CREATE CHECKOUT SESSION
# ==========================================================

@require_POST
def create_checkout_session(request):

    # ------------------------------------------------------
    # GET AND VALIDATE DONATION AMOUNT
    # ------------------------------------------------------

    try:

        amount = int(
            request.POST.get(
                "amount",
                5
            )
        )

    except (
        TypeError,
        ValueError
    ):

        return JsonResponse(

            {

                "error":
                    "Invalid donation amount."

            },

            status=400

        )

    # Minimum donation: €1

    if amount < 1:

        return JsonResponse(

            {

                "error":
                    "Minimum donation is €1."

            },

            status=400

        )

    # Maximum donation: €1000

    if amount > 1000:

        return JsonResponse(

            {

                "error":
                    "Maximum donation is €1000."

            },

            status=400

        )

    # ------------------------------------------------------
    # CONVERT EURO TO CENTS
    #
    # Stripe expects:
    #
    # €1  -> 100
    # €5  -> 500
    # €10 -> 1000
    # ------------------------------------------------------

    amount_in_cents = (
        amount * 100
    )

    # ------------------------------------------------------
    # CREATE STRIPE CHECKOUT SESSION
    # ------------------------------------------------------

    try:

        checkout_session = (
            stripe.checkout.Session.create(

                mode="payment",

                payment_method_types=[
                    "card"
                ],

                line_items=[

                    {

                        "price_data": {

                            "currency":
                                "eur",

                            "product_data": {

                                "name":
                                    "Support Football Trivia",

                                "description":
                                    "Support the development "
                                    "of Football Trivia.",

                            },

                            "unit_amount":
                                amount_in_cents,

                        },

                        "quantity":
                            1,

                    }

                ],

                success_url=(
                    request.build_absolute_uri(
                        "/donate/success/"
                    )
                    + "?session_id={CHECKOUT_SESSION_ID}"
                ),

                cancel_url=(
                    request.build_absolute_uri(
                        "/donate/cancel/"
                    )
                ),

            )
        )

    # ------------------------------------------------------
    # STRIPE ERROR
    # ------------------------------------------------------

    except stripe.StripeError:

        return JsonResponse(

            {

                "error":
                    "Stripe could not create "
                    "the checkout session."

            },

            status=400

        )

    except Exception:

        return JsonResponse(

            {

                "error":
                    "An unexpected error occurred."

            },

            status=500

        )

    # ------------------------------------------------------
    # RETURN CHECKOUT SESSION
    # ------------------------------------------------------

    return JsonResponse(

        {

            "id":
                checkout_session.id,

            "url":
                checkout_session.url,

        }

    )


# ==========================================================
# DONATION SUCCESS
# ==========================================================

def donate_success(request):

    return render(

        request,

        "quiz/donate_success.html"

    )


# ==========================================================
# DONATION CANCEL
# ==========================================================

def donate_cancel(request):

    return render(

        request,

        "quiz/donate_cancel.html"

    )

# ==========================================================
# STRIPE WEBHOOK
# ==========================================================

@csrf_exempt
@require_POST
def stripe_webhook(request):

    payload = request.body

    signature = request.META.get(
        "HTTP_STRIPE_SIGNATURE"
    )

    webhook_secret = (
        settings.STRIPE_WEBHOOK_SECRET
    )

    # ======================================================
    # VERIFY WEBHOOK SIGNATURE
    # ======================================================

    try:

        event = stripe.Webhook.construct_event(

            payload=payload,

            sig_header=signature,

            secret=webhook_secret

        )

    except ValueError:

        return JsonResponse(

            {
                "error":
                    "Invalid webhook payload."
            },

            status=400

        )

    except stripe.SignatureVerificationError:

        return JsonResponse(

            {
                "error":
                    "Invalid webhook signature."
            },

            status=400

        )


    # ======================================================
    # CHECKOUT SESSION COMPLETED
    # ======================================================

    if event.type == "checkout.session.completed":

        session = event.data.object


        # --------------------------------------------------
        # STRIPE SESSION DATA
        # --------------------------------------------------

        session_id = (
            session.id
        )

        payment_status = (
            session.payment_status
        )

        amount_total = (
            session.amount_total
            or 0
        )

        currency = (
            session.currency
            or "eur"
        )

        payment_intent_id = (
            session.payment_intent
        )


        # --------------------------------------------------
        # CUSTOMER EMAIL
        # --------------------------------------------------

        customer_email = None

        if session.customer_details:

            customer_email = (
                session.customer_details.email
            )


        # --------------------------------------------------
        # SAVE ONLY SUCCESSFUL PAYMENTS
        # --------------------------------------------------

        if payment_status == "paid":

            Donation.objects.update_or_create(

                stripe_session_id=session_id,

                defaults={

                    "payment_intent_id":
                        payment_intent_id,

                    "amount":
                        amount_total,

                    "currency":
                        currency,

                    "status":
                        "paid",

                    "customer_email":
                        customer_email,

                }

            )


    # ======================================================
    # STRIPE EXPECTS HTTP 200
    # ======================================================

    return JsonResponse(

        {
            "status":
                "success"
        }

    )

    # ------------------------------------------------------
    # RETURN SUCCESS TO STRIPE
    # ------------------------------------------------------

    return JsonResponse(
        {
            "status": "success"
        }
    )