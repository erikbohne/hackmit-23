import json

def get_data_length(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if 'data' in data and isinstance(data['data'], list):
                return len(data['data'])
            else:
                return 0  # 'data' key not found or not a list
    except FileNotFoundError:
        return 0  # File not found
    except json.JSONDecodeError:
        return 0  # Invalid JSON format




# Replace 'filtered_data.json' with your actual file path
filename = 'filtered_data.json'
data_length = get_data_length(filename)
print(f"Length of 'data' array: {data_length}")



import json

def extract_summary_ids_from_json(json_file):
    # Initialize an empty list to store summary_ids
    summary_ids = []

    try:
        # Open and read the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
            
            # Check if the JSON structure matches what you provided
            if 'data' in data and isinstance(data['data'], list):
                # Iterate through the list of data items
                for item in data['data']:
                    # Check if each item has a 'metadata' field with a 'summary_id'
                    if 'metadata' in item and 'summary_id' in item['metadata']:
                        # Append the 'summary_id' to the list
                        summary_ids.append(item['metadata']['summary_id'])
            else:
                print("Invalid JSON structure. 'data' key should be a list.")

    except FileNotFoundError:
        print(f"File '{json_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return summary_ids






summary_ids = extract_summary_ids_from_json('filtered_data.json')

# Print the list of summary_ids
print(summary_ids)




with open('filtered_data.json', 'r') as file:
    data = json.load(file)
    for i in data['data']:
        print('----------')
        print(i)