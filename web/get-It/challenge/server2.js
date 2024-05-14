const express = require('express')
const app = express()
const path = require('path')

app.use(express.static(path.join(__dirname, 'public')))

app.get('/flag', (req, res) => {
  if (req.headers.referer === 'https://ingeneer-2k24.ingeniums.club:12006/') {
    res.send(`<html>
            <head>
                <title>Flag Second Part </title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>Flag Second Part</h1>
                <p> here is the format of the flag ingeneer{} </p>
                <p> the second part is : ST1k4 </p>
                <p> split two parts by _ </p>
                </div>
            </body>
        </html>
    `)
  } else {
    res.send(`<html>
            <head>
                <title>not this way</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>not this way</h1>
                <p>only request from / of other port </p>
                <img src="not_this_way.gif" style="height: 400px;width: 400px;"  alt=" change your location gif">
                </div>
            </body>
        </html>
    `)
  }
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'))
})

const PORT = 3002
app.listen(PORT, () => {
  console.log(`Server 2 is running on port ${PORT}`)
})
