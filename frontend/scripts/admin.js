document.getElementById("logout").addEventListener("click", async function () {
    await fetch('/logout');
    window.location.href = "/";
});