## Setting up the project

* Preferred Python version: 3.7.3
* Please clone the repository. Then run ```pip install -r plugins.txt```
* Copy ```configs/database.py.example``` to ```configs/database.py```. Make necessary changes to this file based on your database configuration.
* Run both ```python manage.py makemigrations``` and ```python manage.py migrate```
* To create super-admin, run ```python manage.py create_admin```. Super admin username: `sfadmin` and password: `SFadmin123#`
* To create random product categories, run ```python manage.py prepare_random_product_categories```
* To create country-list, run ```python manage.py create_countries```

### For user registration flow, verification and login mechanism, please [see this file](sol_factory/users/README.md)

### For product, product category implementation, please [see this file](sol_factory/products/README.md)

### For chat implementation, please [see this file](sol_factory/chats/README.md)