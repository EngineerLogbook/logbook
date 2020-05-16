from django.test import TestCase
from log.models import Logger, LogFile, LogURL
from project.models import Team,Project
from django.contrib.auth.models import User
from engbook.settings import BASE_DIR, os
from django.core.files import File
import datetime

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

        self.testlog = Logger.objects.create(
            title="Test Log",
            note=" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam purus eros, posuere et pharetra et, blandit ut ipsum. Cras id blandit dui. Nullam porttitor bibendum nisi. Donec mattis velit felis, ut vulputate leo varius vel. Maecenas et nisl sodales, bibendum metus vel, luctus risus. Aenean vestibulum in enim eget fermentum. Cras consequat, tortor vel pretium tempor, eros augue faucibus quam, non varius ex ipsum ullamcorper urna. Nam sed congue ex. Vestibulum in eros pellentesque, iaculis nulla et, accumsan metus. Quisque at accumsan mi, eget aliquet justo. Maecenas felis dui, rutrum sit amet facilisis nec, dictum id nisl. Mauris sed purus congue nunc sagittis vestibulum et quis nisl. Aliquam ut tristique enim. Mauris ut augue a tortor convallis ullamcorper sed eu urna. Cras ut justo turpis.",
            user=self.testuser1,
            project=self.testproject,

        )

    def test_log(self):
        pass
    # # Team tests
    # def test_team_creation_and_slug(self):        
    #     self.assertEquals(self.testteam.slug, 'test-team')

    # def test_team_date_creation(self):
    #     self.assertEquals(self.testteam.date_created.date(), datetime.date.today())
       
    # def test_team_user_assignment(self):
    #     self.assertEquals(self.testteam.members.all()[0].email, 'testingthemail@example.com')
    #     self.assertEquals(self.testteam.members.all()[1].username, 'testuser2')


    # # Project tests
    # def test_project_creation_and_slug(self):
    #     self.assertEquals(self.testproject.slug, 'test-project')

    # def test_project_date_creation(self):
    #     self.assertEquals(self.testproject.date_created.date(), datetime.date.today())
       
    # def test_project_image(self):
    #     self.testproject.image.save('test.png', File(
    #         open(os.path.join(BASE_DIR, 'project', 'test', 'image.png'), 'rb')))

    # def test_project_logo(self):
    #     self.testproject.logo.save('test.png', File(
    #         open(os.path.join(BASE_DIR, 'project', 'test', 'image.png'), 'rb')))

    # def test_project_team_assignment(self):
    #     self.assertEquals(self.testproject.team.title, 'Test Team')