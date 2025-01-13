export const mockData = {
  matchResult: {
    score: 85,
    details: [
      {
        category: "技能匹配",
        score: 90,
        suggestions: [
          "您的技术栈与职位要求高度匹配",
          "具备所需的主要编程语言和框架经验",
          "建议在简历中更详细地展示项目经验",
        ],
      },
      {
        category: "经验要求",
        score: 80,
        suggestions: [
          "工作经验基本符合要求",
          "可以更突出展示团队协作经历",
          "建议添加更多数据量化的成果",
        ],
      },
      {
        category: "教育背景",
        score: 85,
        suggestions: [
          "学历符合职位要求",
          "专业方向匹配度高",
          "可以添加相关证书或培训经历",
        ],
      },
    ],
  },
  sampleJD: `
    职位要求：
    1. 计算机相关专业本科及以上学历
    2. 3年以上 Web 开发经验
    3. 精通 Vue.js, React 等前端框架
    4. 熟悉 Python, Node.js 等后端技术
    5. 有良好的团队协作能力
    6. 具备独立解决问题的能力
  `,
};

export const isGitHubPages = window.location.hostname.includes("github.io");
