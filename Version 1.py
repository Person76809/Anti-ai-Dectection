import requests

# Function to check if the essay was generated by AI

def is_ai_generated(essay):

    # Send the essay to an AI detection API

    api_endpoint = 'https://aiessaydetectionapi.com/detect'

    response = requests.post(api_endpoint, json={'essay': essay})

    if response.status_code == 200:

        result = response.json()

        return result['is_ai_generated']

    else:

        # API request failed, handle the error here

        raise Exception('AI detection API request failed')

# Function to modify the essay to make it original

def modify_essay(essay):

    # Implement your algorithm to modify the essay here

    modified_essay = essay + " (Originality modifications added)"

    return modified_essay

# Example usage

essay = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

is_ai = is_ai_generated(essay)

if is_ai:

    modified_essay = modify_essay(essay)

    print("Original essay detected. Modified essay:")

    print(modified_essay)

else:

    print("Essay is not AI-generated. No modifications needed.")

    print(essay)

 

