import random

from flask_restful import Api, Resource, reqparse

from app import app, data

api = Api(app)


class Quote(Resource):

    @staticmethod
    def get(quote_id: int = 0):
        if quote_id == 0:
            return random.choice(data.QUOTES), 200
        for quote in data.QUOTES:
            if quote["quote_id"] == quote_id:
                return quote, 200
        return "Quote not found", 404

    @staticmethod
    def post(quote_id: int):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in data.QUOTES:
            if quote_id == quote["quote_id"]:
                return f"Quote with id {quote_id} already exists", 400
        quote = {
            "id": int(quote_id),
            "author": params["author"],
            "quote": params["quote"]
        }
        data.QUOTES.append(quote)
        return quote, 201

    @staticmethod
    def put(quote_id: int):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in data.QUOTES:
            if quote_id == quote["quote_id"]:
                quote["author"] = params["author"]
                quote["quote"] = params["quote"]
                return quote, 200

        quote = {
            "id": quote_id,
            "author": params["author"],
            "quote": params["quote"]
        }

        data.QUOTES.append(quote)
        return quote, 201

    @staticmethod
    def delete(quote_id: int):
        data.QUOTES = [quote for quote in data.QUOTES if quote["quote_id"] != quote_id]
        return f"Quote with id {quote_id} is deleted.", 200


api.add_resource(Quote, "/api/v1/quotes", "/api/v1/quotes/", "/api/v1/quotes/<int:quote_id>")

if __name__ == '__main__':
    app.run(debug=True)
