from app import create_app
from config import load_config

# Create the Flask app
instantiated_config = load_config()
app = create_app(instantiated_config)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=instantiated_config.debug)