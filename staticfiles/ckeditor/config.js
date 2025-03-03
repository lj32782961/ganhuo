CKEDITOR.editorConfig = function (config) {
    config.language = 'zh-cn';  // 设置语言
    config.uiColor = '#AADC6E'; // 界面颜色
    config.toolbar = [
        { name: 'basicstyles', items: ['Bold', 'Italic', 'Underline', 'Strike'] },
        { name: 'paragraph', items: ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'] },
        { name: 'insert', items: ['Image', 'Table', 'HorizontalRule', 'SpecialChar', 'Templates'] },  // 添加 "插入模板" 按钮
        { name: 'styles', items: ['Format', 'Font', 'FontSize'] },
        { name: 'colors', items: ['TextColor', 'BGColor'] },
        { name: 'tools', items: ['Maximize'] }
    ];
    config.extraPlugins = 'templates';  // 启用“模板”插件
    config.templates_files = ['/static/ckeditor/templates/templates.js'];  // 载入自定义模板
};
