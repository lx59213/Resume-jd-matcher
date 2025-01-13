import { mockData, isGitHubPages } from "../mock/data";

export async function analyzeResume(file, jd) {
  if (isGitHubPages) {
    // 在 GitHub Pages 环境下返回模拟数据
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(mockData);
      }, 1500); // 添加延迟模拟真实API调用
    });
  }

  // 真实环境的 API 调用代码保持不变
  const formData = new FormData();
  formData.append("resume", file);
  formData.append("jd", jd);

  const response = await fetch("/api/analyze", {
    method: "POST",
    body: formData,
  });

  return response.json();
}
