# 🐙 OctoFit Tracker App

A fitness tracking application with an integrated random joke generator to keep you motivated during your workouts!

## Features

✨ **Random Joke Generator**
- Fetch random jokes from [JokeAPI](https://jokeapi.dev/)
- Support for different joke categories
- Get programming jokes for motivation
- Single-line and multi-part joke support

🏋️ **Fitness Activity Tracker**
- Log your fitness activities (running, yoga, weightlifting, etc.)
- Automatic calorie calculation based on activity type
- Track activity duration and calories burned
- View comprehensive fitness statistics
- Filter activities by type

🎮 **Interactive Menu**
- User-friendly command-line interface
- Easy navigation between features
- Real-time activity logging

## Project Structure

```
skills-build-applications-w-copilot-agent-mode/
├── src/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main application entry point
│   ├── api_client.py            # Generic API client with retry logic
│   ├── joke_generator.py        # Joke generator using JokeAPI
│   └── fitness_tracker.py       # Fitness tracking module
├── tests/
│   ├── __init__.py
│   └── test_joke_generator.py   # Unit tests
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── README.md                    # Project overview
└── SETUP_INSTRUCTIONS.md        # Detailed setup guide
```

## Installation & Setup

Follow the comprehensive setup instructions in [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md).

Quick start:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python src/main.py
```

## Usage

Run the main application:

```bash
python src/main.py
```

The interactive menu allows you to:
1. **Get a random joke** - Fetch a joke from JokeAPI
2. **Get a programming joke** - Get tech-related jokes for motivation
3. **Add a fitness activity** - Log your workouts
4. **View fitness statistics** - See your progress
5. **View all activities** - List all recorded activities
6. **Exit** - Close the application

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run a specific test file
pytest tests/test_joke_generator.py

# Run with coverage
pytest tests/ --cov=src
```

## API Integration

### JokeAPI
- **Base URL**: https://v2.jokeapi.dev
- **Endpoint**: `/joke/{category}`
- **Features**: Single & two-part jokes, multiple categories
- **Documentation**: [JokeAPI Docs](https://jokeapi.dev/)

## Dependencies

- **requests** (2.31.0) - HTTP library for API calls
- **python-dotenv** (1.0.0) - Environment variable management
- **pytest** (7.4.3) - Testing framework

## Features In Detail

### Joke Generator (`src/joke_generator.py`)
- Fetches jokes from JokeAPI
- Retry logic for failed requests
- Pretty-printed joke output
- Support for different joke types

### Fitness Tracker (`src/fitness_tracker.py`)
- Log activities with automatic calorie calculation
- Built-in calorie rates for common activities:
  - Running: 12 cal/min
  - Walking: 4 cal/min
  - Weightlifting: 8 cal/min
  - Yoga: 4 cal/min
  - Cycling: 10 cal/min
  - Swimming: 11 cal/min
  - Cardio: 9 cal/min
- Statistical analysis of activities
- Activity filtering and search

### API Client (`src/api_client.py`)
- Generic HTTP client
- Automatic retry with exponential backoff
- Configurable timeout and retry attempts
- Support for GET and POST requests

## Example Output

```
🐙 OCTOFIT TRACKER APP
==================================================
1. Get a random joke
2. Get a programming joke
3. Add a fitness activity
4. View fitness statistics
5. View all activities
6. Exit
==================================================

😄 Why do Java developers wear glasses?
Because they can't C#

==================================================
🏋️  FITNESS STATISTICS
==================================================
Total Activities: 5
Total Duration: 180 minutes
Total Calories Burned: 1850 cal
Average per Activity: 370 cal, 36 min
==================================================
```

## Development

### Adding New Features
1. Create new modules in the `src/` directory
2. Add corresponding tests in the `tests/` directory
3. Update `requirements.txt` if adding new dependencies
4. Follow the existing code style and documentation patterns

### Code Style
- PEP 8 compliant
- Type hints for all functions
- Comprehensive docstrings
- Clear variable and function names

## Future Enhancements

- 💾 Database integration for persistent storage
- 📊 Data visualization and charts
- 🎯 Fitness goals and progress tracking
- 📱 Mobile app version
- 🌐 Web interface
- 🔔 Workout reminders and notifications
- 🏆 Leaderboards and challenges

## Troubleshooting

See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) for common setup issues and solutions.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

## License

This project is part of the GitHub Skills exercise for building applications with Copilot Agent Mode.

## Resources

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [JokeAPI Documentation](https://jokeapi.dev/)
- [requests Library](https://requests.readthedocs.io/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Copilot](https://github.com/features/copilot)

## Contact

Created by @ArnaudFOFOU237

---

**Happy coding and stay fit!** 🐙🏋️💪
