document.addEventListener("DOMContentLoaded", function () {
    const quizData = [
        {
            question: "1. O que é Phishing?",
            options: [
                "Ataque que engana o usuário para obter informações sensíveis.",
                "Técnica de pescar dados reais.",
                "Malware que se replica automaticamente.",
                "Firewall mal configurado.",
                "Tipo de criptografia"
            ],
            answer: 1
        },
        {
            question: "2. Qual dessas é uma prática recomendada de segurança?",
            options: [
                "Usar a mesma senha em todos os sites.",
                "Evitar atualizações de sistema.",
                "Clicar em links de e-mails desconhecidos.",
                "Ativar autenticação de dois fatores.",
                "Compartilhar senhas com amigos."
            ],
            answer: 3
        },
        {
            question: "3. O que faz um antivírus?",
            options: [
                "Cria senhas seguras para o usuário.",
                "Remove contas suspeitas da internet.",
                "Detecta, bloqueia e remove softwares maliciosos.",
                "Protege contra spam.",
                "Acelera a internet."
            ],
            answer: 2
        },
        {
            question: "4. Qual o principal objetivo de um firewall?",
            options: [
                "Controlar o brilho da tela.",
                "Aumentar a velocidade de download.",
                "Monitorar e controlar o tráfego de rede.",
                "Desligar o computador em caso de ataque.",
                "Formatar o HD automaticamente."
            ],
            answer: 2
        },
        {
            question: "5. O que é engenharia social?",
            options: [
                "Uso de redes sociais para divulgar cursos.",
                "Técnica de manipulação para obter informações.",
                "Análise de dados para fins de marketing.",
                "Método de backup.",
                "Estudo de vulnerabilidades físicas."
            ],
            answer: 1
        }
    ];

    const quizContainer = document.getElementById("quiz");

    function renderQuiz() {
        const form = document.createElement("form");
        quizData.forEach((q, index) => {
            const questionDiv = document.createElement("div");
            questionDiv.classList.add("quiz-question");

            const title = document.createElement("h3");
            title.textContent = q.question;
            questionDiv.appendChild(title);

            q.options.forEach((opt, i) => {
                const label = document.createElement("label");
                label.classList.add("quiz-option");
                label.style.display = "block"; // Garante que fique um abaixo do outro

                const input = document.createElement("input");
                input.type = "radio";
                input.name = "question" + index;
                input.value = i;
                label.appendChild(input);
                label.append(" " + opt);

                questionDiv.appendChild(label);
            });

            form.appendChild(questionDiv);
        });

        const submitBtn = document.createElement("button");
        submitBtn.type = "button";
        submitBtn.classList.add("quiz-submit");
        submitBtn.textContent = "Enviar";
        form.appendChild(submitBtn);

        const results = document.createElement("div");
        results.classList.add("quiz-results");
        form.appendChild(results);

        submitBtn.addEventListener("click", () => {
            let score = 0;
            quizData.forEach((q, index) => {
                const selected = form.querySelector(`input[name="question${index}"]:checked`);
                const correct = q.answer;

                const questionDiv = form.children[index];
                if (selected) {
                    if (parseInt(selected.value) === correct) {
                        score++;
                        selected.parentElement.style.color = "#0f0";
                    } else {
                        selected.parentElement.style.color = "#f00";
                        const correctLabel = questionDiv.querySelectorAll("label")[correct];
                        correctLabel.style.color = "#0f0";
                    }
                } else {
                    const correctLabel = questionDiv.querySelectorAll("label")[correct];
                    correctLabel.style.color = "#0f0";
                }
            });

            results.innerHTML = `<h3>Você acertou ${score} de ${quizData.length} perguntas.</h3>`;
        });

        quizContainer.innerHTML = "";
        quizContainer.appendChild(form);
    }

    renderQuiz();
});
