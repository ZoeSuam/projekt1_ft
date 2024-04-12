from openai import OpenAI

def upload_file_and_finetune(file_path, model_name, api_key='xxxxxxxxxxxxxxxxxxx'):
    """
    Simplified version to upload a .jsonl file to OpenAI and create a fine-tuning job.

    :param file_path: Path to the .jsonl file to be uploaded.
    :param model_name: Name of the model to fine-tune.
    :param api_key: Your OpenAI API key.
    """
    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)

    try:
        # Upload the .jsonl file
        upload_response = client.files.create(
            file=open(file_path, "rb"),
            purpose="fine-tune"
        )
        print(f"File uploaded successfully. File ID: {upload_response.id}")

        # Create a fine-tuning job using the uploaded file
        fine_tune_response = client.fine_tuning.jobs.create(
            training_file=upload_response.id,
            model=model_name
        )
        print(f"Fine-tuning job created successfully. Job ID: {fine_tune_response.id}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

        

if __name__ == '__main__':
    # Make sure to replace the following placeholders with your actual data and API key
    upload_file_and_finetune("ParsedConversations2.jsonl", "ft:gpt-3.5-turbo-0125:personal::97QirxUL", api_key='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')

