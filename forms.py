class CommentForm(forms.ModelForm):

    class Meta:
        model = my_models.Comment
        fields = ('comment',)
        widgets = {
          'comment': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }
