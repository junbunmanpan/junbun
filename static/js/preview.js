document.addEventListener("DOMContentLoaded", () => {
    const previewButton = document.querySelector("button[type='button']"); // プレビュー用ボタン
    const titleInput = document.querySelector("input[name='title']"); // タイトル入力
    const contentInput = document.querySelector("textarea[name='content']"); // 本文入力
    const previewContainer = document.createElement("div"); // プレビュー表示用コンテナ
    previewContainer.classList.add("hidden", "border", "p-4", "mt-4", "bg-gray-100");

    // ボタンのクリックイベント
    previewButton.addEventListener("click", () => {
        const title = titleInput.value.trim();
        const content = contentInput.value.trim();

        if (!title || !content) {
            alert("タイトルと本文を入力してください。");
            return;
        }

        // プレビューの内容を生成
        previewContainer.innerHTML = `
            <h2 class="text-xl font-bold text-gray-800">プレビュー</h2>
            <h3 class="text-lg font-semibold mt-2">${title}</h3>
            <p class="mt-2">${content}</p>
        `;

        // プレビュー表示
        if (previewContainer.classList.contains("hidden")) {
            previewContainer.classList.remove("hidden");
        }

        // ボタンのすぐ上にプレビューを挿入
        previewButton.closest("form").insertAdjacentElement("afterend", previewContainer);
    });
});
