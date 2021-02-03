import React from 'react';

function FormComponent(props) {
    return <>
        <form>
            <div className="form-group">
                <label className="form-label">FirstName</label>
                <input type="text" className="form-control" name="firstName" placeholder="First name" value={props.firstName} onChange={props.handleChange} />
            </div>
            <div className="form-group">
                <label className="form-label">Last Name</label>
                <input type="text" className="form-control" name="lastName" placeholder="Last name" value={props.lastName} onChange={props.handleChange} />
            </div>
            <div className="form-group">
                <label className="form-label">Age</label>
                <input type="text" className="form-control" name="age" placeholder="Age" value={props.age} onChange={props.handleChange} />
            </div>
            <div className="form-group">
                <input type="radio" checked={props.gender === 'male'} name="gender" value="male" onChange={props.handleChange} />Male
                    <br />
                <input type="radio" checked={props.gender === 'female'} name="gender" value="female" onChange={props.handleChange} />Female
                    <br />
                <input type="radio" checked={props.gender === 'other'} name="gender" value="other" onChange={props.handleChange} />Other
                    <br />
            </div>
            <div className="form-group">
                <select name="location" value={props.location} onChange={props.handleChange}>
                    <option>-- Choose the location --</option>
                    <option value="Germany">Germany</option>
                    <option value="England">England</option>
                    <option value="America">America</option>
                    <option value="Korea">Korea</option>
                </select>
            </div>
            <div className="form-group">
                <div>
                    <input type="checkbox" name="isVegan" onChange={props.handleChange} checked={props.isVegan} />
                    <label className="form-label">isVegan</label>
                </div>
                <div>
                    <input type="checkbox" name="isKosher" onChange={props.handleChange} checked={props.isKosher} />
                    <label className="form-label">isKosher</label>
                </div>
                <div>
                    <input type="checkbox" name="isLactoseFree" onChange={props.handleChange} checked={props.isLactoseFree} />
                    <label className="form-label">isLactoseFree</label>
                </div>
            </div>
            <br />
            <input type="submit" name="submit" value="submit" className="btn btn-dark" />
        </form>
        <br></br>
        <h1>Entered Information :</h1>
        <p>Your name : {props.firstName} {props.lastName}</p>
        <p>Your age : {props.age}</p>
        <p>Your gender : {props.gender}</p>
        <p>Your location : {props.location}</p>
        <p>Your dietaryRestriction : </p>
        <p>
            isVegan : {props.isVegan ? 'true' : 'false'}
            <br />
                isKosher : {props.isKosher ? 'true' : 'false'}
            <br />
                isLactoseFree : {props.isLactoseFree ? 'true' : 'false'}
        </p>
    </>
}

export default FormComponent;