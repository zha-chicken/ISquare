'''
import ollama
from datetime import datetime

# 对话记录文件
LOG_FILE = "conversation_log.txt"

def log_conversation(user_input, ai_response):
    """将对话记录追加到文件中"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] 用户: {user_input}\n")
        f.write(f"[{timestamp}] AI: {ai_response}\n")
        f.write("-" * 50 + "\n")  # 分隔线

def main():
    # 确保模型已拉取到本地
    try:
        ollama.pull('deepseek-r1:1.5b')
    except Exception as e:
        print(f"模型加载错误: {e}")
        return

    print("对话系统已启动(输入'退出'结束对话)")
    
    while True:
        ASK = str(input("Question: ")).strip()
        
        if ASK.lower() in ['退出', 'exit', 'quit']:
            print("对话结束")
            break
            
        if not ASK:
            continue
            
        try:
            # 与模型交互
            response = ollama.generate(
                model='deepseek-r1:1.5b',
                prompt=ASK
            )
            ai_response = response['response']
            print("AI:", ai_response)
            
            # 记录对话
            log_conversation(ASK, ai_response)
            
        except Exception as e:
            print(f"发生错误: {e}")
            continue

if __name__ == "__main__":
    main()
'''
import ollama
from datetime import datetime

with open("user_characteristics.txt", "r",encoding = "ANSI") as f:  # 打开文件
    usrcharacteristics = f.read()  # 读取文件

# 文件定义
DIALOG_LOG = "conversation_log.txt"  # 完整对话记录
QUESTION_LOG = "user_questions.log"   # 单独的用户提问记录

def log_question(user_input):
    """单独记录用户提问"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(QUESTION_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {user_input}\n")

def log_dialog(user_input, ai_response):
    """记录完整对话"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DIALOG_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] 用户: {user_input}\n")
        f.write(f"[{timestamp}] AI: {ai_response}\n")
        f.write("-" * 50 + "\n")

def main():
    # 初始化日志文件头
    with open(QUESTION_LOG, "a", encoding="utf-8") as f:
        f.write("\n" + "="*30 + " 新会话开始 " + "="*30 + "\n")
    
    with open(DIALOG_LOG, "a", encoding="utf-8") as f:
        f.write("\n" + "="*30 + " 新对话开始 " + "="*30 + "\n")

    # 确保模型已拉取到本地
    try:
        ollama.pull('deepseek-r1:1.5b')
    except Exception as e:
        print(f"模型加载错误: {e}")
        return

    print("对话系统已启动(输入'退出'结束对话)")
    
    while True:
        ASK = str(input("Question: ")).strip()
        INPUTAI = str("我目前的状态是："+usrcharacteristics+"请依照这个给我回答"+ASK)
        
        if ASK.lower() in ['退出', 'exit', 'quit']:
            print("对话结束")
            break
            
        if not ASK:
            continue
            
        try:
            # 记录用户问题(单独记录)
            log_question(ASK)
            
            # 与模型交互
            response = ollama.generate(
                model='deepseek-r1:1.5b',
                prompt=INPUTAI
            )
            ai_response = response['response']
            print("AI:", ai_response)
            
            # 记录完整对话
            log_dialog(ASK, ai_response)
            
        except Exception as e:
            print(f"发生错误: {e}")
            continue

if __name__ == "__main__":
    main()