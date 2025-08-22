// Czekamy, aż cała strona się załaduje
document.addEventListener('DOMContentLoaded', function() {

    // Znajdujemy w HTML ikonę plecaka i jego zawartość po ich ID
    const ikonaPlecaka = document.getElementById('ikona-plecaka');
    const zawartoscPlecaka = document.getElementById('zawartosc-plecaka');

    // Mówimy przeglądarce: "słuchaj" na kliknięcia w ikonę plecaka
    ikonaPlecaka.addEventListener('click', function() {
        
        // Sprawdzamy, czy zawartość plecaka jest aktualnie ukryta
        if (zawartoscPlecaka.style.display === 'none') {
            // Jeśli tak, to ją pokaż (zmień display na 'block')
            zawartoscPlecaka.style.display = 'block';
        } else {
            // W przeciwnym wypadku (czyli jeśli jest widoczna), ukryj ją
            zawartoscPlecaka.style.display = 'none';
        }
    });
});