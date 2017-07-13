from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse

from user.models import UserProfile


# 食物的分类
class FoodCategory(models.Model):
    category_name = models.CharField(max_length=64, verbose_name="食品种类", default="好吃的")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "食品种类"
        verbose_name_plural = verbose_name


# 食物信息
class Food(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    description = models.TextField(verbose_name='描述')
    cover_image = models.ImageField(max_length=128, upload_to='food/cover/%Y/%m/%d', verbose_name='封面图片',default="image/dangao.jpg")
    link = models.URLField(verbose_name='来源链接', max_length=200, null=True, blank=True)
    category = models.ForeignKey(FoodCategory, verbose_name='分类')
    user = models.ForeignKey(UserProfile, related_name='foods_shared', verbose_name='创建用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    total_likenum = models.PositiveIntegerField(default=0, verbose_name="喜欢总数")
    total_dislikenum = models.PositiveIntegerField(default=0, verbose_name="不喜欢总数")
    total_wantnum = models.PositiveIntegerField(default=0, verbose_name="想吃这个美食的用户总数")
    total_atenum = models.PositiveIntegerField(default=0, verbose_name="吃过这个美食的用户总数")
    tags = models.CharField(max_length=64, default='', verbose_name='食物标签', help_text="请使用','将多个标签分隔开")

    def __str__(self):
        return self.title

    # 获取这个食物的所有的标签
    def get_tags_list(self):
        if self.tags:
            tags_list = self.tags.split(",")
        else:
            tags_list = []
        return tags_list

    # # 获取美食详情的界面的URL地址
    # def get_absolute_url(self):
    #     return reverse('food:fooddetail', kwargs={'food_id':self.id})


    class Meta:
        verbose_name = "食物信息"
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)