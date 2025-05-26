document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".carousel").forEach(carousel => {
        let items = carousel.querySelector(".carousel-items");
        let nextButton = carousel.querySelector(".next");
        let prevButton = carousel.querySelector(".prev");

        let index = 0;
        let gap = 20;

        // Função para atualizar o carrossel e o estado dos botões
        function updateCarousel() {
            const item = items.querySelector(".carousel-item");
            if (!item) return;

            const itemWidth = item.offsetWidth;
            const carouselWidth = carousel.offsetWidth;
            const totalVisible = Math.floor(carouselWidth / (itemWidth + gap));
            const maxIndex = Math.max(0, items.children.length - totalVisible);

            // Corrige o deslocamento
            items.style.transform = `translateX(-${index * (itemWidth + gap)}px)`;

            // Atualiza o estado dos botões
            prevButton.disabled = index === 0;  // Desabilita botão "prev" se no início
            nextButton.disabled = index >= maxIndex;  // Desabilita botão "next" se no final

            return { itemWidth, gap, maxIndex };
        }

        let dimensions = updateCarousel();

        // Função para avançar no carrossel
        nextButton.addEventListener("click", function () {
            if (index < dimensions.maxIndex) {
                index++;
                items.style.transform = `translateX(-${index * (dimensions.itemWidth + gap)}px)`;
                updateCarousel();  // Atualiza o estado dos botões após a mudança
            }
        });

        // Função para voltar no carrossel
        prevButton.addEventListener("click", function () {
            if (index > 0) {
                index--;
                items.style.transform = `translateX(-${index * (dimensions.itemWidth + gap)}px)`;
                updateCarousel();  // Atualiza o estado dos botões após a mudança
            }
        });

        // Atualiza o carrossel quando a janela for redimensionada
        window.addEventListener("resize", function () {
            dimensions = updateCarousel();
        });
    });
});
