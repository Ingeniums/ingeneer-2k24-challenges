require('dotenv').config();
const express = require('express');
const app = express();
const path = require('path');

const PORT = 3000;
const FLAG = process.env.FLAG || "ingeniums{something_not}"


const staticPath = path.join(__dirname, '/public');
app.use(express.static(staticPath));

app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  next();
});
// app.use((req, res, next) => {
//   if (req.method === 'GET' && req.originalUrl !== '/index.html') {
//       return res.redirect('/index.html');
//   }
//   next();
// });


const checkApiKey = (req, res, next) => {
    const apiKey = req.headers.apikey; 
    const from = req.headers.from;
    if (apiKey && apiKey === process.env.API_KEY && from && from === 'google-analytics') {
      next();
    } else {
      res.status(401).send('Unauthorized');
    }
  };

app.put('/google-analytics/7f794c03-2ef4-46a2-a409-3857a061e061', checkApiKey, (req, res) => {
  const data = {
    hello : FLAG
  }
    res.status(200).json(data)
})


app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
