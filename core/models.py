from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

LEAGUE_CHOICES = (
(0, 'Standard'),
(1, '.5 PPR'),
(2, ' PPR'),
)
# Create your models here.
class Question(models.Model):
  league = models.IntegerField(choices=LEAGUE_CHOICES, default=0)
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("question_detail", args=[self.id])

class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __unicode__(self):
        return self.text

class Vote(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)

    def __unicode__(self):
        return "%s upvoted" % (self.user.username)