# Trofim CRM Bot system with GUI on Desktop

version 0.1-dev 17.06.2025

MIT License

## About 

[RUSSIAN]

Этот проект автоматизирует мое планирование бизнес-процессов
у меня и помогает планировать свое время эффективнее.

Важное замечание оно **НЕ ЗАМЕНЯЕТ** личное общение
с клиентами и друзьями. А помогает рассчитать и распланировать
время.

## Structure project

[RUSSIAN]

Проект делится на две главные части:
1) <code>./src</code> - здесь находится клиентская часть ПО с графическим интерфейсом.
2) <code>./services</code> - здесь находятся код серверов на которых запущены боты.

Общая структура:

+ src
+ - config
+ - img
+ - models
+ - main.py
+ services
+ - tg_bot_server
+ - + .venv
+ - + config
+ - + main.py
+ - vk_bot_server
+ - + .venv
+ - + config
+ - + main.py
+ .venv
+ docker-compose.yaml
+ .gitignore
+ LICENSE

### <code>./src</code> - Structure project
( Desktop client app )

### <code>./services</code> - Structure project
( Server services app-s ) 