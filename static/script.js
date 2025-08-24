// Czekamy, aż cała strona się załaduje
document.addEventListener('DOMContentLoaded', function() {

    // Znajdujemy w HTML ikonę plecaka i jego zawartość po ich ID
    const ikonaPlecaka = document.getElementById('ikona-plecaka');
    const zawartoscPlecaka = document.getElementById('zawartosc-plecaka');

    // Obsługa kliknięcia na ikonę plecaka
    ikonaPlecaka.addEventListener('click', function() {
        if (zawartoscPlecaka.style.display === 'none') {
            zawartoscPlecaka.style.display = 'block';
        } else {
            zawartoscPlecaka.style.display = 'none';
        }
    });

    // Automatyczne znikanie flashów po 3 sekundach
    const flashMessages = document.querySelectorAll('.flash-message');
    if (flashMessages.length > 0) {
        setTimeout(function() {
            flashMessages.forEach(function(msg) {
                msg.style.display = 'none';
            });
        }, 3000); // 3000 ms = 3 sekundy
    }
});