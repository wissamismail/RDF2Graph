# RDF2Graph

**RDF2Graph** is a Python-based tool developed by **Wissam Ismail**. Based on the repository's file structure and naming, the project appears designed to **process RDF (Resource Description Framework) triples and convert them into graph-based representations**.

## Features
*   **Pure Python Implementation:** The project is written entirely in **Python (100%)**.
*   **RDF Triple Handling:** Includes a dedicated module (`Triples.py`) for managing or parsing RDF data.
*   **Graph Construction:** Features logic for building or manipulating graph structures (`Graph.py`).
*   **Web Automation Integration:** Utilizes **Selenium** (`seleniumFunctions.py`), which suggests the tool may scrape RDF data from the web or interact with web-based graph interfaces.

## Repository Structure
The project includes the following core files:
*   **`main.py`**: The main execution script for the application.
*   **`Graph.py`**: Contains the logic for graph generation and management.
*   **`Triples.py`**: Handles the processing of RDF triples.
*   **`seleniumFunctions.py`**: Provides automated web interaction capabilities via Selenium.
*   **`requirements.txt`**: Specifies the necessary Python packages and dependencies.

## Getting Started

### Prerequisites
*   **Python 3.x**
*   Specific dependencies listed in `requirements.txt`

### Installation
1.  **Clone the repository** to your local machine.
2.  **Install the required dependencies** using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
To run the application, execute the **`main.py`** file:
```bash
python main.py
```

## Contributors
*   **Wissam Ismail**
