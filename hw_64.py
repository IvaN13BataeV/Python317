from jinja2 import Template

html = '''
{%- macro get_input(name, type='text', data_name='') -%}
    <input type="{{type}}" name="{{name}}" placeholder="{{data_name}}">
{%- endmacro %}

<p>{{ get_input('firstname', data_name='Имя' ) }}</p>
<p>{{ get_input('lastname', data_name='Фамилия') }}</p>
<p>{{ get_input('address', data_name='Адрес') }}</p>
<p>{{ get_input('phone', 'tel', 'Телефон') }}</p>
<p>{{ get_input('email', 'email', 'Почта') }}</p>
'''

tm = Template(html)
msg = tm.render()

print(msg)
