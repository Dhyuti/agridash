# AGRIDASH

Built with Django, this website displays farmed items from the college’s agricultural department using RESTful APIs.

## Usage

Follow these steps to set up the Dashboard on your local environment:

1. Clone the repository:

   ```
   git clone https://github.com/Dhyuti/agridash.git
   cd agridash
   ```
2. Create a virtual environment and activate it:

   ```
   pipenv shell
   ```
3. Installing dependencies:

   ```
   pipenv install
   ```

 4. Migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

 5. To run dev server run this command

    ```
    python manage.py runserver
    ```
