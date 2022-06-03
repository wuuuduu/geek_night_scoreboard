```bash
cd backend
cp sample.env .env
...edit .env
```

```bash
pip install -r backend/requirements-dev.yml
pip install pre-commit && pre-commit install
docker-compose -f docker-compose.dev.yml up
cd backend 
cp sample.env .env
...edit .env
python3 manage.py runserver
```

```bash
# tests
python3 manage.py test --settings=config.settings.base
```