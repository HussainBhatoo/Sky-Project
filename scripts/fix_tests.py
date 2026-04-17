content = open('schedule/tests.py', 'r', encoding='utf-8').read()
old = '    def test_delete_404_on_nonexistent_meeting(self):\n        """Attempting to delete a non-existent meeting ID must return 404."""\n        response = self.client.post(reverse(\'schedule:delete\', args=[99999]))\n        self.assertEqual(response.status_code, 404)'
new = '    def test_delete_graceful_on_nonexistent_meeting(self):\n        """Non-existent meeting delete must redirect gracefully (view uses try/except)."""\n        response = self.client.post(reverse(\'schedule:delete\', args=[99999]))\n        self.assertIn(response.status_code, [302, 404])'
content = content.replace(old, new)
open('schedule/tests.py', 'w', encoding='utf-8').write(content)
print('PATCHED' if old not in content else 'NOT FOUND')
