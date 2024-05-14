require('dotenv').config()
const express = require('express')
const jwt = require('jsonwebtoken')
const app = express()
const path = require('path')

app.use(express.static(path.join(__dirname, 'public')))

function getTokenFromCookie(cookieHeader, cookieName) {
  const cookies = cookieHeader
  const cookieArray = cookies?.split(';')
  let token = null

  cookieArray?.forEach((cookie) => {
    const parts = cookie.split('=')
    const name = parts[0].trim()
    if (name === cookieName) {
      token = parts[1]
    }
  })

  return token
}

app.use((req, res, next) => {
  if (
    req.headers.referer === 'https://ingeneer-2k24.ingeniums.club:12006/' &&
    !getTokenFromCookie(req.headers.cookie, 'getItJwt')
  ) {
    const user = {
      email: 'ingenner@ingeniums.com',
      name: 'do not worry ,I made it easy for you',
      group: 'Terminus',
    }

    const token = jwt.sign(user, 'engineer')

    res.cookie('getItJwt', token, { httpOnly: true })
  }
  next()
})

app.get('/flag', async (req, res) => {
  if (req.headers.referer === 'https://ingeneer-2k24.ingeniums.club:12006/') {
    const token = getTokenFromCookie(req.headers.cookie, 'getItJwt')

    if (!token) {
      res.send(`<html>
            <head>
                <title>Unauthorized</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>Unknown</h1>
                <p> i can not identify who you are </p>
                  <img src="who_are_you.gif" style="height: 400px;width: 400px;"  alt="unkown person gif">
                </div>
            </body>
        </html>
    `)
    } else {
      try {
        const decoded = jwt.verify(token, 'engineer')
        if (decoded.group === 'The Saviors') {
          res.send(`<html>
            <head>
                <title>Flag First Part </title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>Flag First Part</h1>
                <p> here is the format of the flag ingeneer{} </p>
                <p> the first part is : KhOuy4 </p>
                <p> split two parts by _ </p>
                </div>
            </body>
        </html>
    `)
        } else {
          res.send(`<html>
            <head>
                <title>Access Forbidden</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>Access Forbidden</h1>
                <p>you have to be from the Saviors group to let you in.</p>
                <img src="Saviors.webp" style="height: 400px;width: 400px;"  alt="Saviors logo">
                </div>
            </body>
        </html>
    `)
        }
      } catch (error) {
        res.send(`<html>
            <head>
                <title>Unauthorized</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>Unauthorized</h1>
                <p>you have to be from the Saviors group to let you in.</p>
                <img src="out.gif" style="height: 400px;width: 400px;"  alt=" get out gif">
                </div>
            </body>
        </html>
    `)
      }
    }
  } else {
    res.send(`<html>
            <head>
                <title>not this way</title>
            </head>
            <body>
            <div style="display: flex;align-items: center;justify-content: center;flex-direction: column;" >
                <h1>not this way</h1>
                <p> only request from / </p>
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

const PORT = 3001
app.listen(PORT, () => {
  console.log(`Server 1 is running on port ${PORT}`)
})
