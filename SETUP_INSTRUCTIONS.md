# OctoFit Tracker App - Setup Instructions

Follow these step-by-step instructions to set up and run the OctoFit Tracker App.

## Step 1: Create Python Virtual Environment

Creating a virtual environment isolates project dependencies from your system Python installation.

### On macOS/Linux:

```bash
# Navigate to the project directory
cd skills-build-applications-w-copilot-agent-mode

# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# You should see (venv) at the beginning of your terminal prompt
```

### On Windows:

```bash
# Navigate to the project directory
cd skills-build-applications-w-copilot-agent-mode

# Create virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# You should see (venv) at the beginning of your terminal prompt
```

## Step 2: Create requirements.txt

The `requirements.txt` file has already been created with the following dependencies:

```
requests==2.31.0           # HTTP library for API calls
python-dotenv==1.0.0       # Environment variable management
pytest==7.4.3              # Testing framework
```

## Step 3: Install Python Requirements

With the virtual environment activated, install the dependencies:

```bash
pip install -r requirements.txt
```

You should see output like:
```
Collecting requests==2.31.0
Collecting python-dotenv==1.0.0
Collecting pytest==7.4.3
...
Successfully installed requests-2.31.0 python-dotenv-1.0.0 pytest-7.4.3
```

## Step 4: Verify Installation

Verify that all packages are installed correctly:

```bash
pip list
```

You should see the installed packages in the output.

## Step 5: Run the Application

Navigate to the project root and run the main application:

```bash
# Make sure you're in the project directory
# and the virtual environment is activated

python src/main.py
```

## Step 6: Run Tests (Optional)

To run the unit tests:

```bash
pytest tests/
```

Or run a specific test file:

```bash
pytest tests/test_joke_generator.py -v
```

## Project Structure

```
skills-build-applications-w-copilot-agent-mode/
├── venv/                          # Virtual environment (created locally)
├── src/
│   ├── __init__.py
│   ├── main.py                    # Main application entry point
│   ├── api_client.py              # Generic API client
│   ├── joke_generator.py          # Random joke generator
│   └── fitness_tracker.py         # Fitness tracking module
├── tests/
│   ├── __init__.py
│   └── test_joke_generator.py     # Unit tests
├── requirements.txt               # Project dependencies
├── .gitignore                     # Git ignore rules
├── README.md                      # Project overview
└── SETUP_INSTRUCTIONS.md          # This file
```

## Features

The OctoFit Tracker App includes:

1. **Random Joke Generator** - Fetches jokes from JokeAPI to keep you motivated
2. **Fitness Tracker** - Track your workouts and calories burned
3. **Interactive Menu** - User-friendly command-line interface
4. **API Integration** - Makes calls to external APIs (JokeAPI)
5. **Unit Tests** - Comprehensive test suite

## Troubleshooting

### Virtual environment not activating?
- Make sure you're in the project directory
- On Windows, try: `python -m venv venv` instead of `python3`

### pip install fails?
- Ensure the virtual environment is activated
- Try: `python -m pip install --upgrade pip`
- Then: `pip install -r requirements.txt`

### ModuleNotFoundError when running main.py?
- Make sure the virtual environment is activated
- Run from the project root directory
- Check that all files in src/ are present

## Next Steps

1. Explore the application by running `python src/main.py`
2. Try the joke generator features
3. Add fitness activities and track your progress
4. Review and run the unit tests
5. Extend the functionality with your own features

## Additional Resources

- [requests Library](https://requests.readthedocs.io/)
- [JokeAPI](https://jokeapi.dev/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [pytest Documentation](https://docs.pytest.org/)

---

Happy coding and stay fit! 🐙🏋️
