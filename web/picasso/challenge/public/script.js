document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('container');
    const numRows = 7;


    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < 100; j++) {
            const pixel = document.createElement('div');
            pixel.classList.add('pixel');
            container.appendChild(pixel);
        }
    }

    const pixels = document.querySelectorAll('.pixel');
    pixels.forEach(pixel => {
        pixel.addEventListener('click', function () {
            if (this.style.backgroundColor === 'black') {
                this.style.backgroundColor = 'white';
            } else {
                this.style.backgroundColor = 'black';
            }
        });
    });


});

