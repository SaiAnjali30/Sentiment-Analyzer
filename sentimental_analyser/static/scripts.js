document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector("textarea");

    textarea.addEventListener("input", () => {
        const count = textarea.value.length;
        console.log(`Characters: ${count}`);
    });
});