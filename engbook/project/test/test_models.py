from django.test import TestCase
from project.models import Project, Team
from django.contrib.auth.models import User
from django.core.files import File
import datetime,mock
from django.core.files.uploadedfile import SimpleUploadedFile


class TestModels(TestCase):

    def setUp(self):
        self.testuser1 = User.objects.create_user(
            'testuser1', password='testpassword', email="testingthemail@example.com")
        self.testuser2 = User.objects.create_user(
            'testuser2', password='testpassword')

        self.testteam = Team.objects.create(
            title='Test Team',
            description='Testing the team model',
        )
        self.testteam.save()
        self.testteam.members.set([self.testuser1, self.testuser2])
        self.testteam.save()

        self.testproject = Project.objects.create(
            title="Test Project",
            description="testing the project model",
            team=self.testteam,

        )

    # Team tests
    def test_team_creation_and_slug(self):        
        self.assertEquals(self.testteam.slug, 'test-team')

    def test_team_date_creation(self):
        self.assertEquals(self.testteam.date_created.date(), datetime.date.today())
       
    def test_team_user_assignment(self):
        self.assertEquals(list(self.testteam.members.all()), [self.testuser1,self.testuser2])


    # Project tests
    def test_project_creation_and_slug(self):
        self.assertEquals(self.testproject.slug, 'test-project')

    def test_project_date_creation(self):
        self.assertEquals(self.testproject.date_created.date(), datetime.date.today())
    
    # If this doesn't error out, file uploading was successful       
    def test_project_image(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.png'
                
        self.testproject.image = file_mock
        self.testproject.save()
        
        self.assertIsNotNone(self.testproject.image)

    # If this doesn't error out, file uploading was successful       
    def test_project_logo(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.png'
                
        self.testproject.logo = file_mock
        self.testproject.save()
        
        self.assertIsNotNone(self.testproject.logo)

    def test_project_team_assignment(self):
        self.assertEquals(self.testproject.team, self.testteam)