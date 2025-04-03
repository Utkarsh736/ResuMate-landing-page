# ResuMate Landing Page

ResuMate is an AI-powered job search companion designed to help users streamline their job search process. This repository contains the landing page for ResuMate, built with [FastHTML](https://github.com/AnswerDotAI/fasthtml) by Answer.ai. The landing page showcases ResuMate’s features, includes a subscription form, and provides a call-to-action to start using the app.

## Features

- **Hero Section**: Introduces ResuMate with a tagline and description.
- **Key Features List**: Highlights AI-driven resume optimization, job recommendations, interview prep, and career guidance.
- **Subscription Form**: Allows users to subscribe for updates with dynamic feedback via HTMX.
- **Styled Design**: Uses Pico CSS (bundled with FastHTML) with custom colors and spacing for a clean, modern look.

## Tech Stack

- **FastHTML**: A Python-based framework for building server-rendered hypermedia applications.
- **Pico CSS**: Minimal CSS framework for styling, included with FastHTML.
- **HTMX**: For dynamic, client-side interactions without full page reloads.
- **uv**: A fast Python package manager by Astral for dependency management.

## Prerequisites

- **Python**: Version 3.11 or higher (specified in `pyproject.toml`).
- **uv**: Installed as the package manager (see [installation instructions](https://github.com/astral-sh/uv#installation)).

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/resumate-landing-page.git
   cd resumate-landing-page
    ```
2. Install uv (if not already installed):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
3. Sync Dependencies:
    ```bash
    uv sync
    ```
    This command will create a virtual environment and install the required dependencies specified in `pyproject.toml`.

4. Run the Application:
    ```bash
    uv run python app.py
    ```
    This will start the FastHTML server, and you should see output indicating that the app is running.

## Usage
- Open your browser and navigate to http://localhost:5000.
- Explore the landing page:
- Read about ResuMate’s features.
- Enter an email in the subscription form and click "Subscribe" to see a dynamic success message.
- Click "Start Your Journey" (currently a placeholder link to /signup).

## Project Structure
```plaintext
resumate-landing-page/
├── .gitignore         # Ignores .venv, __pycache__, .sesskey, etc.
├── pyproject.toml     # Project metadata and dependencies
├── app.py            # FastHTML app code for the landing page
└── README.md         # This file
```

## Customization
- Styling: Edit the Style tag in app.py to adjust colors, spacing, or other CSS properties.
- Content: Modify the text in app.py (e.g., H2, P, Li) to update the landing page content.
- Dependencies: Add packages to pyproject.toml under [project.dependencies] and run uv sync.

## Contributing
Feel free to fork this repository, submit issues, or open pull requests to enhance the landing page!

## License
This project is open-source and available under the . (Add a LICENSE file if desired.)

## Acknowledgments
Built with FastHTML by Answer.ai.
Powered by uv for fast dependency management.