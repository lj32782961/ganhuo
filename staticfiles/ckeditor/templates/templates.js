CKEDITOR.addTemplates('default', {
    imagesPath: CKEDITOR.getUrl(CKEDITOR.plugins.getPath('templates') + 'templates/images/'),
    templates: [
        {
            title: '两栏文章模板1',
            description: '用于博客文章的两栏排版',
            html: `
                <div class="page-container">
                    <header class="navbar">
                        <h2>网站标题</h2>
                    </header>
                    <div class="content-wrapper">
                        <main class="main-content">
                            <h2>文章标题</h2>
                            <p><strong>作者：</strong> xxx</p>
                            <p><em>发布时间：</em> yyyy-mm-dd</p>
                            <p>这里是正文内容...</p>
                        </main>
                        <aside class="sidebar">
                            <h3>文章标签</h3>
                            <ul>
                                <li>标签1</li>
                                <li>标签2</li>
                                <li>标签3</li>
                            </ul>
                            <h3>高热度文章</h3>
                            <ul>
                                <li>文章1</li>
                                <li>文章2</li>
                                <li>文章3</li>
                            </ul>
                        </aside>
                    </div>
                </div>
            `
        },

        {
            title: '两栏文章模板2',
            description: '包含导航栏和左右两栏的布局',
            html: `
                <nav style="background-color: #333; color: white; padding: 10px;">
                    <h2 style="margin: 0;">导航栏</h2>
                </nav>
                <div style="display: flex; margin-top: 10px;">
                    <div style="width: 30%; padding: 10px; background: #f4f4f4;">
                        <h3>左侧内容</h3>
                        <p>这里是左侧的内容区域。</p>
                    </div>
                    <div style="width: 70%; padding: 10px;">
                        <h3>右侧文章区域</h3>
                        <p>这里是主要的文章内容。</p>
                    </div>
                </div>
            `
        }
    ]
});
