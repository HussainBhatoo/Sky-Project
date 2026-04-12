from django import forms
from core.models import Meeting, Team


class MeetingForm(forms.ModelForm):
    """
    Form for creating new meetings within the Sky Engineering Schedule module.
    Applies the Sky Spectrum design system CSS classes to all widgets.
    """

    class Meta:
        model = Meeting
        fields = [
            'meeting_title',
            'team',
            'start_datetime',
            'end_datetime',
            'platform_type',
            'meeting_link',
            'agenda_text',
        ]
        widgets = {
            'meeting_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Sprint Review Q2',
                'id': 'id_meeting_title',
            }),
            'team': forms.Select(attrs={
                'class': 'form-control filter-select',
                'id': 'id_team',
            }),
            'start_datetime': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'id': 'id_start_datetime',
            }),
            'end_datetime': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'id': 'id_end_datetime',
            }),
            'platform_type': forms.Select(attrs={
                'class': 'form-control filter-select',
                'id': 'id_platform_type',
            }),
            'meeting_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://teams.microsoft.com/...',
                'id': 'id_meeting_link',
            }),
            'agenda_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the meeting agenda...',
                'rows': 4,
                'id': 'id_agenda_text',
            }),
        }
        labels = {
            'meeting_title': 'Meeting Title',
            'team': 'Assign Team',
            'start_datetime': 'Start Date & Time',
            'end_datetime': 'End Date & Time',
            'platform_type': 'Platform',
            'meeting_link': 'Meeting Link (optional)',
            'agenda_text': 'Agenda',
        }
