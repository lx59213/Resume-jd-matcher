# Element Plus CDN 使用指南

## 图标组件使用

在使用 Element Plus 的 CDN 版本时，图标组件的使用需要特别注意：

1. **引入顺序**：
```html
<!-- 先引入 Vue 3 -->
<script src="//unpkg.com/vue@3"></script>
<!-- 再引入 Element Plus -->
<script src="//unpkg.com/element-plus"></script>
<!-- 最后引入图标库 -->
<script src="//unpkg.com/@element-plus/icons-vue"></script>
```

2. **组件注册**：
在 main.js 中单独注册需要使用的图标组件：
```javascript
// 注册特定图标组件
app.component("el-icon-arrow-down", ElementPlusIconsVue.ArrowDown);
```

3. **模板使用**：
在 HTML 模板中使用图标时，需要使用 `el-icon-` 前缀：
```html
<el-icon class="custom-icon">
    <el-icon-arrow-down />
</el-icon>
```

4. **常见问题**：
- 如果出现 `Failed to resolve component` 错误，检查组件名称是否正确注册
- 组件名称必须使用 `el-icon-` 前缀
- 确保 CDN 引入顺序正确

5. **样式控制**：
```css
/* 图标旋转动画 */
.custom-icon {
    transition: transform 0.3s;
}
.custom-icon.is-active {
    transform: rotate(-90deg); /* 左右翻转 */
}
```

## 最佳实践

1. 只注册需要使用的图标组件，避免全局注册所有图标
2. 使用 `el-icon` 包裹图标组件，便于样式控制
3. 使用 CSS 类控制图标状态，而不是直接操作 DOM 