# WControl

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL database
- Required Python packages: `psycopg2`, `click`, `python-dotenv`
- Environment variables: `USER`, `PASSWORD`, `DATABASE`, `HOST`, `PORT`

### Installation

1. Clone the repository or download the source code.
2. Install the required Python packages using pip:

   ```bash
   pip install psycopg2-binary click python-dotenv
   ```

3. Set up your environment variables (`USER`, `PASSWORD`, `DATABASE`, `HOST`, `PORT`) as per your PostgreSQL configuration.

## Usage

Run the application from the command line. Here are some basic commands:

- List items from the register:

  ```bash
  python app.py list
  ```

- Insert a new item into the register:

  ```bash
  python app.py insert <value> "<description>"
  ```

- Delete an item from the register by ID:

  ```bash
  python app.py delete <id>
  ```

- Clear all items from the register:

  ```bash
  python app.py clear
  ```

- Update the weekly budget value:

  ```bash
  python app.py week <new_weekly_budget>
  ```

- Check the current spend and remaining budget:

  ```bash
  python app.py check
  ```

Replace `<value>`, `<description>`, and `<id>` with actual values as needed.

## Contributing

Contributions are welcome Please feel free to submit a pull request.
