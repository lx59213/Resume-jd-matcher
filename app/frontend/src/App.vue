<template>
  <div class="app-container">
    <el-alert v-if="isGitHubPages" type="info" :closable="false" show-icon>
      这是演示版本，使用模拟数据。要体验完整功能，请
      <el-link
        type="primary"
        href="https://github.com/yourusername/Resume-jd-matcher#本地部署"
        target="_blank"
      >
        下载并部署项目
      </el-link>
    </el-alert>
    <!-- 其他内容保持不变 -->
  </div>
</template>

<script>
import { isGitHubPages } from "./mock/data";

export default {
  data() {
    return {
      isGitHubPages,
    };
  },
};
</script>
