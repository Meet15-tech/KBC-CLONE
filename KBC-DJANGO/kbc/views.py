import random

from django.shortcuts import render, redirect
from .models import Player, Question, FFFResult, GameHistory
from .forms import PlayerForm


money = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹1 Crore",
    "₹7 Crore"
]


def home(request):
    return render(request, "kbc/home.html")


def register(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("register")
    else:
        form = PlayerForm()

    players = Player.objects.all()

    return render(
        request,
        "kbc/register.html",
        {
            "form": form,
            "players": players
        }
    )


def fastest_finger(request):
    players = Player.objects.all()

    if not players:
        return redirect("register")

    question = Question.objects.order_by("?").first()

    if request.method == "POST":
        FFFResult.objects.all().delete()

        question_id = request.POST.get("question_id")
        question = Question.objects.get(id=question_id)

        for player in players:
            answer = request.POST.get("answer_" + str(player.id))
            response_time = request.POST.get("time_" + str(player.id))

            if answer and response_time:
                is_correct = answer.upper() == question.answer.upper()

                FFFResult.objects.create(
                    player=player,
                    answer=answer.upper(),
                    response_time=float(response_time),
                    is_correct=is_correct
                )

        winner = FFFResult.objects.filter(
            is_correct=True
        ).order_by("response_time").first()

        results = FFFResult.objects.all().order_by("response_time")

        if winner:
            request.session["hotseat_player_id"] = winner.player.id
            request.session["fff_question_id"] = question.id

        return render(
            request,
            "kbc/fff_result.html",
            {
                "winner": winner,
                "results": results
            }
        )

    return render(
        request,
        "kbc/fff.html",
        {
            "players": players,
            "question": question
        }
    )


def start_hotseat_game(request):
    hotseat_player_id = request.session.get("hotseat_player_id")
    fff_question_id = request.session.get("fff_question_id")

    if not hotseat_player_id:
        return redirect("fastest_finger")

    selected_questions = []

    levels = [
        ("simple", 3),
        ("medium", 3),
        ("hard", 3),
        ("hardest", 3),
        ("extreme", 3),
        ("ultimate", 1),
    ]

    for difficulty, count in levels:
        questions = Question.objects.filter(difficulty=difficulty)

        if fff_question_id:
            questions = questions.exclude(id=fff_question_id)

        questions = list(questions)

        if len(questions) < count:
            return redirect("fastest_finger")

        selected = random.sample(questions, count)

        for q in selected:
            selected_questions.append(q.id)

    request.session["selected_questions"] = selected_questions
    request.session["current_question"] = 0
    request.session["current_amount"] = "₹0"
    request.session["safe_amount"] = "₹0"
    request.session["fifty_used"] = False
    request.session["audience_used"] = False

    return redirect("hotseat")


def hotseat(request):
    player_id = request.session.get("hotseat_player_id")
    selected_questions = request.session.get("selected_questions")

    if not player_id:
        return redirect("fastest_finger")

    if not selected_questions:
        return redirect("start_hotseat_game")

    player = Player.objects.get(id=player_id)

    current_question = request.session.get("current_question", 0)

    if current_question >= 16:
        GameHistory.objects.create(
            player=player,
            amount_won="₹7 Crore",
            result="Winner"
        )

        return render(
            request,
            "kbc/winner.html",
            {
                "player": player,
                "amount": "₹7 Crore"
            }
        )

    current_prize = money[current_question]

    question_id = selected_questions[current_question]
    question = Question.objects.get(id=question_id)

    hidden_options = []
    votes = None

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "quit":
            amount = request.session.get("current_amount", "₹0")

            GameHistory.objects.create(
                player=player,
                amount_won=amount,
                result="Quit"
            )

            return render(
                request,
                "kbc/winner.html",
                {
                    "player": player,
                    "amount": amount
                }
            )

        elif action == "fifty":
            request.session["fifty_used"] = True

            all_options = ["A", "B", "C", "D"]
            wrong_options = []

            for option in all_options:
                if option != question.answer:
                    wrong_options.append(option)

            hidden_options = random.sample(wrong_options, 2)

        elif action == "audience":
            request.session["audience_used"] = True

            correct_vote = random.randint(50, 80)
            remaining = 100 - correct_vote

            votes = {
                "A": 0,
                "B": 0,
                "C": 0,
                "D": 0
            }

            votes[question.answer] = correct_vote

            other_options = ["A", "B", "C", "D"]
            other_options.remove(question.answer)

            vote1 = random.randint(0, remaining)
            vote2 = random.randint(0, remaining - vote1)
            vote3 = remaining - vote1 - vote2

            votes[other_options[0]] = vote1
            votes[other_options[1]] = vote2
            votes[other_options[2]] = vote3

        elif action == "answer":
            selected_answer = request.POST.get("answer")

            if selected_answer == question.answer:
                won_amount = money[current_question]

                request.session["current_amount"] = won_amount

                if current_question == 4:
                    request.session["safe_amount"] = "₹10,000"

                if current_question == 9:
                    request.session["safe_amount"] = "₹3,20,000"

                request.session["current_question"] = current_question + 1

                return render(
                    request,
                    "kbc/correct_answer.html",
                    {
                        "player": player,
                        "amount": won_amount
                    }
                )

            amount = request.session.get("safe_amount", "₹0")

            GameHistory.objects.create(
                player=player,
                amount_won=amount,
                result="Wrong Answer"
            )

            return render(
                request,
                "kbc/winner.html",
                {
                    "player": player,
                    "amount": amount,
                    "correct_answer": question.answer
                }
            )

    return render(
        request,
        "kbc/hotseat.html",
        {
            "player": player,
            "question": question,
            "question_number": current_question + 1,
            "current_prize": current_prize,
            "money": money,
            "current_amount": request.session.get("current_amount", "₹0"),
            "safe_amount": request.session.get("safe_amount", "₹0"),
            "fifty_used": request.session.get("fifty_used", False),
            "audience_used": request.session.get("audience_used", False),
            "hidden_options": hidden_options,
            "votes": votes,
        }
    )


def leaderboard(request):
    history = GameHistory.objects.all().order_by("-date")

    return render(
        request,
        "kbc/leaderboard.html",
        {
            "history": history
        }
    )