const { createApp, ref } = Vue;

// 创建应用实例
const app = createApp({
  setup() {
    const activeTab = ref("jobAnalysis");
    const jdText = ref("");
    const loading = ref(false);
    const jobAnalysis = ref("");
    const matchAnalysis = ref("");
    const resumeContent = ref("");
    const fileList = ref([]);
    const showSlogan = ref(true);
    const slogan = ref(
      document.querySelector("#app").getAttribute("data-slogan")
    );

    const toggleSlogan = () => {
      showSlogan.value = !showSlogan.value;
    };

    const handleFileChange = (file) => {
      fileList.value.push(file.raw);
    };

    const handleSubmit = async () => {
      if (fileList.value.length === 0) {
        ElementPlus.ElMessage.error("请选择简历文件");
        return;
      }

      if (!jdText.value) {
        ElementPlus.ElMessage.error("请输入职位描述");
        return;
      }

      loading.value = true;
      const formData = new FormData();
      fileList.value.forEach((file) => {
        formData.append("files[]", file);
      });
      formData.append("jd", jdText.value);

      try {
        const response = await fetch("/upload", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();
        if (response.ok) {
          jobAnalysis.value = data.job_analysis;
          matchAnalysis.value = data.match_analysis;
          resumeContent.value = data.resume;
        } else {
          ElementPlus.ElMessage.error(data.error || "处理失败，请重试");
        }
      } catch (error) {
        console.error("Error:", error);
        ElementPlus.ElMessage.error("发生错误：" + error.message);
      } finally {
        loading.value = false;
      }
    };

    return {
      activeTab,
      jdText,
      loading,
      jobAnalysis,
      matchAnalysis,
      resumeContent,
      handleFileChange,
      handleSubmit,
      showSlogan,
      slogan,
      toggleSlogan,
    };
  },
});

// 注册 Element Plus
app.use(ElementPlus);

// 注册图标组件
app.component("el-icon-arrow-down", ElementPlusIconsVue.ArrowDown);

// 挂载应用
app.mount("#app");
