from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

# 假设 chat 函数定义在 chat.py 中
from chat import GPT
gpt = GPT()

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    # 检查请求中是否包含文件
    if 'question' not in request.files:
        return jsonify({'error': '没有找到 question 文件'}), 400

    file = request.files['question']

    # 检查是否选择了文件
    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400

    # 保存上传的 question.wav 文件
    question_filename = 'question.wav'
    file.save(question_filename)

    # 调用 chat 函数处理 question.wav 并生成 answer.wav
    gpt.chat()

    # 检查 answer.wav 是否生成
    answer_filename = 'answer.wav'
    if not os.path.exists(answer_filename):
        return jsonify({'error': '未生成 answer.wav 文件'}), 500

    # 将 answer.wav 文件发送给客户端
    return send_file(answer_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

