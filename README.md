# Netcare Access Team 1
## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

Before you begin, ensure that you have the following installed:

- **Python**: Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer, which typically comes pre-installed with Python. You can verify by running `pip --version`.

### Installation

#### 1. Clone the repository

First, clone the repository to your local machine using the following command:

```
$ git clone https://github.com/cc459/Predictive-Analysis.git
```

#### 2. Navigate into the project directory
```
$ cd Team-1
```

#### 3. Create a virtual environment
For Mac/Linux:
```
$ python3 -m venv venv
```

For Windows:
```
$ python -m venv venv
```

#### 4. Activate the virtual environment
For Mac/Linux:
```
$ source venv/bin/activate
```

For Windows:
```
$ venv\Scripts\activate
```

If the activation is successful, you should see `(venv)` at the start of your terminal prompt.

#### 5. Install the required packages
With the virtual environment active, install all necessary dependencies:
```
$ pip install -r requirements.txt
```

#### Notes
Once you're done working, you can deactivate the virtual environment by running
```
$ deactivate
```

If you add new packages during development, please update the `requirements.txt` file:
```
$ pip freeze > requirements.txt
```
This ensures that anyone else working on the project will have access to the updated dependencies.






