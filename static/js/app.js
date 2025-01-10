const { createApp, ref } = Vue;
const { ElMessage } = ElementPlus;

// 导入所需的图标
const { UploadFilled } = ElementPlusIconsVue;

const app = createApp({
  setup() {
    const jobDescription = ref("");
    const loading = ref(false);
    const uploadFile = ref(null);

    const handleSuccess = (response) => {
      uploadFile.value = response.filename;
      ElMessage({
        message: "File uploaded successfully",
        type: "success",
      });
    };

    const handleError = () => {
      uploadFile.value = null;
      ElMessage.error("Upload failed");
    };

    const analyze = async () => {
      if (!uploadFile.value) {
        ElMessage.warning("Please upload a resume first");
        return;
      }

      if (!jobDescription.value) {
        ElMessage.warning("Please enter a job description");
        return;
      }

      loading.value = true;
      try {
        const response = await fetch("/analyze", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            filename: uploadFile.value,
            jobDescription: jobDescription.value,
          }),
        });

        if (!response.ok) {
          throw new Error("Analysis failed");
        }

        const result = await response.json();
        ElMessage({
          message: "Analysis complete",
          type: "success",
        });
      } catch (error) {
        ElMessage.error(error.message || "Analysis failed");
      } finally {
        loading.value = false;
      }
    };

    return {
      jobDescription,
      loading,
      handleSuccess,
      handleError,
      analyze,
    };
  },
});

// 注册图标组件
app.component("upload-filled", UploadFilled);

app.use(ElementPlus);
app.mount("#app");
