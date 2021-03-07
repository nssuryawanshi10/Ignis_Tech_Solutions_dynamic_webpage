 class Like(models.Model):
    ''' like  comment '''

    comment = models.OneToOneField(Comment, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.comment)[:30]

class DisLike(models.Model):
    ''' Dislike  comment '''

    comment = models.OneToOneField(Comment, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment.comment)[:30]
