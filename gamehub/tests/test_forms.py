from django.test import SimpleTestCase
from gamehub.forms import CommentForm

class TestFroms(SimpleTestCase):

    def test_comment_form_valid_data(self):
        form = CommentForm(data ={
            'content': 'This is a test content',
            'quality_rate': 2,
            'music_rate': 2,
            'community_rate': 2,
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)