document.getElementById('popup-btn').addEventListener('click',
    function() {
    var popupContainer = document.getElementById('popup-container');
    var popupBox = document.createElement('div');
    var closeButton = document.createElement('span');

    popupBox.className = 'popup-box';
    popupBox.innerHTML = '<div class="popup-content">This is a popup box.</div>';
    closeButton.className = 'close-btn';
    closeButton.innerHTML = '&times;';
    popupBox.appendChild(closeButton);
    popupContainer.appendChild(popupBox);

    closeButton.addEventListener('click', function() {
        popupContainer.removeChild(popupBox);
    });
});

