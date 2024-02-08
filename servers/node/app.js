import express from 'express';

const app = express();

app.get('/', (req,res) => {
    res.send({ message:'Hello World'});

});

app.post('/postRequest', (req,res) => {
    res.send({ message:'Hello World, this is a POST request'});
});

const PORT = 8080;
app.listen(PORT, () => {
    console.log('Server is running on port', PORT);
});
