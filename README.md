# symeo-cloud-function-example

## :construction: Installation

### Minimum requirements

- [Python](https://www.python.org/) 3.10

### Install the application locally

- Run `git clone git@github.com:symeo-io/symeo-cloud-function-example.git` or `https://github.com/symeo-io/symeo-cloud-function-example.git`
- Run `cd symeo-cloud-function-example` to navigate to the code folder
- Run `pip install -r requirements.txt` and `pip install -r requirements-dev.txt` to install project dependencies
- Run `pre-commit install` to set up the git hook scripts

## Goal of this Google Cloud Function

- Retrieving an object from an HTTP request which has this form:

```json
{
  "id": "id-example",
  "content": {
    "title": "title-example",
    "description": "description-example"
  }
}
```

- Writing the `content` of this object in a firestore database.

## :wrench: Development

### Coding conventions

The coding conventions and style are enforced by the [ruff](https://beta.ruff.rs/docs/) linter and the [black](https://github.com/psf/black) formatter.

To check linting error in command line, run `ruff check <target_directory>`. The configuration of ruff can be found in the [.ruff.toml](./.ruff.toml) file.

To fix automatically format errors, run `black <target_directory>`.

To check all coding conventions before committing to your remote repo we use [pre-commit](https://pre-commit.com/) hooks. If you didn't already run `pre-commit install` right after cloning the repo, you should do it now.

## :office: Architectures

### Structure

The source code is contained in the `/src` directory:

```text
src
├── application
│   └── cloud_function_adapter
│       ├── __init__.py
│       ├── adapter
│       │   └── __init__.py
│       │   └── cloud_function_adapter.py
│       ├── dto
│       │   ├── __init__.py
│       │   └── clound_function_dto.py
│       └── mapper
│           ├── __init__.py
│           └── cloud_function_mapper.py
├── bootstrap
│   ├── __init__.py
│   └── main.py
├── domain
│   ├── __init__.py
│   ├── model
│   │   ├── __init__.py
│   │   └── cloud_function_model.py
│   ├── port_in
│   │   ├── __init__.py
│   │   └── storage_facade.py
│   ├── port_out
│   │   ├── __init__.py
│   │   └── storage_port.py
│   └── service
│       ├── __init__.py
│       └── storage_service.py
└── infrastructure
    ├── __init__.py
    └── firestore_storage_adapter
        ├── __init__.py
        └── adapter
            ├── __init__.py
            └── firestore_storage_adapter.py
```

The structure of this project follows **Hexagonal-Architecture** and **Domain-Driven-Design** principles and is seperated into 4 main folders:
1. `/application`: it will contain adapters related to your "application". For now, you will only find one application adapter (`cloud_function_adapter`) containing
the process method (`/application/cloud_function_adapter/adapter/cloud_function_adapter.py`) as well as the DTOs of this endpoint (`/application/cloud_function_adapter/dto`).
2. `/domain`: this is where all the business logic has to be. You will find the `models`, the different ports `/domain/port/in` and `/domain/port/out` on which you will plug your adapters and finally your `services`.
3. `/infrastructure`: this is where all your adapters related to your infrastructure should be. For now, you will only find one adapter which is a `firestore_storage_adapter`.
4. `/bootstrap`: this is where you will bootstrap your project by making [dependency injections](#entrypoint-and-dependency-injection).

### Framework

The framework used for this project is Flask.

Data validation is made thanks to Pydantic.

#### Official documentations

- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Pydantic](https://docs.pydantic.dev/latest/)

## :rocket: Infrastructure

### Entrypoint and Dependency Injection

The entrypoint of your application is the `main.py` file located at `/src/bootstrap/main.py`. Our bootstrap method looks like this:

```python
def cloud_function(request: flask.Request) -> flask.Response:
    key_filename = "key_filename"
    firestore_storage_adapter: FirestoreStorageAdapter = FirestoreStorageAdapter(key_filename)
    storage_service: StorageService = StorageService(firestore_storage_adapter)
    cloud_function_adapter: CloudFunctionAdapter = CloudFunctionAdapter(storage_service)
    return cloud_function_adapter.process(request)
```

We can see that this is where we achieve **dependency injections**.

## :white_check_mark: Testing strategy

The tests are carried out using the [pytest](https://docs.pytest.org/en/7.3.x/) library.

Faker values are generated with the [faker](https://faker.readthedocs.io/en/master/) library.

### Commands

- Use `pytest` to launch all tests.
- Use `coverage run -m pytest tests` to launch all tests and get coverage report.
- Use `coverage report` to display your coverage report

#### Unit Tests

You will find an example of unit tests in `/tests/unit/domain/service` used to test the behavior of the example service [storage_service.py](./src/domain/service/storage_service.py).

In those tests, we do not reach external dependencies. Therefore, we must (when we have to) mock things like database access, external api access, etc...
