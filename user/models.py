from django.db import models


class UserInfo(models.Model):
    gender_choices = [
        (1,"男"),
        (0, "女"),
    ]
    user = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    email = models.EmailField(verbose_name="邮箱", max_length=32)
    mobile_phone = models.CharField(verbose_name="手机号", max_length=32)
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    class Meta:
        # verbose_name = "用户信息"
        # verbose_name_plural = "用户信息"
        pass

    def __str__(self):
        return self.user

