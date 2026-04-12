"""
SCHEDULE APP — COMPREHENSIVE TEST SUITE
Student 4: Maurya Patel | W2112200
5COSC021W Software Development Group Project — CWK2

Tests all schedule functionality including:
- Authentication redirects
- Calendar view rendering (GET)
- Meeting creation (POST valid + POST invalid)
- Meeting deletion (POST)
- Team filter (GET with ?team_id param)
- Calendar data integrity
- Audit log creation on CRUD
- Form validation rules
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta

from core.models import User, Team, Department, Meeting, AuditLog


class ScheduleTestSetup(TestCase):
    """Shared setup for all schedule tests."""

    def setUp(self):
        """
        Creates a test user, department, team, and client for all tests.
        """
        self.client = Client()

        # Create test user
        self.user = User.objects.create_user(
            username='testuser_schedule',
            password='TestPass123!',
            email='testuser@sky.com',
            first_name='Test',
            last_name='User',
        )

        # Create department & team (required FKs for Meeting)
        self.dept = Department.objects.create(
            department_name='Test Department',
            department_lead_name='Lead Person',
            description='Test dept description',
        )
        self.team = Team.objects.create(
            department=self.dept,
            team_name='Test Team Alpha',
            work_stream='Backend',
            project_name='Test Project',
            project_codebase='test-repo',
        )

        self.client.login(username='testuser_schedule', password='TestPass123!')


class ScheduleAuthenticationTest(ScheduleTestSetup):
    """
    Test that all schedule views require authentication.
    Unauthenticated users must be redirected to the login page.
    """

    def test_calendar_requires_login(self):
        """Calendar view must redirect unauthenticated users to login."""
        self.client.logout()
        response = self.client.get(reverse('schedule:calendar'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_create_requires_login(self):
        """Create view must redirect unauthenticated users."""
        self.client.logout()
        response = self.client.get(reverse('schedule:create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    def test_delete_requires_login(self):
        """Delete view must redirect unauthenticated users."""
        meeting = Meeting.objects.create(
            created_by_user=self.user,
            team=self.team,
            meeting_title='Delete Auth Test',
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=1),
            platform_type='zoom',
            agenda_text='Test',
        )
        self.client.logout()
        response = self.client.post(reverse('schedule:delete', args=[meeting.meeting_id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)


class ScheduleCalendarViewTest(ScheduleTestSetup):
    """
    Tests for the main calendar GET view (schedule_calendar).
    Verifies template rendering, context data, and calendar grid.
    """

    def test_calendar_get_status_200(self):
        """Calendar view returns HTTP 200 for authenticated user."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertEqual(response.status_code, 200)

    def test_calendar_uses_correct_template(self):
        """Calendar view uses schedule/calendar.html template."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertTemplateUsed(response, 'schedule/calendar.html')

    def test_calendar_context_has_meetings(self):
        """Calendar context must include meetings queryset."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertIn('meetings', response.context)

    def test_calendar_context_has_form(self):
        """Calendar context must include MeetingForm for inline creation."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertIn('form', response.context)

    def test_calendar_context_has_calendar_days(self):
        """Calendar context must include calendar_days list."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertIn('calendar_days', response.context)
        days = response.context['calendar_days']
        self.assertGreater(len(days), 27)  # All months have 28+ days
        self.assertLessEqual(len(days), 31)

    def test_calendar_context_has_month_name(self):
        """Calendar context must include month_name string."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertIn('month_name', response.context)
        self.assertTrue(len(response.context['month_name']) > 0)

    def test_calendar_context_has_teams(self):
        """Calendar context must include teams for the filter dropdown."""
        response = self.client.get(reverse('schedule:calendar'))
        self.assertIn('teams', response.context)

    def test_calendar_shows_existing_meeting(self):
        """A pre-existing meeting must appear in the meetings context."""
        meeting = Meeting.objects.create(
            created_by_user=self.user,
            team=self.team,
            meeting_title='Visible Sprint Review',
            start_datetime=timezone.now() + timedelta(days=2),
            end_datetime=timezone.now() + timedelta(days=2, hours=1),
            platform_type='teams',
            agenda_text='Quarterly review agenda',
        )
        response = self.client.get(reverse('schedule:calendar'))
        self.assertIn(meeting, response.context['meetings'])

    def test_calendar_team_filter(self):
        """Passing ?team_id=X must filter meetings to that team only."""
        other_dept = Department.objects.create(
            department_name='Other Dept',
            department_lead_name='Other Lead',
            description='Other',
        )
        other_team = Team.objects.create(
            department=other_dept,
            team_name='Other Team',
            work_stream='Frontend',
            project_name='Other Project',
            project_codebase='other-repo',
        )
        m1 = Meeting.objects.create(
            created_by_user=self.user, team=self.team,
            meeting_title='Meeting for Alpha',
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=1),
            platform_type='zoom', agenda_text='Alpha agenda',
        )
        m2 = Meeting.objects.create(
            created_by_user=self.user, team=other_team,
            meeting_title='Meeting for Other',
            start_datetime=timezone.now() + timedelta(days=2),
            end_datetime=timezone.now() + timedelta(days=2, hours=1),
            platform_type='teams', agenda_text='Other agenda',
        )
        response = self.client.get(
            reverse('schedule:calendar') + f'?team_id={self.team.team_id}'
        )
        meetings_in_context = list(response.context['meetings'])
        self.assertIn(m1, meetings_in_context)
        self.assertNotIn(m2, meetings_in_context)

    def test_calendar_show_form_flag_on_new_param(self):
        """?new=true must set show_form=True in context."""
        response = self.client.get(reverse('schedule:calendar') + '?new=true')
        self.assertTrue(response.context.get('show_form', False))

    def test_calendar_day_with_meeting_has_event_flag(self):
        """A calendar day matching a meeting's date must have has_event=True."""
        today = timezone.now()
        # Create a meeting exactly today
        Meeting.objects.create(
            created_by_user=self.user,
            team=self.team,
            meeting_title='Today Meeting',
            start_datetime=today,
            end_datetime=today + timedelta(hours=1),
            platform_type='in_person',
            agenda_text='Today agenda',
        )
        response = self.client.get(reverse('schedule:calendar'))
        calendar_days = response.context['calendar_days']
        today_day = next((d for d in calendar_days if d['is_today']), None)
        self.assertIsNotNone(today_day)
        self.assertTrue(today_day['has_event'])


class ScheduleCreateMeetingTest(ScheduleTestSetup):
    """
    Tests for meeting creation (schedule_create view).
    Covers valid data, invalid data, field requirements, and audit logging.
    """

    def _valid_post_data(self, title='Test Sprint Planning') -> dict:
        """Returns a valid POST payload for creating a meeting."""
        start = timezone.now() + timedelta(days=3)
        end = start + timedelta(hours=1)
        return {
            'meeting_title': title,
            'team': self.team.team_id,
            'start_datetime': start.strftime('%Y-%m-%dT%H:%M'),
            'end_datetime': end.strftime('%Y-%m-%dT%H:%M'),
            'platform_type': 'teams',
            'meeting_link': 'https://teams.microsoft.com/test',
            'agenda_text': 'Sprint planning for Q2 2026',
        }

    def test_create_valid_meeting_redirects_to_calendar(self):
        """Valid POST to create must redirect (302) to the calendar."""
        response = self.client.post(reverse('schedule:create'), self._valid_post_data())
        self.assertRedirects(response, reverse('schedule:calendar'))

    def test_create_valid_meeting_saves_to_database(self):
        """Valid POST must create exactly one new Meeting record."""
        initial_count = Meeting.objects.count()
        self.client.post(reverse('schedule:create'), self._valid_post_data())
        self.assertEqual(Meeting.objects.count(), initial_count + 1)

    def test_create_meeting_sets_created_by_user(self):
        """Created meeting must have created_by_user set to logged-in user."""
        self.client.post(reverse('schedule:create'), self._valid_post_data(title='User Attribution Test'))
        meeting = Meeting.objects.get(meeting_title='User Attribution Test')
        self.assertEqual(meeting.created_by_user, self.user)

    def test_create_meeting_creates_audit_log(self):
        """Creating a meeting must generate a CREATE AuditLog entry."""
        initial_logs = AuditLog.objects.count()
        self.client.post(reverse('schedule:create'), self._valid_post_data(title='Audit Log Test Meet'))
        meeting = Meeting.objects.get(meeting_title='Audit Log Test Meet')
        new_log = AuditLog.objects.filter(
            action_type='CREATE',
            entity_type='Meeting',
            entity_id=meeting.meeting_id,
        )
        self.assertTrue(new_log.exists())
        self.assertEqual(AuditLog.objects.count(), initial_logs + 1)

    def test_create_missing_title_fails(self):
        """POST without meeting_title must not create a meeting."""
        data = self._valid_post_data()
        data['meeting_title'] = ''
        initial_count = Meeting.objects.count()
        response = self.client.post(reverse('schedule:create'), data)
        self.assertEqual(Meeting.objects.count(), initial_count)
        # Should re-render (200) not redirect (302)
        self.assertEqual(response.status_code, 200)

    def test_create_missing_team_fails(self):
        """POST without team selection must not create a meeting."""
        data = self._valid_post_data()
        data['team'] = ''
        initial_count = Meeting.objects.count()
        response = self.client.post(reverse('schedule:create'), data)
        self.assertEqual(Meeting.objects.count(), initial_count)

    def test_create_missing_platform_fails(self):
        """POST without platform_type must not create a meeting."""
        data = self._valid_post_data()
        data['platform_type'] = ''
        initial_count = Meeting.objects.count()
        response = self.client.post(reverse('schedule:create'), data)
        self.assertEqual(Meeting.objects.count(), initial_count)

    def test_create_invalid_platform_choice_fails(self):
        """POST with an invalid platform_type must not create a meeting."""
        data = self._valid_post_data()
        data['platform_type'] = 'invalid_platform'
        initial_count = Meeting.objects.count()
        response = self.client.post(reverse('schedule:create'), data)
        self.assertEqual(Meeting.objects.count(), initial_count)

    def test_create_optional_meeting_link(self):
        """meeting_link is optional - creation should succeed without it."""
        data = self._valid_post_data(title='No Link Meeting')
        data['meeting_link'] = ''
        response = self.client.post(reverse('schedule:create'), data)
        self.assertEqual(Meeting.objects.filter(meeting_title='No Link Meeting').count(), 1)

    def test_create_get_redirects_to_calendar_with_new_param(self):
        """GET to create view must redirect to ?new=true on calendar."""
        response = self.client.get(reverse('schedule:create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/schedule/', response.url)
        self.assertIn('new=true', response.url)

    def test_create_all_platform_types_valid(self):
        """All four platform choices must be accepted by the form."""
        for platform in ['teams', 'zoom', 'google_meet', 'in_person']:
            data = self._valid_post_data(title=f'Platform Test {platform}')
            data['platform_type'] = platform
            response = self.client.post(reverse('schedule:create'), data)
            self.assertRedirects(response, reverse('schedule:calendar'), msg_prefix=f'Failed for {platform}')


class ScheduleDeleteMeetingTest(ScheduleTestSetup):
    """
    Tests for meeting deletion (schedule_delete view).
    Covers POST success, GET safety, and audit log entries.
    """

    def _create_test_meeting(self, title='Delete Test Meeting') -> Meeting:
        """Helper to create a meeting for deletion tests."""
        return Meeting.objects.create(
            created_by_user=self.user,
            team=self.team,
            meeting_title=title,
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=1),
            platform_type='zoom',
            agenda_text='To be deleted',
        )

    def test_delete_removes_meeting_from_database(self):
        """POST delete must remove the meeting from the database."""
        meeting = self._create_test_meeting()
        meeting_id = meeting.meeting_id
        self.client.post(reverse('schedule:delete', args=[meeting_id]))
        self.assertFalse(Meeting.objects.filter(meeting_id=meeting_id).exists())

    def test_delete_redirects_to_calendar(self):
        """Successful delete must redirect to the calendar view."""
        meeting = self._create_test_meeting()
        response = self.client.post(reverse('schedule:delete', args=[meeting.meeting_id]))
        self.assertRedirects(response, reverse('schedule:calendar'))

    def test_delete_creates_audit_log(self):
        """Deleting a meeting must generate a DELETE AuditLog entry."""
        meeting = self._create_test_meeting(title='Audit Delete Test')
        meeting_id = meeting.meeting_id
        log_count_before = AuditLog.objects.count()
        self.client.post(reverse('schedule:delete', args=[meeting_id]))
        self.assertEqual(AuditLog.objects.count(), log_count_before + 1)
        log = AuditLog.objects.filter(action_type='DELETE', entity_id=meeting_id)
        self.assertTrue(log.exists())

    def test_delete_graceful_on_nonexistent_meeting(self):
        """Non-existent meeting delete must redirect gracefully (view uses try/except)."""
        response = self.client.post(reverse('schedule:delete', args=[99999]))
        self.assertIn(response.status_code, [302, 404])

    def test_delete_get_request_does_not_delete(self):
        """GET to delete URL must NOT delete the meeting (only POST should)."""
        meeting = self._create_test_meeting()
        meeting_id = meeting.meeting_id
        self.client.get(reverse('schedule:delete', args=[meeting_id]))
        self.assertTrue(Meeting.objects.filter(meeting_id=meeting_id).exists())


class ScheduleMeetingModelTest(ScheduleTestSetup):
    """
    Tests for the Meeting model itself (Entity 12 from ERD).
    """

    def test_meeting_str_returns_title(self):
        """Meeting __str__ must return meeting_title."""
        meeting = Meeting.objects.create(
            created_by_user=self.user,
            team=self.team,
            meeting_title='Model String Test',
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=1),
            platform_type='teams',
            agenda_text='Test',
        )
        self.assertEqual(str(meeting), 'Model String Test')

    def test_meeting_team_fk_cascade_delete(self):
        """Deleting a team must cascade-delete its meetings."""
        temp_team = Team.objects.create(
            department=self.dept,
            team_name='Temp Cascade Team',
            work_stream='QA',
            project_name='Cascade Project',
            project_codebase='cascade-repo',
        )
        Meeting.objects.create(
            created_by_user=self.user,
            team=temp_team,
            meeting_title='Cascade Test Meeting',
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=1),
            platform_type='zoom',
            agenda_text='Cascade test',
        )
        temp_team.delete()
        self.assertFalse(Meeting.objects.filter(meeting_title='Cascade Test Meeting').exists())

    def test_meeting_platform_choices_enforced(self):
        """Meeting model has exactly 4 platform choices as per ERD."""
        choices = dict(Meeting.PLATFORM_CHOICES)
        self.assertEqual(len(choices), 4)
        self.assertIn('teams', choices)
        self.assertIn('zoom', choices)
        self.assertIn('google_meet', choices)
        self.assertIn('in_person', choices)
