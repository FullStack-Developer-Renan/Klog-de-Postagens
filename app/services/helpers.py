def verify_recieved_key(data: dict):
    required_keys = ["title", "date", "content", "writer", "email"]
    keys = data.keys()

    return [key for key in required_keys if key not in keys]


def get_profile(data: dict):
    if verify_recieved_key(data):
        raise KeyError(
            {
                "error": {
                    "required_keys": ["title", "date", "content", "writer", "email"],
                    "recieved_keys": list(data.keys()),
                }
            },
            400,
        )

    return [data]