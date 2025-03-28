


document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".carousel").forEach(carousel => {
        let items = carousel.querySelector(".carousel-items");
        let nextButton = carousel.querySelector(".next");
        let prevButton = carousel.querySelector(".prev");

        let index = 0;
        let itemWidth = items.querySelector(".carousel-item").offsetWidth;
        let gap = 10; // Ajuste esse valor conforme necessário

        // Corrigindo cálculo de itens visíveis
        let totalVisible = Math.floor(carousel.offsetWidth / (itemWidth + gap));
        let maxIndex = Math.max(0, items.children.length - totalVisible);
 // Último índice válido para rolagem

        // 🔹 Garante que os itens comecem alinhados à esquerda
        items.style.transform = "translateX(0)";

        nextButton.addEventListener("click", function () {
            if (index < maxIndex) {
                index++;
                items.style.transform = `translateX(-${index * (itemWidth + gap)}px)`;
            }
        });

        prevButton.addEventListener("click", function () {
            if (index > 0) {
                index--;
                items.style.transform = `translateX(-${index * (itemWidth + gap)}px)`;
            }
        });
    });
});
