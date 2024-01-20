from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from users.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

PLANT_CHOICES = [
('african_violet', 'African Violet'),
('asparagus', 'Asparagus'),
('anthurium', 'Anthurium'),
('balm', 'Balm'),
('banana', 'Banana'),
('basil', 'Basil'),
('beans', 'Beans'),
('beetroot', 'Beetroot'),
('blueberry', 'Blueberry'),
('broccoli', 'Broccoli'),
('bromeliad', 'Bromeliad'),
('brussel_sprout', 'Brussel Sprout'),
('cabbage', 'Cabbage'),
('capsicum', 'Capsicum'),
('carrot', 'Carrot'),
('cauliflower', 'Cauliflower'),
('celery', 'Celery'),
('chives', 'Chives'),
('cucumber', 'Cucumber'),
('roses', 'Roses'),
('eggplant', 'Eggplant'),
('endive', 'Endive'),
('fennel', 'Fennel'),
('garlic', 'Garlic'),
('lavender', 'Lavender'),
('leek', 'Leek'),
('lettuce_fancy', 'Lettuce-Fancy'),
('lettuce_head', 'Lettuce-Head'),
('melons', 'Melons'),
('mint', 'Mint'),
('mustard_cress', 'Mustard/Cress'),
('onion', 'Onion'),
('parsley', 'Parsley'),
('passion_fruit', 'Passion Fruit'),
('pea', 'Pea'),
('pumpkin', 'Pumpkin'),
('radish', 'Radish'),
('rhubarb', 'Rhubarb'),
('roses', 'Roses'),
('sage', 'Sage'),
('spinach', 'Spinach'),
('silver_beet', 'Silver-beet'),
('squash', 'Squash'),
('strawberry', 'Strawberry'),
('thyme', 'Thyme'),
('tomato', 'Tomato'),
('turnip_parsnip', 'Turnip, Parsnip'),
('watercress', 'Watercress'), ]

class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    description = models.CharField(max_length=2000, null=True, blank=True)
    crop = models.CharField(max_length= 50, choices=PLANT_CHOICES,  default='african_violet')
    data = models.FileField(upload_to='static/uploads/', blank=True)
    guess = models.FloatField(default=0.0, blank=True)
    #tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
