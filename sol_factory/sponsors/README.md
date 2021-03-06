## Necessary APIs

### To get list of product categories:

**Sample URL:** `/sponsors/featured-categories/`

**Method:** GET

**Headers:** 
* Content-Type: application/json

**Sample Response:**
```json
[
    {
        "id": 1,
        "tsync_id": "e6f1b037-b3be-4ccb-8003-455c3b867c2d",
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
        ],
        is_master: false, // True for The main big feature box
        is_publish: true, // True for showing in home page
    },
]
```