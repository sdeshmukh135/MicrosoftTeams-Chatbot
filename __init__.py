import logging
import openai
import azure.functions as func

secret_key = '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'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Give OpenAI our secret_key to authenticate
    openai.api_key = secret_key

    # get variables from HTTP request body
    req_body = req.get_json()

    # call OpenAI API
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
)

    # format response
    output_text = output['choices'][0]['text']

    # provide response
    return func.HttpResponse(
              output_text,
             status_code=200
        )
