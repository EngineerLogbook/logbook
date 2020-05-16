from django.test import TestCase
from log.models import Logger, LogFile, LogURL
from project.models import Team,Project
from django.contrib.auth.models import User
from django.core.files import File
import datetime, mock

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

    # Log tests
    def test_log_creation_and_slug(self):        
        self.assertEquals(self.testlog.slug, 'test-log')

    def test_log_date_creation_and_modification(self):
        self.assertEquals(self.testlog.date_created.date(), datetime.date.today())
        self.testlog.title="Test Log Modified"
        self.testlog.save()
        self.assertTrue(self.testlog.date_created < self.testlog.date_modified)
       
    def test_log_user_assignment(self):
        self.assertEquals(self.testlog.user, self.testuser1)

    def test_log_project_assignment(self):
        self.assertEquals(self.testlog.project, self.testproject)
    
    def test_log_file_assosciation(self):
        file_mock = mock.MagicMock(spec=File)
        file_mock.name = 'test.pdf'
        
        self.logfile = LogFile.objects.create(
            title='testfile',
            file=file_mock,
            log=self.testlog
        )
        self.assertEquals(Logger.objects.filter(logfile__title='testfile').first(), self.testlog) 

    def test_log_url_assosciation(self):
        self.logurl = LogURL.objects.create(
            url="https://google.com",
            log=self.testlog
        )
        self.assertEquals(Logger.objects.filter(logurl__url="https://google.com").first(), self.testlog) 
               
