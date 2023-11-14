# General Scraper

An ambitious lieutenant scraper. Parameterised with env variables - for now.

## Installation

This project uses `pipenv` for handling package dependencies. To set up your development environment, follow the steps below:

### Prerequisites

Ensure you have `pipenv` installed. If you do not have `pipenv` installed, you can install it using `pip`:

```sh
pip install pipenv
```
For more information on using `pipenv`, you can refer to the [official documentation](https://pipenv.pypa.io/en/latest/)

### Setting Up the Development Environment

1. **Clone the repository:**

    ```sh
    git clone https://github.com/DeeprajPandey/lieutenant-scraper.git
    cd lieutenant-scraper
    ```

2. **Install dependencies:**

    Use `pipenv` to install the project dependencies from the `Pipfile`:

    ```sh
    pipenv install
    ```

    This will create a virtual environment and install the necessary packages.

3. **Activate the virtual environment:**

    ```sh
    pipenv shell
    ```

    This will spawn a new shell subprocess, which can be deactivated by simply closing it, or by running `exit`.

4. **Run the application:**

    With the virtual environment activated and config, you can now run the application:

    ```sh
    python main.py
    ```

### Using `pipenv` for Development

- To install a new package for your project:

    ```sh
    pipenv install package-name
    ```

- To install dev-packages (packages that are only needed for development, not in production):

    ```sh
    pipenv install package-name --dev
    ```

- To generate a `Pipfile.lock`, which should be committed:

    ```sh
    pipenv lock
    ```

## Todo

- [ ] Add `.env.example` and `config.yaml.example` to root and add edit instructions after activating virtual environemnt in installation instructions.
