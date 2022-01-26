
  <h3 align="center">API TESTE</h3>

### Built With

* [DJANGO REST FRAMEWORK](https://www.django-rest-framework.org/)
* [DJANGO](https://docs.djangoproject.com/en/4.0/)
* [PYTHON](https://docs.python.org/3/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
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
2. start project and app
   ```sh
   django-admin startproject apiteste .
   python manage.py startapp employees
   ```
3. run migrates
   ```sh
   python manage.py migrate
   ```
   
4. create super user
   ```sh
   python manage.py createsuperuser
   ```
   set user, email and password


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


