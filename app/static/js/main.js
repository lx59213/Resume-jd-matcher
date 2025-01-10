const { createApp, ref } = Vue;
const { ElMessage } = ElementPlus;

// 创建 Vue 应用
const app = createApp({
  setup() {
    // 获取标语
    const appElement = document.getElementById("app");
    const slogan = appElement.dataset.slogan;
    const showSlogan = ref(true);

    // 标签页状态
    const activeTab = ref("jobAnalysis");
    const loading = ref(false);
    const jdText = ref("");
    const jobAnalysis = ref("");
    const matchAnalysis = ref("");
    const resumeContent = ref("");
    const selectedFiles = ref([]);

    // 切换标语显示
    const toggleSlogan = () => {
      showSlogan.value = !showSlogan.value;
    };

    // 处理文件变化
    const handleFileChange = (file, fileList) => {
      selectedFiles.value = fileList;
    };

    // 处理表单提交
    const handleSubmit = async () => {
      if (selectedFiles.value.length === 0) {
        ElMessage.warning("请先选择简历文件");
        return;
      }

      if (!jdText.value.trim()) {
        ElMessage.warning("请输入职位描述");
        return;
      }

      loading.value = true;
      const formData = new FormData();
      selectedFiles.value.forEach((file) => {
        formData.append("files", file.raw);
      });
      formData.append("jd", jdText.value);

      try {
        const response = await fetch("/analyze", {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          throw new Error("分析失败");
        }

        const result = await response.json();
        jobAnalysis.value = result.jobAnalysis || "";
        matchAnalysis.value = result.matchAnalysis || "";
        resumeContent.value = result.resumeContent || "";

        ElMessage.success("分析完成");
      } catch (error) {
        console.error("Error:", error);
        ElMessage.error(error.message || "分析失败");
      } finally {
        loading.value = false;
      }
    };

    return {
      slogan,
      showSlogan,
      activeTab,
      loading,
      jdText,
      jobAnalysis,
      matchAnalysis,
      resumeContent,
      toggleSlogan,
      handleFileChange,
      handleSubmit,
    };
  },
});

// 注册必要的组件
app.use(ElementPlus);

// 注册图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

// 挂载应用
app.mount("#app");
