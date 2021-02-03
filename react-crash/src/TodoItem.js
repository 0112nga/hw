import React from 'react';

// function TodoItem(props) {
//     return <div className="form-check form-switch todo-item">
//     <input type="checkbox" className="form-check-input" checked={props.item.completed}/>
//     <label className="form-check-label">{props.item.text}</label>
// </div>
// }
// export default TodoItem;

class TodoItem extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            item : []
        }
    }

    // is called right before rendering elements in DOM
    // to set state based on intital props
    static getDerivedStateFromProps(props, state){
        return {item: props.item}
    }
    // shouldComponentUpdate(nextProps, nextState){
    //     //return true if want it to update
    //     //return false if not
    // }

    // //can check the what the value of state and props were before even after update
    // //can think as way to create backup of the current way things are
    // getSnapshotBeforeUpdate(prevProps, prevState){
    //     //prevState.item
    // }
    onChange = () => this.props.handleClick(this.props.item.id);
    render(){
        return <div className="form-check form-switch todo-item">
        <input type="checkbox" className="form-check-input" checked={this.props.item.completed} onChange={this.onChange}/>
        <label style={this.props.item.completed ? {fontStyle: "Italic",color: "#cdcdcd", textDecoration:"line-through"} : null} className="form-check-label">{this.props.item.text}</label>
    </div>
    }
}
export default TodoItem;