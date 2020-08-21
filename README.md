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

#### GET /products/slider/{currency_id}/{language}
- General:
    - Retrieves the products that are set by the admin to show on the slider.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/slider/1/en 
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
#### GET /products/categories/{category_id}/{currency_id}/{language}
- General:
    - Retrieves all the products that belong to the selected category id.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
    - Retrieved data is paginated.
    
- Sample:
```commandline
https://mystore9.herokuapp.com/products/categories/1/1/en 
```
response:
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "brand_name": "Infinix",
            "sub_category": {
                "id": 1,
                "category_name": "Electronics",
                "name": "Mobiles",
                "name_ar": "aaaa",
                "category": 1
            },
            "product_name": "test",
            "price1": 200.0,
            "price2": 0.0,
            "product_description": "some details here to check if they appear or not.",
            "image1": "image/upload/products/فؤاد_المهندس.jpg",
            "image2": "image/upload/products/James_Breasted_2.jpg",
            "image3": "image/upload/products/الأديب_يوسف_السباعي_82dxQfh.jpg",
            "image4": "image/upload/products/Fouad_el-Mohandes.jpg",
            "image5": "image/upload/products/test_image_9RPyJN1.jpg",
            "brand": 1
        }
    ]
}
```
#### GET /products/subcategories/{subcategory_id}/{currency_id}/{language}
- General:
    - Retrieves all the products that belong to the selected subcategory id.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
    - Retrieved data is paginated.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/subcategories/1/1/en 
```
response:
```json
{
    "count": 4,
    "next": "http://127.0.0.1:8000/products/subcategories/1/1/en?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "brand_name": "Infinix",
            "sub_category": {
                "id": 1,
                "category_name": "Electronics",
                "name": "Mobiles",
                "name_ar": "aaaa",
                "category": 1
            },
            "product_name": "test",
            "price1": 200.0,
            "price2": 0.0,
            "product_description": "some details here to check if they appear or not.",
            "image1": "image/upload/products/فؤاد_المهندس.jpg",
            "image2": "image/upload/products/James_Breasted_2.jpg",
            "image3": "image/upload/products/الأديب_يوسف_السباعي_82dxQfh.jpg",
            "image4": "image/upload/products/Fouad_el-Mohandes.jpg",
            "image5": "image/upload/products/test_image_9RPyJN1.jpg",
            "brand": 1
        }
    ]
}
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

#### GET /products/trending/{currency_id}/{language}
- General:
    - Retrieves all the products ordered by sold quantities.
    - Products retrieved are only the ones that still in the stock.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
    - Retrieved data is paginated.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/trending/1/en 
```
response:
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "brand_name": "Infinix",
            "sub_category": {
                "id": 1,
                "category_name": "Electronics",
                "name": "Mobiles",
                "name_ar": "aaaa",
                "category": 1
            },
            "product_name": "",
            "price1": 10.0,
            "price2": 20.0,
            "product_description": "",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "brand": 1
        }
    ]
}
```

#### GET /products/best-selling/{currency_id}/{language}
- General:
    - Retrieves all the products ordered reductions.
    - Products retrieved are only the ones that still in the stock.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
    - Retrieved data is paginated.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/best-selling/1/en 
```
response:
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "brand_name": "Infinix",
            "sub_category": {
                "id": 1,
                "category_name": "Electronics",
                "name": "Mobiles",
                "name_ar": "aaaa",
                "category": 1
            },
            "product_name": "test product",
            "price1": 10.0,
            "price2": 20.0,
            "product_description": "this is description",
            "image1": null,
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "brand": 1
        }
    ]
}
```

#### GET /products/search/{currency_id}/{lang}/?search={search_pattern}
- General:
    - Retrieves all the products matching the search parameters.
    - Filtered fields are ('name', 'name_ar', 'keywords', 'brand name', 'brand name_ar', 'sub_category name', 'sub_category name_ar', 'category name', 'category_name_ar', 'description').
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
    - Retrieved data is paginated.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/search/1/en/?search=test 
```
response:
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "brand_name": "Infinix",
            "sub_category": {
                "id": 1,
                "category_name": "Electronics",
                "name": "Mobiles",
                "name_ar": "aaaa",
                "category": 1
            },
            "product_name": "test",
            "price1": 200.0,
            "price2": 0.0,
            "product_description": "some details here to check if they appear or not.",
            "image1": "image/upload/products/فؤاد_المهندس.jpg",
            "image2": "image/upload/products/James_Breasted_2.jpg",
            "image3": "image/upload/products/الأديب_يوسف_السباعي_82dxQfh.jpg",
            "image4": "image/upload/products/Fouad_el-Mohandes.jpg",
            "image5": "image/upload/products/test_image_9RPyJN1.jpg",
            "brand": 1
        }
  ]
}
```

to be continued...