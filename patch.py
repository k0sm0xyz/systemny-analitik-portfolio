import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Цветовые стили для разных символов
g = '<span style="color: #00ff00;">•</span>' # Зеленый
y = '<span style="color: #ffff00;">•</span>' # Желтый
r = '<span style="color: #ff0000;">•</span>' # Красный
s = ' '

# Собираем цветной логотип построчно с правильными пропорциями (буквы меньше нулей)
colored_logo = f"""<pre class="matrix">
{g}{s}{g}{s}{s}{s}{s}{y}{y}{y}{y}{y}{y}{y}{y}{s}{s}{s}{s}{r}{r}{r}{r}{r}{s}{s}{s}{s}{g}{s}{g}{s}{g}{s}{s}{s}{s}{y}{y}{y}{y}{y}{y}{y}{y}{s}{s}{s}{s}{r}{s}{r}{s}{s}{s}{s}{g}{s}{g}{s}{s}{s}{s}{y}{y}{y}{y}{y}
{g}{g}{s}{s}{s}{s}{y}{s}{s}{s}{s}{s}{s}{s}{y}{s}{s}{s}{s}{r}{s}{s}{s}{s}{s}{s}{s}{s}{s}{g}{g}{g}{s}{g}{g}{s}{s}{s}{y}{s}{s}{s}{s}{s}{s}{s}{y}{s}{s}{s}{s}{r}{s}{s}{s}{s}{s}{s}{s}{s}{s}{g}{s}{s}{s}{s}{s}{s}{s}{s}{s}{y}
{g}{s}{g}{s}{s}{s}{s}{y}{y}{y}{y}{y}{y}{y}{y}{s}{s}{s}{s}{r}{r}{r}{r}{s}{s}{s}{s}{s}{s}{g}{s}{s}{s}{g}{s}{s}{s}{s}{y}{y}{y}{y}{y}{y}{y}{y}{s}{s}{s}{s}{r}{s}{r}{s}{s}{s}{s}{g}{g}{g}{s}{s}{s}{s}{y}{y}{y}{y}{y}
</pre>"""

content = re.sub(r"<pre class=\"matrix\">.*?</pre>", colored_logo, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
