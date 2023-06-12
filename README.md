# Trakzee

## About

Simple web app for tracking your habits. Main purpose is to learn and practice fullstack web development 

## Commands

### App commands

**Update containers**
- docker compose up -d --build

**View Flask logs**
- `docker compose logs api`

**Lint code**
- `docker compose exec api flake8 src`

**Format code**
- `docker compose exec api black src --check --line-length 119`
- `docker compose exec api black src --line-length 119`

**Organize imports**
- `docker-compose exec api isort src --check-only`
- `docker-compose exec api isort src`

### Db commands

**Reset database**
- `docker compose exec api python src/main.py recreate_db`

**Seed database**
- `docker compose exec api python src/main.py seed_db`

**Create initial migration folder**
- `docker compose exec api python src/main.py db init`

**Create new migration**
- `docker compose exec api python src/main.py db migrate -m "Migration name"`

**Apply migration**
- `docker compose exec api python src/main.py db upgrade`

### Pytest commands

**normal run**
- `docker-compose exec api python -m pytest "src/tests"`

**disable warnings**
- `docker-compose exec api python -m pytest "src/tests" -p no:warnings`

**run only the last failed tests**
- `docker-compose exec api python -m pytest "src/tests" --lf`

**run only the tests with names that match the string expression**
- `docker-compose exec api python -m pytest "src/tests" -k "config and not test_development_config"`

**stop the test session after the first failure**
- `docker-compose exec api python -m pytest "src/tests" -x`

**enter PDB after first failure then end the test session**
- `docker-compose exec api python -m pytest "src/tests" -x --pdb`

**stop the test run after two failures**
- `docker-compose exec api python -m pytest "src/tests" --maxfail=2`

**show local variables in tracebacks**
- `docker-compose exec api python -m pytest "src/tests" -l`

**list the 2 slowest tests**
- `docker-compose exec api python -m pytest "src/tests" --durations=2`