document.addEventListener("DOMContentLoaded", function () {
  const app = Vue.createApp({
    data() {
      return {
        showSlogan: true,
        slogan: document.getElementById("app").dataset.slogan,
        activeTab: "jobAnalysis",
        files: [],
        loading: false,
        jobAnalysis: "",
        matchAnalysis: "",
        resumeContent: "",
      };
    },
    methods: {
      toggleSlogan() {
        this.showSlogan = !this.showSlogan;
      },
      async handleSubmit() {
        const fileInput = document.getElementById("resume-upload");
        const textarea = document.querySelector("textarea");

        if (fileInput.files.length === 0) {
          ElementPlus.ElMessage.warning("请选择简历文件");
          return;
        }

        if (!textarea.value.trim()) {
          ElementPlus.ElMessage.warning("请输入职位描述");
          return;
        }

        this.loading = true;
        const formData = new FormData();

        for (const file of fileInput.files) {
          formData.append("files[]", file);
        }
        formData.append("jd", textarea.value);

        try {
          const response = await fetch("/upload", {
            method: "POST",
            body: formData,
          });

          if (!response.ok) {
            throw new Error("上传失败");
          }

          const result = await response.json();
          this.jobAnalysis = result.job_analysis;
          this.matchAnalysis = result.match_analysis;
          this.resumeContent = result.resume;

          ElementPlus.ElMessage.success("分析完成");
        } catch (error) {
          ElementPlus.ElMessage.error(error.message);
        } finally {
          this.loading = false;
        }
      },
    },
  });

  // 注册必要的组件
  app.use(ElementPlus);

  // 挂载应用
  app.mount("#app");

  // 标签切换功能
  const tabs = document.querySelectorAll(".tab");
  const tabContent = document.querySelector(".tab-content");

  tabs.forEach((tab) => {
    tab.addEventListener("click", function () {
      tabs.forEach((t) => t.classList.remove("active"));
      this.classList.add("active");
    });
  });

  // 文件上传按钮更新文本
  const fileInput = document.getElementById("resume-upload");
  const uploadButton = document.querySelector(".upload-button");

  fileInput.addEventListener("change", function () {
    const fileCount = this.files.length;
    if (fileCount > 0) {
      uploadButton.textContent = `已选择 ${fileCount} 个文件`;
    } else {
      uploadButton.textContent = "选择文件";
    }
  });

  // 分析按钮点击事件
  const analyzeButton = document.querySelector(".analyze-button");
  analyzeButton.addEventListener("click", function () {
    app._instance.proxy.handleSubmit();
  });
});
