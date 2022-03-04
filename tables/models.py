from django.db import models

class User(models.Model):
    Username = models.CharField(max_length=256)
    Userid = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.Username

class Team(models.Model):
    teamid = models.IntegerField(default=0)
    teamname = models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.teamname

class Mapt(models.Model):
    rowid = models.IntegerField(default=0)
    Userid = models.IntegerField(default=0)
    teamid = models.IntegerField(default=0)

    def __str__(self):
        return self.rowid

