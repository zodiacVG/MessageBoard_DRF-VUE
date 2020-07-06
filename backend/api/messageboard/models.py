from django.db import models

# Create your models here.
class Note(models.Model):
    commitid=models.AutoField(primary_key=True)  #评论id
    userid=models.IntegerField(default=0000000)                   #用户id
    username=models.CharField(default='游客', max_length=20)
    committime=models.DateTimeField(auto_now_add=True)      #评论时间，希望能够实现自动记录时间戳（暂不清楚格式）
    upvote=models.IntegerField(default=0)            
    downvote=models.IntegerField(default=0)
    content=models.TextField()
    
