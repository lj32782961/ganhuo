document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("language-button");
    const dropdown = document.getElementById("language-dropdown");
    const currentLanguage = document.getElementById("current-language");

    button.addEventListener("click", function (event) {
        event.stopPropagation();  // 防止触发 `document` 的点击事件
        // if (dropdown.style.display === "none" || dropdown.style.display === "") {
        //     dropdown.style.display = "block";  // 显示下拉框
        // } else {
        //     dropdown.style.display = "none";  // 隐藏下拉框
        // }
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
    });
    });

    // 点击外部区域时，关闭下拉框
    document.addEventListener("click", function (event) {
        if (!button.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.style.display = "none";
        }
    });

    // 高亮当前选择的语言
    const langCode = currentLanguage.textContent.trim().toLowerCase();
    document.querySelectorAll("#language-dropdown a").forEach(link => {
        if (link.dataset.lang === langCode) {
            link.classList.add("active");
        }
        link.addEventListener('click', function () {
            currentLanguage.textContent = link.textContent.trim();  // 更新当前语言显示
            dropdown.style.display = "none";  // 选择语言后关闭下拉框
        });
    });
});

