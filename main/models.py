from django.db import models
from accounts.models import User

class Post(models.Model):

    CATEGORY_CHOICES = [
        ('地理', '地理'),
        ('歴史', '歴史'),
        ('人物', '人物'),
        ('自然', '自然'),
        ('伝統', '伝統'),
        ('スポーツ', 'スポーツ'),
        ('食', '食'),
        ('文化', '文化'),
        ('芸能', '芸能'),
        ('特産品', '特産品'),
        ('方言', '方言'),
        ('その他', 'その他'),
    ]

    PREFECTURE_CHOICES = [
        ('北海道', '北海道'),
        ('青森県', '青森県'),
        ('岩手県', '岩手県'),
        ('宮城県', '宮城県'),
        ('秋田県', '秋田県'),
        ('山形県', '山形県'),
        ('福島県', '福島県'),
        ('茨城県', '茨城県'),
        ('栃木県', '栃木県'),
        ('群馬県', '群馬県'),
        ('埼玉県', '埼玉県'),
        ('千葉県', '千葉県'),
        ('東京都', '東京都'),
        ('神奈川県', '神奈川県'),
        ('新潟県', '新潟県'),
        ('富山県', '富山県'),
        ('石川県', '石川県'),
        ('福井県', '福井県'),
        ('山梨県', '山梨県'),
        ('長野県', '長野県'),
        ('岐阜県', '岐阜県'),
        ('静岡県', '静岡県'),
        ('愛知県', '愛知県'),
        ('三重県', '三重県'),
        ('滋賀県', '滋賀県'),
        ('京都府', '京都府'),
        ('大阪府', '大阪府'),
        ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'),
        ('和歌山県', '和歌山県'),
        ('鳥取県', '鳥取県'),
        ('島根県', '島根県'),
        ('岡山県', '岡山県'),
        ('広島県', '広島県'),
        ('山口県', '山口県'),
        ('徳島県', '徳島県'),
        ('香川県', '香川県'),
        ('愛媛県', '愛媛県'),
        ('高知県', '高知県'),
        ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'),
        ('長崎県', '長崎県'),
        ('熊本県', '熊本県'),
        ('大分県', '大分県'),
        ('宮崎県', '宮崎県'),
        ('鹿児島県', '鹿児島県'),
        ('沖縄県', '沖縄県'),
    ]

    title = models.CharField(verbose_name="タイトル", max_length=20)
    category = models.CharField(verbose_name="カテゴリ", max_length=20, choices=CATEGORY_CHOICES)
    prefecture = models.CharField(verbose_name="都道府県", max_length=20, choices=PREFECTURE_CHOICES)
    content = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='related_post', blank=True)

    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'posts'
        ordering = ["-create_at"]

class Comment(models.Model):
    content = models.TextField(verbose_name="コメント")
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.create_at
    
    class Meta:
        db_table = 'comments'
        ordering = ["-create_at"]