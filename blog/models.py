from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta():
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug
    

class Post(models.Model):
    ACTIVE = 'Active'
    DRAFT = 'draft'
    CHOICES_STATUS = (
        (ACTIVE , 'Active'),
        (DRAFT, 'Draft')
    )
    category = models.ForeignKey(Category, null=True, blank=True, related_name='posts', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)

    slug = models.SlugField(max_length=255, unique=True)

    intro = models.TextField()
    intro_ar = models.TextField()

    body = models.TextField()
    body_ar = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    image = models.ImageField(upload_to = 'uploads/', blank=True, null=True)


    def __str__(self):

        return f"{self.title} - {self.created_at.date()}"

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug ,self.slug)
