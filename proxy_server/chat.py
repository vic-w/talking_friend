import openai
from key import key

# 设置你的 OpenAI API 密钥
openai.api_key = key
class GPT():
    def __init__(self):
        self.messages = [ {"role": "system", "content": "请用简短的语言回答，每次不超过5句话"} ]

    def chat(self):
        audio_file = open("question.wav", "rb")
        transcript = openai.audio.transcriptions.create(
          model="whisper-1",
          file=audio_file,
          response_format='text'
        )
        
        print(transcript)
        self.messages.append({"role": "user", "content": transcript} )

        if len(self.messages)>20:
            self.messages = self.messages[-20:]

    
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages = self.messages,
            #response_format={'type': 'json_object'}
        )
    
        text = completion.choices[0].message.content

        print(text)
        
        response = openai.audio.speech.create(
          model="tts-1",
          voice="alloy",
          input=text,
          response_format = 'wav'
        )
        
        response.stream_to_file('answer.wav')
    
if __name__ == '__main__':
    gpt = GPT()
    gpt.chat()
