document.addEventListener("DOMContentLoaded", function () {
    const html = document.documentElement;
    const oldButton = document.querySelector(".theme-toggle");

    if (!oldButton) return;

    // Ganti tombol agar event bawaan Django tidak ikut berjalan.
    const button = oldButton.cloneNode(true);
    oldButton.replaceWith(button);

    // Jika tema masih auto, ubah menjadi light.
    if (html.dataset.theme === "auto") {
        html.dataset.theme = "light";
        localStorage.setItem("theme", "light");
    }

    // Siklus hanya Light dan Dark.
    button.addEventListener("click", function () {
        const current = html.dataset.theme;
        const next = current === "dark" ? "light" : "dark";

        html.dataset.theme = next;
        localStorage.setItem("theme", next);
    });
});