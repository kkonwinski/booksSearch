import openai


class ChatGbtAdapter:
    API_TOKEN = ''

    def prepare_question(self, question: str):
        openai.api_key = self.API_TOKEN
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}",
            temperature=0.9,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

    def show_response(self, response: dict = None):
        print(response.get('choices')[0].get('text'))
