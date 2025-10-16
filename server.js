// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose.connect('mongodb://127.0.0.1:27017/exam_angular', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error(err));

// Schema and Model
const bookSchema = new mongoose.Schema({
  title: String,
  author: String,
  price: Number,
  genre: String,
  available: Boolean
});
const Book = mongoose.model('Book', bookSchema);

// REST API
app.get('/api/books', async (req, res) => {
  const books = await Book.find();
  res.json(books);
});

app.post('/api/books', async (req, res) => {
  const book = new Book(req.body);
  await book.save();
  res.json(book);
});

app.put('/api/books/:id', async (req, res) => {
  const book = await Book.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(book);
});

app.delete('/api/books/:id', async (req, res) => {
  await Book.findByIdAndDelete(req.params.id);
  res.json({ message: 'Deleted successfully' });
});

app.listen(3000, () => console.log('Server running at http://localhost:3000'));
