from doctran import Doctran

doctran = Doctran(openai_api_key=OPENAI_API_KEY)
document = doctran.parse(content="your_content_as_string")