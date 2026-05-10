from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'blog_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'blog_tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog_comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.name} - {self.blog.title}"
