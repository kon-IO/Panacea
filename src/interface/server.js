const express = require('express'); 
const cors = require('cors');
const { exec } = require('child_process')

const app = express();
app.use(cors())
 
app.listen(5000, '0.0.0.0', () => {
    console.log("http://0.0.0.0:5000")
});

app.use(express.static(__dirname ))

app.get('/', (req, res) => {
    res.json({
        message: "Server Pinged"
    })
})

app.get('/data', (req, res) => {
    console.log("data started")
    exec("cat > ", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
    res.json({
        message: "Photo Captured from camera 1"
    })
})

// app.get('/camera2', (req, res) => {
//     console.log("captured")
//     res.status(201).json({
//         message: "Photo Captured from camera 2"
//     })
// })