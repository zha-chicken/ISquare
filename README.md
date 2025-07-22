Isquare AI&Time Management

## 概述

结合AI与时间管理的先进产品
## 功能特点

1. **实时对话交互**：
   - 使用 DeepSeek-R1 大型语言模型进行对话
   - 支持自然语言交流
   

2. **用户特征分析**：
   - 自动分析用户提问内容
   - 识别用户情绪、喜好和目标
   - 生成用户特征摘要（一句话格式）
   - 输入“清除个性化配置”以重置用户分析

3. **对话记忆**：
   - 记录完整对话历史
   - 单独保存用户提问记录
   - 持续更新用户特征分析

## 文件说明

| 文件名 | 功能描述 |
|--------|----------|
| `ConversationAI.py` | 主对话程序，处理用户交互和日志记录 |
| `AnalyzeAI.py` | 用户特征分析程序，处理用户提问日志 |
| `restart_service` | 重启服务 |
| `user_questions.log` | 用户提问历史记录（自动生成） |
| `conversation_log.txt` | 完整对话记录（自动生成） |
| `user_characteristics.txt` | 用户特征分析结果（自动生成） |

## 安装与使用

### 前置要求

1. 安装 Python 3.7+
2. 安装 依赖：
   ```bash
   pip install ollama
   pip install pycryptodome
   pip install flask
   pip install flask_cors
   ```

### 运行步骤

1. **拉取语言模型**（首次运行前）：
2. 下载ollama
3. 
   ```bash
   ollama pull deepseek-r1:8b
   ```

4. **启动对话API**：
   ```bash
   python ConversationAI.py
   ```

5. **开始对话**：
   ```
   调用API(前端网页MAIN.html)
   ```

## 技术说明

1. **特征分析格式**：
   - 系统会生成一句话格式的用户特征摘要
   - 格式：`用户的情绪是xxx,喜好是xxx,目标是xxx`
   - 缺失的特征项会被自动省略
   - 正规则表达式过滤分析内容并且喂给对话AI

2. **文件编码**：
   - 用户提问日志：UTF-8
   - 特征分析结果：ANSI
   - 完整对话记录：UTF-8 (AES加密，密钥储存在key.txt)

3. **特征更新机制**：
   - 每次用户提问后自动更新特征分析
   - 最新特征会用于后续所有对话

## 注意事项

1. 首次运行需要下载约 1.5B 参数的模型，请确保网络畅通(1.1GB)
2. 系统会持续追加日志内容，建议定期清理旧日志文件
3. 特征分析基于用户提问内容，提问越多分析越准确
4. 如需更换模型，请修改代码中的 `deepseek-r1:8b` 为其他可用模型

## 自定义建议

1. **调整分析频率**：  
   修改 `ConversationAI.py` 中的 `AnalyzeAI.analyze_user_questions()` 调用位置可改变特征分析频率

2. **更改模型**：  
   替换代码中的模型名称可使用其他 Ollama 支持的模型

3. **修改日志格式**：  
   编辑 `log_question` 和 `log_dialog` 函数可自定义日志格式

模仿用户 创造情绪价值
