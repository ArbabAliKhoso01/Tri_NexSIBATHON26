// Wait until DOM loads
document.addEventListener("DOMContentLoaded", function () {

    // ===== Navbar mobile toggle =====
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            navLinks.classList.toggle("active");
        });
    }

    // ===== Cards toggle =====
    const loginCard = document.getElementById("login");
    const signupCard = document.getElementById("signup");

    const showSignup = document.getElementById("showSignup");
    const showLogin = document.getElementById("showLogin");

    // Default landing: login visible
    if (loginCard && signupCard) {
        loginCard.classList.add("active");
        signupCard.classList.remove("active");
    }

    // Show Sign Up
    if (showSignup && loginCard && signupCard) {
        showSignup.addEventListener("click", function (e) {
            e.preventDefault();
            loginCard.classList.remove("active");
            signupCard.classList.add("active");
        });
    }

    // Show Login
    if (showLogin && loginCard && signupCard) {
        showLogin.addEventListener("click", function (e) {
            e.preventDefault();
            signupCard.classList.remove("active");
            loginCard.classList.add("active");
        });
    }

});

