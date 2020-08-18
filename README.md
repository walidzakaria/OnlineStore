# OnlineStore
An online store application for selling different items.

## API Documentation
### Getting Started
- `Base URL:` The application is temporarily hosted on herokuapp in this link [https://mystore9.herokuapp.com](https://mystore9.herokuapp.com).
- `Authentication:` Some endpoints need authentication, and will be mentioned in details.

### Error Handling
All errors are handled based on `Django REST Framework`.

### Endpoints
#### POST /auth/users/
- General:
    - Signs up a new user account. It requires a unique username, phone, first name, last name, a unique email, and password retyped twice.
    - If signed up successfully, an activation email will be sent to the user.
- Sample:
```commandline
POST https://mystore9.herokuapp.com/auth/users/ 
```
body:
```json
{
    "username": "waliddeveloper",
    "phone": "01229277250",
    "first_name": "walid",
    "last_name": "zakaria",
    "email": "walidpianooo@gmail.com",
    "password": "password",
    "re_password": "password"
}
```
response:
```json
{
    "username": "waliddeveloper",
    "phone": "01229277250",
    "first_name": "walid",
    "last_name": "zakaria",
    "email": "walidpianooo@gmail.com",
    "id": 3
}
```

#### POST /auth/token/login
- General:
    - Login the valid user by email address and password.
    - If the user is valid, a token will be returned.
- Sample:
```commandline
POST https://mystore9.herokuapp.com/auth/token/login 
```
body:
```json
{
    "email": "walidpianooo@gmail.com",
    "password": "password"
}
```
response:
```json
{
    "auth_token": "c14f6f9b56a76222c947465dff1a8a9752abd16f"
}
```
#### GET /products/categories/{language}
- General:
    - Retrieves all main categories (id, English name, and Arabic name).
    - ar/en language parameters decides whether the categories are sorted based on the English name or the Arabic name.
- Sample:
```commandline
GET https://mystore9.herokuapp.com/products/categories/ar 
```
response:
```json
[
    {
        "id": 1,
        "name": "Accessories",
        "name_ar": ""
    },
    {
        "id": 2,
        "name": "Electronics",
        "name_ar": ""
    }
]
```
#### GET /products/subcategories/{language}
- General:
    - Retrieves all sub categories (id, category name, English name, Arabic name, category id).
    - ar/en language parameters decides whether the subcategories are sorted based on the English name or the Arabic name.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/subcategories/en 
```
response:
```json
[
    {
        "id": 1,
        "category_name": "Accessories",
        "name": "Errings",
        "name_ar": "",
        "category": 1
    },
    {
        "id": 2,
        "category_name": "Accessories",
        "name": "Rings",
        "name_ar": "",
        "category": 1
    }
]
```

#### GET /products/slider/{language}
- General:
    - Retrieves the products that are set by the admin to show on the slider.
    - ar/en language parameters are set for the product name and description.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/slider/en 
```
response:
```json
[
    {
        "id": 9,
        "brand_name": "Samsung",
        "sub_category": {
            "id": 5,
            "category_name": "Electronics",
            "name": "Mobiles",
            "name_ar": "",
            "category": 2
        },
        "product_name": "s20 ultra",
        "price1": "10.00",
        "price2": "9.00",
        "product_description": "",
        "image1": "/media/products/s11_ultra.jpg",
        "image2": null,
        "image3": null,
        "image4": null,
        "image5": null,
        "brand": 2
    }
]
```
#### GET /products/categories/{category_id}/{language}
- General:
    - Retrieves all the products that belong to the selected category id.
    - ar/en language parameters are set for the product name and description.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/categories/2/en 
```
response:
```json
[
    {
        "id": 4,
        "brand_name": "Xiaomi",
        "sub_category": {
            "id": 5,
            "category_name": "Electronics",
            "name": "Mobiles",
            "name_ar": "",
            "category": 2
        },
        "product_name": "Redmi note 9s",
        "price1": "90.00",
        "price2": "0.00",
        "product_description": "",
        "image1": "/media/products/note_9s.jpg",
        "image2": null,
        "image3": null,
        "image4": null,
        "image5": null,
        "brand": 5
    }
]
```
#### GET /products/subcategories/{subcategory_id}/{language}
- General:
    - Retrieves all the products that belong to the selected subcategory id.
    - ar/en language parameters are set for the product name and description.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/subcategories/5/en 
```
response:
```json
[
    {
        "id": 4,
        "brand_name": "Xiaomi",
        "sub_category": {
            "id": 5,
            "category_name": "Electronics",
            "name": "Mobiles",
            "name_ar": "",
            "category": 2
        },
        "product_name": "Redmi note 9s",
        "price1": "90.00",
        "price2": "0.00",
        "product_description": "",
        "image1": "/media/products/note_9s.jpg",
        "image2": null,
        "image3": null,
        "image4": null,
        "image5": null,
        "brand": 5
    }
]
```
#### GET /currencies/exchange/
- General:
    - Retrieves all currencies with the latest exchange rate based on the admin entry
- Sample:
```commandline
https://mystore9.herokuapp.com/currencies/exchange/ 
```
response:
```json
[
    {
        "id": 1,
        "currency": "Dollar",
        "currency_ar": "دولار",
        "code": "USD",
        "rate": "1.0000"
    },
    {
        "id": 3,
        "currency": "Euro",
        "currency_ar": "يورو",
        "code": "EUR",
        "rate": "1.2000"
    },
    {
        "id": 2,
        "currency": "Egyptian Pound",
        "currency_ar": "جنيه مصري",
        "code": "EGP",
        "rate": "16.3300"
    }
]
```

to be continued...