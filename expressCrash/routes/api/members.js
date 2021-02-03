const express = require('express');
const members = require('../../members');
const uuid = require('uuid');
const route = express.Router();

route.get('/', (req, res)=>{
    res.json(members);
});
route.get('/:id', (req, res)=>{
    const found = members.some(member => member.id === parseInt(req.params.id));

    if(found){
        res.json(members.filter(member => member.id === parseInt(req.params.id)));
    }else{
        res.status(400).json({ msg :'member not found'});
    }
});
// create members
route.post('/', (req, res)=>{
    const newMember = {
        id: uuid.v4(),
        name: req.body.name,
        email: req.body.email,
        status: 'active'
    };

    if(!newMember.name || !newMember.email){
        res.status(400).json({ msg: 'Please include name and email'});
    }
    members.push(newMember);
    // res.redirect('/');
});

//update members
route.put('/:id', (req, res)=>{
    const found = members.some(member => member.id === parseInt(req.params.id));

    if(found){
        const updateMember = req.body;
        members.forEach(member => {
            if(member.id === parseInt(req.params.id)){
                member.name = updateMember.name ? updateMember.name : member.name;
                member.email = updateMember.email ? updateMember.email : member.email;

                res.json(members);
            }
        })
    }else{
        res.status(400).json({msg : 'member not found'});
    }

});

//delete member
route.delete('/:id', (req, res)=>{
    const found = members.some(member => member.id === parseInt(req.params.id));

    if(found){
        res.json({msg: 'member deleted ', members : members.filter(member => member.id !== parseInt(req.params.id))});
    }else{
        res.status(400).json({msg: 'member not found'});
    }
})



module.exports = route;