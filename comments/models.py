from django.db import models

# 评论模型
class Comment(models.Model):
    # 名字
    name = models.CharField(max_length=100)
    # 邮箱
    email = models.EmailField(max_length=225)
    # 个人网站
    url = models.URLField(blank=True)
    # 内容
    text = models.TextField()
    # 评论时间
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog_app.Post')

    def __str__(self):
        return self.text[ :20]

