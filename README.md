# KPAY Merchant Multitenant

## Documentation

## virtual env

### Windows

```shell
  python -m venv venv
  python/Scripts/active
```

### MacOs

```shell
  python -m venv venv
  python/Scripts/active
```

## Installation

Install kpay-merchant-multitenant with pip

```shell
  pip install -r requirements
  cd kpay-merchant-multitenant
```

## Migration commands

```shell
    python manage.makemigrations
    python manage.py migrate
```

## Project setup

### .env file

```dotenv
SECRET_KEY=''
DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
DB_NAME=
REDIS_URL=
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Appendix

Any additional information goes here

