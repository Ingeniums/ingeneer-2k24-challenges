require('dotenv').config();
const express = require('express');
const app = express();
const path = require('path');

const PORT = 3000;


const staticPath = path.join(__dirname, '/public');
app.use(express.static(staticPath));




app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
