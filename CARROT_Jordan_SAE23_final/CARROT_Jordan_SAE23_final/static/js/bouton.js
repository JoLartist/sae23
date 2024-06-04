document.getElementById('showFormsButton').addEventListener('click', function() {
            var formsContainer = document.getElementById('formsContainer');
            if (formsContainer.style.display === 'none' || formsContainer.style.display === '') {
                formsContainer.style.display = 'block';
            } else {
                formsContainer.style.display = 'none';
            }
        });