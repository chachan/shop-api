# shop-api

Created using:

- [Vercel](https://vercel.com) to compile and serve Python Serverless Functions
- Python 3.6 as runtime
- Flask for easy requests handling
- MongoDB hosted on MongoDB Atlas service
- Visual Studio Code. Some extensions worth to mention: Code Time, GitHub Theme, GitLens, Indicator, markdownlint, Pylance, TODO Highlight
- [Postman](https://www.postman.com/)
- [Dash for macOS](https://kapeli.com/dash)
- macOS 10.14.6

## API Reference

### Get a list of items for sale

```bash
curl -X GET 'https://shop-api.chachan.vercel.app/api/items'
```

### List a new item up for sale

```bash
curl -X POST 'https://shop-api.chachan.vercel.app/api/items' \
--header 'Content-Type: application/json' \
--data-raw '{
    "items": [
        {
            "name": "Pillow",
            "price": 12.3
        }
    ]
}'
```

### Unlist an item for sale

```bash
curl -X DELETE 'https://shop-api.chachan.vercel.app/api/items' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item": {
        "name": "Pillow"
    }
}'
```

### Add an item to a shopping cart

```bash
curl -X POST 'https://shop-api.chachan.vercel.app/api/cart' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item": {
        "name": "Flour",
        "price": 12.3
    }
}'
```

### Remove an item from a shopping cart

```bash
curl --location --request DELETE 'https://shop-api.chachan.vercel.app/api/cart' \
--header 'Content-Type: application/json' \
--data-raw '{
    "item": {
        "name": "Flour"
    }
}'
```

### View a user's shopping cart

```bash
curl -X GET 'https://shop-api.chachan.vercel.app/api/cart'
```
