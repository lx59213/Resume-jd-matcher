document.addEventListener("DOMContentLoaded", function () {
  // 文件上传处理
  const fileInput = document.getElementById("resume-upload");
  const uploadButton = document.querySelector(".upload-button");
  let files = [];

  fileInput.addEventListener("change", function (e) {
    files = Array.from(e.target.files);
    uploadButton.textContent =
      files.length > 0 ? `已选择 ${files.length} 个文件` : "选择文件";
  });

  // 标签切换
  const tabs = document.querySelectorAll(".tab");
  const tabContent = document.querySelector(".tab-content");

  tabs.forEach((tab) => {
    tab.addEventListener("click", function () {
      // 移除其他标签的激活状态
      tabs.forEach((t) => t.classList.remove("active"));
      // 激活当前标签
      this.classList.add("active");
      // TODO: 更新标签内容
    });
  });

  // 分析按钮处理
  const analyzeButton = document.querySelector(".analyze-button");
  const textarea = document.querySelector("textarea");

  analyzeButton.addEventListener("click", async function () {
    if (files.length === 0) {
      alert("请先上传简历文件");
      return;
    }

    if (!textarea.value.trim()) {
      alert("请输入职位描述");
      return;
    }

    analyzeButton.disabled = true;
    analyzeButton.textContent = "分析中...";

    try {
      // 创建 FormData 对象
      const formData = new FormData();
      files.forEach((file) => {
        formData.append("files", file);
      });
      formData.append("jobDescription", textarea.value);

      // 发送请求
      const response = await fetch("/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("分析失败");
      }

      const result = await response.json();
      // TODO: 显示分析结果
    } catch (error) {
      alert(error.message);
    } finally {
      analyzeButton.disabled = false;
      analyzeButton.textContent = "开始匹配";
    }
  });
});
