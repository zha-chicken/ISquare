# AnalyzeAI.py
import ollama

def analyze_user_questions():
    """分析用户问题并生成用户特征，使用默认文件路径"""
    try:
        with open("user_questions.log", "r", encoding="utf-8") as f:
            data = f.read()

        analyze_prompt = ('不要输出深度思考过程，直接给结果->这是一位用户问AI的问题:' + data + 
                         '能帮我一句话分析ta的喜好,目标，和情绪吗?注意：我只要一句话，格式：用户的情绪是xxx,喜好是xxx,目标是xxx,如果用户没有关于某个的就不要跟我说了。')

        # 确保模型已拉取到本地
        ollama.pull('deepseek-r1:1.5b')

        # 与模型交互
        response = ollama.generate(
            model='deepseek-r1:1.5b',
            prompt=analyze_prompt
        )
        
        with open("user_characteristics.txt", "a", encoding="ANSI") as e:
            e.write(response['response'])
    
    except Exception as e:
        print(f"分析过程中出错: {e}")
        return None

# 如果直接运行脚本，执行分析
if __name__ == "__main__":
    analyze_user_questions()