from bottle import route, run, request, response
import os
import openai

# Replace with your actual OpenAI API key
openai.api_key = "sk-proj-alongandveryrandomseriesofcharacters"

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

def generate_llm_response(prompt):
    """Generates a response from the OpenAI API."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that understands and responds to API requests"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating LLM response: {e}")
        return "Error: Could not generate response."


@route('/<path:path>', method='ANY') #Catch all route
def wildcard_route(path):
    """Handles wildcard requests and generates an LLM response."""
    try:
        # Construct a prompt based on the request path and query parameters.
        query_string = request.query_string
        full_path = f"/{path}"
        if query_string:
            full_path += f"?{query_string}"

        prompt = f"You are a backend API engine respond to the following request, reply only with the api response and nothing else: {full_path}"

        # Generate the LLM response.
        llm_response = generate_llm_response(prompt)

        # Set the response content type.
        response.content_type = 'text/json'

        return llm_response

    except Exception as e:
        print(f"Error handling request: {e}")
        response.status = 500
        return "Internal Server Error"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)
