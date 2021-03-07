models.py :-

class Comment(models.Model):
    ''' Main comment model'''
    user =  models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(validators=[MinLengthValidator(150)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def __str__(self):
        return str(self.comment)[:30]
