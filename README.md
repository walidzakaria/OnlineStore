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

#### POST /auth/token/logout
- General:
    - Logout the valid user by destroying the valid token.
    
- Sample:
```commandline
POST https://mystore9.herokuapp.com/auth/token/logout 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
response has no content with status 204.


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

#### GET /products/slider/{lang}
- General:
    - Retrieves the sliders that are set by the admin to show on the slider.
    - Each slider contains a link which could lead to anywhere in the app.
    - lang parameters filters only the sliders that are assigned against a certain language.
    - Sliders set with lang="both" shows in both languages. 
- Sample:
```commandline
https://mystore9.herokuapp.com/products/slider/en 
```
response:
```json
[
    {
        "name": "eid festival",
        "image": "image/upload/v1598224440/z69jic0x7krl15lntekr.jpg",
        "link": "http://127.0.0.1:8000/admin/products/slider/add/"
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


#### GET /products/new-arrival/{currency_id}/{language}
- General:
    - Retrieves all the products ordered recent purchases.
    - Products retrieved are only the ones that still in the stock.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
    - Retrieved data is paginated.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/new-arrival/1/en 
```
response:
```json
{
    "count": 9,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 10,
            "brand_name": "Adidas",
            "sub_category": {
                "id": 8,
                "category_name": "Accessories",
                "name": "watch",
                "name_ar": "ساعات",
                "category": 1
            },
            "product_name": "District L1",
            "price1": 50.0,
            "price2": 0.0,
            "delivery_days": 1,
            "product_description": "",
            "image1": "image/upload/v1598131549/gqp6gdinsy9wfr4pdqz4.jpg",
            "image2": null,
            "image3": null,
            "image4": null,
            "image5": null,
            "brand": 6
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

#### GET /products/auto-suggestion/{word-pattern}/
- General:
    - Retrieves 10 suggestions containing the word pattern.
    - word-pattern is included with <b></b> tags.
 
- Sample:
```commandline
https://mystore9.herokuapp.com/products/auto-suggestion/tes/ 
```
response:
```json
[
    "<b>tes</b>t product",
    "<b>tes</b>t"
]
```

#### GET /products/{product_id}/{currency_id}/{lang}
- General:
    - Retrieves a selected product details.
    - currency_id parameter defines the exchanged product price.
    - ar/en language parameters are set for the product name and description.
- Sample:
```commandline
https://mystore9.herokuapp.com/products/10/1/en/ 
```
response:
```json
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
```

#### GET /orders/shipping/{currency_id}/{lang}
- General:
    - Retrieves shipping cities with shipping fees.
    - currency_id parameter defines the exchanged shipping rate.
    - ar/en language parameters are set for the city name and sorting.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/shipping/2/ar 
```
response:
```json
[
    {
        "id": 1,
        "city_name": "الغردقة",
        "fees": 375.0
    },
    {
        "id": 2,
        "city_name": "القاهرة",
        "fees": 660.0
    }
]
```
#### GET /orders/shipping/{currency_id}/{shipping_id}/{lang}
- General:
    - Retrieves a single shipping city with shipping fees based on id.
    - currency_id parameter defines the exchanged shipping rate.
    - ar/en language parameters are set for the city name and sorting.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/shipping/2/2/ar 
```
response:
```json
{
    "id": 2,
    "city_name": "القاهرة",
    "fees": 660.0
}
```
#### GET /orders/user-addresses/
- General:
    - Requires authentication.
    - Retrieves a logged user shipping addresses.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-addresses/ 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
response:
```json
[
    {
        "id": 1,
        "address": "this place",
        "user": 1,
        "city": 1
    },
    {
        "id": 6,
        "address": "cairo - in this place.",
        "user": 1,
        "city": 1
    }
]
```
#### POST /orders/user-addresses/
- General:
    - Requires authentication.
    - Creates a new shipping address against the logged user.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-addresses/ 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
body:
```json
{
    "address": "new address",
    "city": 1
}
```
response:
```json
{
    "id": 9,
    "address": "new address",
    "user": 1,
    "city": 1
}
```
#### PUT /orders/user-addresses/{address_id}
- General:
    - Requires authentication.
    - Updates a shipping address against the logged user and address_id
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-addresses/7 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
body:
```json
{
    "address": "new address updates",
    "city": 2
}
```
response:
```json
{
    "id": 7,
    "address": "new address updates",
    "user": 1,
    "city": 2
}
```
#### DELETE /orders/user-addresses/{address_id}
- General:
    - Requires authentication.
    - Deletes a shipping address against the logged user and address_id
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-addresses/7 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```

response:
```json
{
    "message": "deleted"
}
```
#### GET orders/user-orders/
- General:
    - Requires authentication.
    - Retrieves all user previous order headers & count.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-orders/ 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```

response:
```json
{
    "count": 4,
    "data": [
        {
            "id": 10049,
            "currency_code": "EGP",
            "user_city": "Hurghada",
            "user_address": "this place",
            "due_days": 1,
            "created_at": "2020-09-01T20:37:13.235039Z",
            "updated_at": "2020-09-01T20:37:13.651690Z",
            "status": "Preparation",
            "notes": "some notes",
            "number_of_items": 5,
            "shipping_fees": "25.00",
            "total": "5648.00",
            "due_amount": "5673.00",
            "exchange_rate": "15.0000",
            "exchanged_due_amount": "85095.00",
            "due_date": "2020-09-02",
            "created_by": 1,
            "updated_by": 1,
            "client": 1,
            "currency": 2
        }
    ]
}
```
#### POST /orders/user-order-create/
- General:
    - Requires authentication.
    - Creates a new order against the logged user.
    - Prices & exchange rates are internally retrieved from server side.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-order-create/ 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
body:
```json
[
    {
        "notes": "some notes",
        "user_address": 1,
        "currency": 2
    },
    [
         {
             "product": 1,
             "quantity": 2
         },
         {
             "product": 2,
             "quantity": 3              
          }
    ]
]
```
response:
```json
{
    "id": 10051,
    "created_at": "2020-09-01T23:12:43.857815Z",
    "updated_at": "2020-09-01T23:12:44.271559Z",
    "status": "Preparation",
    "notes": "some notes",
    "number_of_items": 5,
    "shipping_fees": "44.00",
    "total": "5648.00",
    "due_amount": "5692.00",
    "exchange_rate": "15.0000",
    "exchanged_due_amount": "85380.00",
    "due_date": "2020-09-02",
    "created_by": 27,
    "updated_by": 27,
    "client": 27,
    "user_address": 7,
    "currency": 2
}
```
#### GET orders/user-orders/{order_id}/lang
- General:
    - Requires authentication.
    - Retrieved an order with detailed products against the logged user and order id.
    - Products show according to the lang in parameters.
- Sample:
```commandline
https://mystore9.herokuapp.com/orders/user-orders/10050/en 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
response:
```json
{
    "order_header": {
        "id": 10050,
        "currency_code": "USD",
        "user_city": "Hurghada",
        "user_address": "this place",
        "due_days": 1,
        "created_at": "2020-09-01T20:39:09.702733Z",
        "updated_at": "2020-09-01T20:39:10.062512Z",
        "status": "Preparation",
        "notes": "some notes",
        "number_of_items": 5,
        "shipping_fees": "25.00",
        "total": "5648.00",
        "due_amount": "5673.00",
        "exchange_rate": "1.0000",
        "exchanged_due_amount": "5673.00",
        "due_date": "2020-09-02",
        "created_by": 1,
        "updated_by": 1,
        "client": 1,
        "currency": 1
    },
    "order_items": [
        {
            "id": 54,
            "product": {
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
                "delivery_days": 1,
                "product_description": "this is description",
                "image1": null,
                "image2": null,
                "image3": null,
                "image4": null,
                "image5": null,
                "brand": 1
            },
            "quantity": 2,
            "product_value": "20.00",
            "order": 10050
        }
    ]
}
```

#### GET /auth/current-user/
- General:
    - Requires authentication.
    - Retrieved logged user information.
- Sample:
```commandline
https://mystore9.herokuapp.com/auth/current-user/ 
```
header:
```json
{
  "Authorization": "Token ?????????????????????"
}
```
response:
```json
{
    "id": 1,
    "email": "walidpiano@yahoo.com",
    "username": "admin",
    "first_name": "Walid",
    "last_name": "Hanna",
    "phone": "01229277250"
}
```

to be continued...