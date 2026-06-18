from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    answer = models.CharField(max_length=1)
    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return self.question


class GameHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    amount_won = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player.name


class FFFResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)
    response_time = models.FloatField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.player.name