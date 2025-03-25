from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Woman.Status.PUBLISHED)


class Woman(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Is published'

    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug', validators=(
        MinLengthValidator(limit_value=5, message='Required at least 5 symbols'),
        MaxLengthValidator(limit_value=100, message='Maximum is 100 symbols'),
    ))
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Photo')
    content = models.TextField(blank=True, verbose_name='Post Text')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Time of Update')
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT,
        verbose_name='Is Published')
    tags = models.ManyToManyField(to='TagPost', blank=True, related_name='tags', verbose_name='Tags')

    objects = models.Manager()
    published = PublishedManager()
    cat = models.ForeignKey(to='Category', on_delete=models.PROTECT, related_name='posts')
    husband = models.OneToOneField(to='Husband', on_delete=models.SET_NULL, null=True, blank=True, related_name='wuman',
                                   verbose_name='Husband')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='post', kwargs={'post_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(unidecode(str(self.title)))
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['-time_created']),
        ]
        verbose_name_plural = 'Famous women'
        verbose_name = 'Famous women'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse(viewname='tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')
