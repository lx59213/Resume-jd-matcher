import requests
from flask import current_app


def generate_matched_resume(resume_texts, jd_text):
    """
    使用AI生成匹配JD的简历和分析结果

    Returns:
        dict: 包含简历内容、职位分析和匹配度的字典
    """
    try:
        # 第一步：分析职位要求
        job_analysis = analyze_job_requirements(jd_text)

        # 第二步：生成匹配的简历
        matched_resume = generate_resume_content(resume_texts, jd_text)

        # 第三步：计算匹配度
        match_analysis = calculate_match_rate(job_analysis, resume_texts)

        return {
            "resume": matched_resume,
            "job_analysis": job_analysis,
            "match_analysis": match_analysis,
        }
    except Exception as e:
        raise Exception(f"AI处理错误: {str(e)}")


def analyze_job_requirements(jd_text):
    """分析职位要求"""
    try:
        headers = {
            "Authorization": f"Bearer {current_app.config['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个专业的职位分析专家，请分析该职位的关键要求。",
                },
                {
                    "role": "user",
                    "content": f"""请分析以下职位描述，提取关键要求：

{jd_text}

请按以下格式输出：
1. 必备技能：（列出3-5个最重要的技能要求）
2. 加分项：（列出2-3个优先考虑的条件）
3. 职位特点：（总结该职位的关键特征）
""",
                },
            ],
            "temperature": 0.7,
            "stream": False,
        }

        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data,
        )

        if response.status_code != 200:
            raise Exception(f"API调用失败: {response.text}")

        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        raise Exception(f"职位分析错误: {str(e)}")


def calculate_match_rate(job_analysis, resume_texts):
    """计算匹配度"""
    try:
        combined_resume = "\n".join(resume_texts)

        headers = {
            "Authorization": f"Bearer {current_app.config['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "你是一个专业的简历匹配分析专家。"},
                {
                    "role": "user",
                    "content": f"""请分析以下职位要求和简历的匹配程度：

职位分析：
{job_analysis}

简历内容：
{combined_resume}

请输出：
1. 整体匹配度评分（百分比）
2. 优势分析（列出3个最匹配的点）
3. 不足分析（列出2个需要提升的点）
4. 改进建议
""",
                },
            ],
            "temperature": 0.7,
            "stream": False,
        }

        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data,
        )

        if response.status_code != 200:
            raise Exception(f"API调用失败: {response.text}")

        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        raise Exception(f"匹配度分析错误: {str(e)}")


def generate_resume_content(resume_texts, jd_text):
    """生成匹配的简历内容"""
    try:
        headers = {
            "Authorization": f"Bearer {current_app.config['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": """你是一个专业的简历优化专家，擅长：
1. 分析职位JD，提取关键要求
2. 从简历中找出与JD最匹配的经验和技能
3. 调整内容顺序，突出重点
4. 优化语言表述，使其更专业和有针对性""",
                },
                {"role": "user", "content": create_prompt(resume_texts, jd_text)},
            ],
            "temperature": 0.7,
            "stream": False,
        }

        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=data,
        )

        if response.status_code != 200:
            raise Exception(f"API调用失败: {response.text}")

        return format_resume(response.json()["choices"][0]["message"]["content"])
    except Exception as e:
        raise Exception(f"简历生成错误: {str(e)}")


def create_prompt(resume_texts, jd_text):
    """
    创建AI提示词
    """
    prompt = f"""请分析以下职位描述(JD)和简历内容，生成一份最匹配该职位的简历：

职位描述：
{jd_text}

候选人简历：
"""

    # 添加所有简历内容
    for i, resume in enumerate(resume_texts, 1):
        prompt += f"\n简历 {i}:\n{resume}\n"

    prompt += """
请根据职位要求，从以上简历中：
1. 提取最相关的经验和技能
2. 调整内容的展示顺序，突出与职位最相关的部分
3. 优化语言表述，使其更符合职位要求
4. 确保生成的内容简洁、专业、有针对性

输出格式要求：
1. 基本信息（姓名、联系方式等）
2. 教育背景
3. 专业技能（与职位相关度最高的排在前面）
4. 工作经验（最相关的经验优先展示）
5. 项目经验（突出与职位要求相关的项目）

请直接输出优化后的简历内容，确保格式清晰。
"""

    return prompt


def format_resume(content):
    """
    格式化生成的简历内容
    """
    # 添加分隔线
    sections = content.split("\n\n")
    formatted_sections = []

    for section in sections:
        if section.strip():
            formatted_sections.append(section.strip())

    return "\n\n" + "-" * 50 + "\n\n".join(formatted_sections)
