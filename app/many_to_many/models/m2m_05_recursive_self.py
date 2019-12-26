from django.db import models


class TwitterUser(models.Model):
    name = models.CharField(max_length=20)
    following = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False)

    def __str__(self):
        return self.name


# 위 M2M필드 생성 시 암시적으로 자동 생성 되는 테이블의 모습
# 실제로 사용되지 않음
class TwitterUserFollowing(models.Model):
    from_twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    to_twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
