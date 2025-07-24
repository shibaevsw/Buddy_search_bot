1. Список всех отслеживаемых файлов
bash
git ls-files
Показывает все файлы в индексе (включая подмодули).

Пример вывода:

text
README.md
src/main.js
.gitignore
2. Компактный статус с флагом -s
bash
git status -s
Отслеживаемые файлы помечаются буквами в левой колонке:

A — добавлен в индекс.

M — изменён и добавлен в индекс.

(пробел) — изменения не добавлены в индекс.

Неотслеживаемые файлы помечаются как ??.

Пример:

text
A  new-file.txt
M  modified-file.js
 M unstaged-change.md
?? untracked-file.log
3. Детализированный статус
bash
git status
В разделе Changes to be committed перечислены файлы, добавленные в индекс (отслеживаемые).

В разделе Untracked files — неотслеживаемые файлы.

Примеры использования
Команда	Что показывает?
git ls-files	Все файлы в индексе (простой список).
git status -s	Статус файлов: A, M — отслеживаемые; ?? — неотслеживаемые.
git status	Детальный отчет с разделами для отслеживаемых и неотслеживаемых файлов.
Важно!
Файл считается отслеживаемым, если он был добавлен в Git командой git add.

Если файл игнорируется (через .gitignore), он не появится в списке отслеживаемых.



1. Просмотр привязанных удалённых репозиториев
bash
git remote -v
Эта команда покажет:

Имя удалённого репозитория (обычно origin)

URL для fetch (получения данных)

URL для push (отправки данных)

Пример вывода:

text
origin  https://github.com/your-username/your-repo.git (fetch)
origin  https://github.com/your-username/your-repo.git (push)
2. Если вывод пустой
Если команда git remote -v ничего не возвращает — проект не привязан к удалённому репозиторию.
Чтобы добавить привязку:

bash
git remote add origin https://github.com/your-username/your-repo.git
3. Дополнительные проверки
Убедитесь, что URL ведёт на GitHub
HTTPS-ссылка: https://github.com/...

SSH-ссылка: git@github.com:...

Проверьте ассоциацию с конкретным репозиторием
bash
git config --get remote.origin.url
Эта команда покажет только URL для origin.

4. Если настроено несколько удалённых репозиториев
bash
git remote show origin
Покажет:

URL репозитория

Список веток

Статус синхронизации с сервером

Как интерпретировать результаты
Ситуация	Что делать
URL содержит github.com	Проект привязан к GitHub
URL содержит другой домен (e.g., gitlab.com)	Проект привязан к другому сервису
Нет вывода	Привязка не настроена → используйте git remote add
URL неверный	Обновите его: git remote set-url origin новый-URL
Пример исправления URL
bash
git remote set-url origin https://github.com/new-username/new-repo.git




🚀 Базовая схема: main + develop
text
main     = продакшен (стабильная версия)
develop  = разработка (текущие изменения)
1. Создаем структуру веток
bash
# Переходим в папку проекта
cd ваш-проект

# Создаем ветку develop от main
git checkout main
git checkout -b develop
git push -u origin develop  # пушим ветку на сервер
2. Ежедневный рабочий процесс
bash
# Всегда начинаем с develop
git checkout develop
git pull origin develop

# Создаем новую feature-ветку
git checkout -b feature/new-payment

# Работаем, делаем коммиты...
git add .
git commit -m "Добавлена оплата через PayPal"

# Пушим ветку
git push -u origin feature/new-payment
3. Мерж изменений в develop
bash
# Возвращаемся в develop
git checkout develop
git pull origin develop

# Мержим фичу
git merge feature/new-payment

# Решаем конфликты (если есть), затем пушим
git push origin develop

# Удаляем feature-ветку (опционально)
git branch -d feature/new-payment
git push origin --delete feature/new-payment
4. Подготовка релиза на прод
bash
# Переключаемся на main
git checkout main
git pull origin main  # всегда обновляем!

# Мержим develop в main
git merge develop

# Создаем тег версии
git tag -a v1.2.0 -m "Релиз платежной системы"
git push origin --tags
5. Ручной деплой на продакшен
bash
# 1. Забираем код из main на продакшен-сервер
git fetch origin
git checkout main

# 2. Запускаем деплой-скрипт (пример)
./deploy-to-prod.sh

# ИЛИ для простых проектов - копируем файлы
rsync -avz . user@prod-server:/var/www/project
⚙️ Настройка защиты веток (рекомендуется)
В GitHub/GitLab:

Зайдите в Settings → Branches

Для main и develop установите:

Require pull request before merging

Require approvals (минимум 1)

Require status checks (если есть CI)

🔄 Workflow визуально
Diagram
Code







📌 Правила для команды
Никогда не пушить напрямую в main! Только через мерж из develop

Все изменения - через feature-ветки

Перед мержем в develop:

bash
git pull origin develop
run tests  # если есть тесты
Релизы делать по расписанию (например, каждую пятницу)

🛠️ Пример скрипта деплоя (deploy-to-prod.sh)
bash
#!/bin/bash

# 1. Переходим в папку проекта
cd /path/to/project

# 2. Обновляем код
git fetch origin
git checkout main
git reset --hard origin/main

# 3. Устанавливаем зависимости
npm install  # или pip install -r requirements.txt

# 4. Собираем проект (если нужно)
npm run build  # или make

# 5. Перезапускаем сервис
sudo systemctl restart my-service.service

# 6. Опционально: отправляем уведомление
curl -X POST -H 'Content-type: application/json' \
--data '{"text":"Релиз v1.2.0 успешно задеплоен!"}' \
https://hooks.slack.com/services/XXX/YYY/ZZZ
❓ Что делать при баге на проде?
bash
# 1. Создаем hotfix-ветку ОТ main
git checkout main
git checkout -b hotfix/login-issue

# 2. Фиксим баг, тестируем
git commit -m "Исправлена ошибка авторизации"

# 3. Мержим в main И в develop
git checkout main
git merge hotfix/login-issue
git tag -a v1.2.1 -m "Экстренный фикс авторизации"

git checkout develop
git merge hotfix/login-issue

# 4. Деплоим исправление
./deploy-to-prod.sh
💡 Советы для старта
Используйте понятные имена feature-веток: feature/, fix/, refactor/

Всегда пишите осмысленные сообщения коммитов

Перед мержем в develop:

bash
git rebase -i develop  # уплотните коммиты
Храните историю main в чистоте - только релизные коммиты

Эта схема - отличная база. Когда проект вырастет, вы сможете добавить:

CI/CD для автоматического тестирования и деплоя

Ветку release/ для подготовки к деплою

Докеризацию

Canary-деплои



Чтобы полностью заменить ваш текущий проект кодом из репозитория на GitHub (отменить все локальные изменения и вернуть "чистую" версию), выполните следующие команды:

🔥 Полный сброс до состояния удалённого репозитория
bash
# 1. Перейти в корень проекта
cd путь/к/проекту

# 2. Забрать последние изменения с удалённого сервера
git fetch --all

# 3. Сбросить ветку до состояния origin/main (или другой вашей основной ветки)
git reset --hard origin/main

# 4. Очистить неотслеживаемые файлы и директории (опционально, но рекомендуется)
git clean -fd
Пояснение команд:
git fetch --all
Скачивает все изменения со всех удалённых репозиториев, но не применяет их.

git reset --hard origin/main

--hard — полностью сбрасывает состояние до указанной версии

origin/main — ветка на удалённом сервере (замените main на вашу ветку, например master или develop)

git clean -fd

-f — принудительное удаление

-d — удаляет неотслеживаемые директории

Удалит все файлы/папки, которых нет в репозитории

🔄 Альтернативный способ (через пересоздание)
Если предыдущий метод не сработал или вы хотите гарантированно чистую копию:

bash
# 1. Перейти в родительскую директорию
cd ..

# 2. Удалить текущую папку проекта (осторожно!)
rm -rf ваш-проект  # для Linux/macOS
# или
# rd /s /q ваш-проект  # для Windows (в CMD)

# 3. Клонировать заново
git clone https://github.com/ваш-логин/ваш-репозиторий.git
⚠️ Важные предупреждения
Это необратимые действия!
Вы потеряете:

Все незакоммиченные изменения

Локальные файлы, не добавленные в Git

Локальные коммиты, не отправленные на сервер

Перед выполнением:

Убедитесь, что нужный код есть на GitHub

Если есть важные незакоммиченные изменения — сохраните их:

bash
git stash  # временное сохранение изменений
(позже можно восстановить через git stash pop)

🛡️ Что делать, если случайно сбросили нужные изменения?
Если вы всё же потеряли важные данные:

Для отслеживаемых файлов (были в коммитах):

bash
git reflog  # найти хеш последнего коммита
git reset --hard [хеш_коммита]
Для неотслеживаемых файлов:

Восстановите из резервной копии (если есть)

Используйте программы для восстановления файлов (например, Recuva для Windows)

💡 Как избежать проблем в будущем
Чаще коммитьте и пушите:

bash
git add .
git commit -m "WIP: текущие изменения"
git push origin feature/my-feature
Используйте ветки:

bash
git checkout -b experiment  # безопасное место для экспериментов
Настройте игнорирование ненужных файлов:
Создайте .gitignore в корне проекта:

text
# Пример содержимого
node_modules/
.env
*.log
Для частичного сброса:

bash
# Отменить изменения в конкретном файле:
git checkout -- путь/к/файлу

# Удалить все локальные изменения (но сохранить новые файлы):
git reset --hard
После сброса ваш проект будет в точности соответствовать последней версии в репозитории GitHub. Рекомендую использовать первый метод (reset --hard), так как он быстрее и сохраняет историю git.
