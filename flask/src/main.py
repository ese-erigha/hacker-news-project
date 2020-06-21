from ariadne import load_schema_from_path, make_executable_schema
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

# Load schema from file...
type_defs = load_schema_from_path("./src/graphql/schema.graphql")

# Build an executable schema
schema = make_executable_schema(type_defs)

app = Flask(__name__)


@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=None)
    status_code = 200 if success else 400
    return jsonify(result), status_code
