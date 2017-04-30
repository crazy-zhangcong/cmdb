from django.db import models

# Create your models here.


class IDC(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    """存储所有主机"""
    hostname = models.CharField(max_length=64)
    ip_addr = models.GenericIPAddressField(unique=True)
    port = models.PositiveSmallIntegerField(default=22)
    idc = models.ForeignKey("IDC")
    enabled = models.BooleanField(default=True, verbose_name="是否启用")

    def __str__(self):
        return self.ip_addr


class HostGroup(models.Model):
    """主机组"""
    name = models.CharField(max_length=64, unique=True)
    hosts = models.ManyToManyField("Host")

    def __str__(self):
        return self.name


class RemoteUser(models.Model):
    """存储远程用户名密码"""
    username = models.CharField(max_length=64)
    auth_type_choices = (
        (0, "ssh/password"),
        (1, "ssh/key"),
    )
    auth_type = models.SmallIntegerField(choices=auth_type_choices, default=0)
    password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return "%s(%s)" % (self.username, self.auth_type)

    class Meta:
        unique_together = ('username', 'auth_type', 'password')


class UserProfile(models.Model):
    """堡垒机账号"""
    pass

