const alertPanel = document.getElementById('alert');

const closeBtn = document.getElementById('close')

function handleClick(){

    alertPanel.style.display = 'none';

}

closeBtn.addEventListener('onclick',handleClick)