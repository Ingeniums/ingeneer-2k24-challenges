document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('container');
    const numRows = 7; 
    
    const initialMatrix = [
        "1110000100100001000001110000000111100100001110011100111101111011111000000111101111000100111101111000",
        "1001001100100001000010001000000100100000010000100010100101000010001000000000100001001100100101000000",
        "1001010100100001000010001000000100100100010000100010100001000010001000000000100001010100100101000000",
        "1111011110111101000010001000000111100100010000111110111101111010001000000111101111000100111101111000",
        "1000000100100101000010001000000100000100010000100010000100001010001000000100000001000100100101001000",
        "1000000100100101000010001000000100000100010000100010100100001010001000000100000001000100100101001000",
        "1000000000111101111001110011110100000100001110100010111101111011111011110111101111011110111101111000"
    ];

    initialMatrix.forEach((row, rowIndex) => {
        for (let j = 0; j < row.length; j++) { 
            const pixel = document.createElement('div');
            pixel.classList.add('pixel');
            if (row[j] === '1') {
                pixel.style.backgroundColor = 'black'; 
            }
            container.appendChild(pixel);
        }
    });

    
    const pixels = document.querySelectorAll('.pixel');
    pixels.forEach(pixel => {
        pixel.addEventListener('click', function() {
            if (this.style.backgroundColor === 'black') {
                this.style.backgroundColor = 'white'; 
            } else {
                this.style.backgroundColor = 'black'; 
            }
            updateMatrix();
        });
    });

    function updateMatrix() {
        let matrix = '';
        for (let i = 0; i < numRows; i++) {
            for (let j = 0; j < initialMatrix[i].length; j++) { 
                const index = i * initialMatrix[i].length + j;
                if (index < pixels.length) {
                    const pixel = pixels[index];
                    if (pixel.style.backgroundColor === 'black') {
                        matrix += '1'; 
                    } else {
                        matrix += '0'; 
                    }
                } else {
                    matrix += '0'; t
                }
            }
            matrix += '\n'; 
        }
        console.log(matrix);
    }
    updateMatrix();
});
