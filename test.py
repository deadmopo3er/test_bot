import os

# Создаем базовую структуру
os.mkdir('event_bot')
os.mkdir('event_bot/config')
os.mkdir('event_bot/models')
os.mkdir('event_bot/handlers')
os.mkdir('event_bot/services')
os.mkdir('event_bot/utils')

# Создаем файлы в директории config
with open('event_bot/config/settings.py', 'w') as f:
    pass

# Создаем файлы в директории models
with open('event_bot/models/__init__.py', 'w') as f:
    pass

with open('event_bot/models/event.py', 'w') as f:
    pass

with open('event_bot/models/user.py', 'w') as f:
    pass

# Создаем файлы в директории handlers
with open('event_bot/handlers/__init__.py', 'w') as f:
    pass

with open('event_bot/handlers/common.py', 'w') as f:
    pass

with open('event_bot/handlers/event.py', 'w') as f:
    pass

with open('event_bot/handlers/user.py', 'w') as f:
    pass

# Создаем файлы в директории services
with open('event_bot/services/__init__.py', 'w') as f:
    pass

with open('event_bot/services/database.py', 'w') as f:
    pass

with open('event_bot/services/event_service.py', 'w') as f:
    pass

with open('event_bot/services/user_service.py', 'w') as f:
    pass

# Создаем файлы в директории utils
with open('event_bot/utils/__init__.py', 'w') as f:
    pass

with open('event_bot/utils/keyboard.py', 'w') as f:
    pass

# Создаем файл main.py
with open('event_bot/main.py', 'w') as f:
    pass

# Создаем файл requirements.txt
with open('event_bot/requirements.txt', 'w') as f:
    pass
