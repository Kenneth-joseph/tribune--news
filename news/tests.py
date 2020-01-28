from django.test import TestCase
from .models import Editor, Article, Tags


class EditorTestCase(TestCase):

    # set up method
    def setUp(self):
        self.james = Editor(first_name='james', last_name='Mark', email='james@moringaschool.com')

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    # Testing save Methods
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

# Create your tests here.
