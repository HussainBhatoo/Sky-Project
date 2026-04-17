content = open('templates/schedule/calendar.html', 'r', encoding='utf-8').read()
old = '<div id="meeting-form" style="display: none;" class="card animate-slide-up mb-3" style="max-width: 600px;">'
new = '<div id="meeting-form" class="card animate-slide-up mb-3" style="display: {% if show_form %}block{% else %}none{% endif %}; max-width: 640px;">'
if old in content:
    content = content.replace(old, new)
    print('PATCHED form div OK')
else:
    print('Not found - checking actual string')
    idx = content.find('id="meeting-form"')
    print(repr(content[idx:idx+150]))
open('templates/schedule/calendar.html', 'w', encoding='utf-8').write(content)
