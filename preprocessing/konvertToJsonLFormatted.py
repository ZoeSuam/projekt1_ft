import json


def parse_jsonl_file(file_path):
    parsed_conversations = []
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            content = file.read().strip()

            # Properly format the content to be a valid JSON array
            # Add commas between objects and wrap the entire content in square brackets
            formatted_content = "[" + content.replace("}\n{", "},\n{") + "]"

            # Parse the formatted content as JSON
            conversations = json.loads(formatted_content)

            # Assuming each conversation is now a proper JSON object
            for conversation in conversations:
                parsed_conversations.append(conversation)
    except Exception as e:
        print(f"An error occurred: {e}")
    return parsed_conversations


def sec():
    file_path = '../venv/data/TrainingData2.jsonl'
    output_file_path = '../ParsedConversations2.jsonl'  # Define the output file name
    parsed_conversations = parse_jsonl_file(file_path)
    print(len(parsed_conversations), "conversations parsed.")

    # Write the parsed conversations to a new file in JSON Lines format
    try:
        with open(output_file_path, 'w') as outfile:
            for conversation in parsed_conversations:
                json_str = json.dumps(conversation)  # Convert the dictionary to a JSON string
                outfile.write(json_str + '\n')  # Write the JSON string to a file, adding a newline character
        print(f"Parsed conversations have been saved to {output_file_path}")
    except Exception as e:
        print(f"Failed to write the file: {e}")



if __name__ == "__main__":
    sec()



