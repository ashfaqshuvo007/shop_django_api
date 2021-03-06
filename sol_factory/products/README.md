## Necessary APIs

### To get list of product categories:

**Sample URL:** `/products/categories/`

**Method:** GET

**Headers:** 
* Content-Type: application/json

**Sample Response:**
```json
[
    {
        "id": 1,
        "name": "Bearings",
        "tsync_id": "e6f1b037-b3be-4ccb-8003-455c3b867c2d",
        "parent": null,
        "description": ""
    },
    {
        "id": 2,
        "name": "Generators",
        "tsync_id": "0cb3efbe-7d5f-41c6-b721-85beb78ac998",
        "parent": null,
        "description": ""
    }
]
```
### To get list of products:

**Sample URL:** `/products/`

**Method:** GET

**Headers:** 
* Content-Type: application/json

**Sample Response:**
```json
[
    {
        "id": 1,
        "name": "Walton",
        "tsync_id": "f0e0a383-2bfc-4568-806a-224f2c06ee7c",
        "date_created": "2019-07-04T21:23:16.779079Z",
        "last_updated": "2019-07-04T21:52:19.489839Z",
        "description": "dsdsd dsd",
        "category": 2,
        "icons": [
            {
                "photo": "http://127.0.0.1:8000/products/static_media/uploads/2019/07/04/walton_AC_1.jpg",
                "photo_url": "static_media/uploads/2019/07/04/walton_AC_1.jpg",
                "order": 1
            },
            {
                "photo": "http://127.0.0.1:8000/products/static_media/uploads/2019/07/04/Screenshot_from_2019-07-05_02-46-16.png",
                "photo_url": "static_media/uploads/2019/07/04/Screenshot_from_2019-07-05_02-46-16.png",
                "order": 2
            }
        ]
    }
]
```
