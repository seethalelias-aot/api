from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {"name": "my store", "items": [{"name": "abc", "price": "15"}]},
    {"name": "newstore", "items": [{"name": "abcf", "price": "15.1"}]},
]


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "not found"})


@app.route("/store")
def get_stores():
    return jsonify(stores)


@app.route("/store/<string:name>/items", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            # print(stores)
            return jsonify(new_item)
    return jsonify({"message": "not found"})


@app.route("/store/<string:name>/items")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "not found"})


app.run()
