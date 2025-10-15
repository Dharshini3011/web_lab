var express=require('express');
var mongoose=require('mongoose');

var app=express();
app.use(express.json());
app.use(express.static(__dirname));

mongoose.connect('mongodb://127.0.0.1:27017/employee');

var emp=mongoose.model('Emp',{name:String,role:String});

app.get('/emp',(req,res)=>{
    emp.find()
    .then(doc=>res.send(doc))
    .catch(err=>res.status(500).send(err));
    
    });

    app.post('/emp',(req,res)=>{
        emp.create(req.body)
        .then(doc=>res.send(doc))
    .catch(err=>res.status(500).send(err))

            
    });
    
    app.put('/emp/:id',(req,res)=>{
    emp.findByIdAndUpdate(req.params.id,req.body)
    .then(doc=>res.send(doc))
    .catch(err=>res.status(500).send(err));
});
    app.delete('/emp/:id',(req,res)=>{
        emp.findByIdAndDelete(req.params.id)
    .then(doc=>res.send(doc))
    .catch(err=>res.status(500).send(err));
    });

    
    app.listen(3000,function(){
    console.log("server started at 3000\nRunning at http://localhost:3000/employee.html");
    });
