require('dotenv').config();
const express = require('express');
const app = express();
const path = require('path');

const PORT = 3000;
const FLAG = process.env.FLAG || "ingeniums{something_not}"


const staticPath = path.join(__dirname, '/public');
app.use(express.static(staticPath));

// app.use((req, res, next) => {
//   if (req.method === 'GET' && req.originalUrl !== '/index.html') {
//       return res.redirect('/index.html');
//   }
//   next();
// });





app.put('/7f794c03',  (req, res) => {
    const data = {
      hello : FLAG
    }
      res.status(200).json(data)
  })

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
