import React from 'react';
import Header from './components/header';
import FormComponent from './FormComponent';

class FormContainer extends React.Component{
    constructor(){
        super();
        this.state = {
            firstName: '',
            lastName: '',
            age: '',
            gender: '',
            location: '',
            isVegan :false,
            isKosher: false,
            isLactoseFree: false
        }
    }
    handleChange = (event) => {
        const {name, value,type, checked} = event.target;
        type === "checkbox" ? this.setState({
            [name] : checked
        }) 
        : this.setState({
            [name] : value
        })
    }
    render(){
        return <div className="container">
            <Header />
            <FormComponent handleChange={this.handleChange}
                        {...this.state}
            />
        </div>
    }
}

export default FormContainer;