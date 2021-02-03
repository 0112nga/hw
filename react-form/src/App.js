import React from 'react';
import Header from './components/header';

class App extends React.Component {
  constructor(){
    super();
    this.state = {
      firstName: '',
      isFriendly : true,
      gender:'',
      favColor: ''
    }
  }
  handleChange =(event) => {
    const {name, value, type, checked} = event.target;
    type === "checkbox" ? this.setState({[name]: checked}) : this.setState({
        // [event.target.name] : event.target.value
        [name] : value
      })
  }
  render(){
    return <div class="container">
    <Header />
    <form>
      <div className="form-group">
        <label className="form-label">First Name</label>
        <input type="text" name="firstName"placeholder="First name" className="form-control" onChange={this.handleChange}/>
      </div>
      <br/>
      <div className="form-group">
        <label className="form-label">Last Name</label>
        <input type="text" name="lastName"placeholder="Last name" className="form-control" onChange={this.handleChange}/>
      </div>
      <h3>{this.state.firstName} {this.state.lastName}</h3>
      <br />
      {/* in react textarea can be:, and have value */}
      <textarea value={'some thing in here'}/>
      <br />
      {/* check box */}
      <input type="checkbox" checked={this.state.isFriendly} name="isFriendly" onChange={this.handleChange}/> Is friendly?

      {/* radio */}
      <br />
      <input type="radio" checked={this.state.gender === "male"} name="gender" value="male" onChange={this.handleChange}/> Male
      <br />
      <input type="radio" checked={this.state.gender === "female"} name="gender" value="female" onChange={this.handleChange}/> Female
      <br />
      <h3>{`you are ${this.state.gender}`}</h3>
      {/* select box */}
      <label>Your favorite color is : </label>
      <select name="favColor" value={this.state.favColor} onChange={this.handleChange}>
          <option >Choose color</option>
          <option value="blue">blue</option>
          <option value="green">green</option>
          <option value="white">white</option>
          <option value="black">black</option>
          <option value="orange">orange</option>
      </select>
      <div>Your favorite color is : {this.state.favColor}</div>
      <button>Submit</button>
    </form>

    </div>
  }
}

export default App;
