from jinja2 import Template

pages = [
    {"link": "index", "header": "Главная"},
    {"link": "news", "header": "Новости"},
    {"link": "about", "header": "О компании"},
    {"link": "shop", "header": "Магазин"},
    {"link": "contacts", "header": "Контакты"},
]

html = """
<ul>
{% for page in pages -%}
{% if page['header'] == "Главная" -%}
<li><a href="/{{page['link']}}" class="active">{{page['header']}}</a></li>
{% else -%}
<li><a href="/{{page['link']}}">{{page['header']}}</a></li>
{% endif -%}
{% endfor -%}
</ul>
"""

tm = Template(html)
msg = tm.render(pages=pages)

print(msg)
