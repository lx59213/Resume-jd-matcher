const { createApp, ref } = Vue;
const { ElMessage } = ElementPlus;

const app = createApp({
  setup() {
    const jobDescription = ref("");
    const loading = ref(false);

    const handleSuccess = (response) => {
      ElMessage({
        message: "File uploaded successfully",
        type: "success",
      });
    };

    const handleError = () => {
      ElMessage.error("Upload failed");
    };

    const analyze = async () => {
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
            jobDescription: jobDescription.value,
          }),
        });

        const result = await response.json();
        ElMessage({
          message: "Analysis complete",
          type: "success",
        });
      } catch (error) {
        ElMessage.error("Analysis failed");
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

app.use(ElementPlus);
app.mount("#app");
