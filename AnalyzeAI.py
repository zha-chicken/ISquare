import ollama

with open("user_questions.log", "r",encoding = "utf-8") as f:  # 打开文件
    data = f.read()  # 读取文件

Analyze = '不要输出深度思考过程，直接给结果->这是一位用户问AI的问题:'+data+'能帮我一句话分析ta的喜好,目标，和情绪吗?注意：我只要一句话，格式：用户的情绪是xxx,喜好是xxx,目标是xxx,如果用户没有关于某个的就不要跟我说了。'

# 确保模型已拉取到本地
ollama.pull('deepseek-r1:1.5b')

# 与模型交互
response = ollama.generate(
    model='deepseek-r1:1.5b',
    prompt=Analyze
)
print(response['response'])
with open("user_characteristics.txt","a") as e:
    e.write(response['response'])