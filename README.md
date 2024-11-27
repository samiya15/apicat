# apicat
to create a virtual environment we use the code 
    python -m venv .venv
we then activate the virtual environment
    .\.venv\Scripts\Activate.ps1
afterwards we install django
     pip install django
once django is installed we start the ecommerce project
    django-admin startproject ecommerce
in the ecommerce folder we start the models for customer and order as required in the question
    django-admin startapp customer
      django-admin startapp order
we can then run the surver to ensure proper installation of django
