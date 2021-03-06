import uuid

from django.db import models


class NewsDetail(models.Model):
    nede_id = models.UUIDField(primary_key=True, default=uuid.uuid1, max_length=36, editable=False)
    # nede_classify = models.ForeignKey(NewsClassify, to_field='necl_name')
    nede_classify = models.ForeignKey('NewsClassify',
                                      null=True,
                                      on_delete=models.SET_NULL, to_field='necl_name')
    # 创建该条数据时的系统时间
    nede_create_date = models.DateField(auto_now_add=True)
    # 封面图片
    nede_cover_img = models.URLField(default="")
    nede_title = models.CharField(max_length=128)
    nede_author = models.CharField(max_length=64, default="佚名")
    # 爬取的文章上的时间，不是爬取文章存进数据库的时间，所以用CharField
    nede_web_time = models.CharField(max_length=32, null=True)
    nede_content = models.URLField(default="")
    # 阅读次数
    nede_browse = models.IntegerField(default=0)
    # 被喜欢的次数
    nede_love = models.IntegerField(default=0)

    class Meta:
        db_table = "news_detail"

    def __str__(self):
        return self.nede_title
