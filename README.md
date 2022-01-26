
  <h3 align="center">API TESTE</h3>

### Built With

* [DJANGO REST FRAMEWORK](https://www.django-rest-framework.org/)
* [DJANGO](https://docs.djangoproject.com/en/4.0/)
* [PYTHON](https://docs.python.org/3/)



<!-- GETTING STARTED -->
## Getting Started

This is a employee api

### Prerequisites

Install requirements
* Django
  ```sh
  pip install django
  ```
* Django rest framework
  ```sh
  pip install djangorestframework
  ```
  
### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:JPAkira/API-Test.git
   ```
   
2. run migrates
   ```sh
   python manage.py migrate
   ```
   
3. create super user
   ```sh
   python manage.py createsuperuser
   ```
   set user, email and password
   
4. Run server
   ```sh
   python manage.py runserver
   ```

5. API URL
   ```sh
   curl -H "Content-Type: application/javascript" http://localhost:8000/employees/api/employee/
   ```

6. Admin Site
   ```sh
   http://localhost:8000/admin
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


