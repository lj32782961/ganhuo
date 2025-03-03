const languageLinks = document.querySelectorAll('.language-switch a');

    languageLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            // event.preventDefault(); // 阻止默认跳转行为

            // 移除所有链接的 active 类
            languageLinks.forEach(l => l.classList.remove('active'));

            // 添加 active 类到被点击的链接
            link.classList.add('active');

            //  此处可以根据需要添加跳转逻辑，例如：
            //  setTimeout(() => { window.location.href = link.href; }, 100); // 延迟 100ms 跳转

        });
    });

    const tags = document.querySelectorAll('.tag-cloud a');

    tags.forEach(tag => {
        tag.addEventListener('click', (event) => {
            // event.preventDefault(); // 阻止默认跳转行为

            // 移除所有链接的 active 类
            tags.forEach(l => l.classList.remove('active'));

            // 添加 active 类到被点击的链接
            tag.classList.add('active');

            // 保存激活的标签到 localStorage
            localStorage.setItem('activeTag', tag.textContent);

            //  此处可以根据需要添加跳转逻辑，例如：
             setTimeout(() => { window.location.href = link.href; }, 100); // 延迟 100ms 跳转
            
            // 页面加载完成后，检查 localStorage 中是否有 activeTag，并应用样式
            window.addEventListener('load', () => {
            const activeTag = localStorage.getItem('activeTag');
            if (activeTag) {
                const activeLink = Array.from(document.querySelectorAll('.tag-cloud a')).find(link => link.textContent === activeTag);  // 使用Array.from和find方法更可靠地查找
                if (activeLink) {
                activeLink.classList.add('active');
                }
            }
            });
        });
    });