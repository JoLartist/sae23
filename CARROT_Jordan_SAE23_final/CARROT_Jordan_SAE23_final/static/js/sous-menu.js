// Pour rendre le menu déroulant utilisable avec le clavier
document.querySelectorAll('.dropdown-submenu').forEach(item => {
    item.addEventListener('focus', function() {
        this.querySelector('.dropdown-submenu-content').style.display = 'block';
    });
    item.addEventListener('blur', function() {
        this.querySelector('.dropdown-submenu-content').style.display = 'none';
    });
});

// Pour gérer les sélections dans le menu déroulant
document.getElementById('posteDropdown').addEventListener('change', function() {
    var selectedPoste = this.value;
    // Vous pouvez ajouter du code pour traiter la sélection ici
});
