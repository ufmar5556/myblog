document.addEventListener("DOMContentLoaded", function () {
    console.log("Ayra Starr Blog Loaded!");

    // Smooth scrolling for navigation
    document.querySelectorAll("a.nav-link").forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
