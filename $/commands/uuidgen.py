import uuid

def generate_uuid():
    unique_id = uuid.uuid4()
    print(f"Generated UUID: {unique_id}")

if __name__ == "__main__":
    generate_uuid()
