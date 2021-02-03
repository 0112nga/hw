import React from 'react';
import Header from './components/Header';
import Greeting from './Greeting';
import TodoItem from './TodoItem';
import todoData from './todoData';
// import Conditional from './Conditional';
// import Product from './Product';
// import products from './ProductData';
// import Joke from './Joke';
// import JokeData from './JokeData';

class App extends React.Component {
    // const JokeComponents = JokeData.map((joke)=> 
    //     <Joke key={joke.id} question={joke.question} answer={joke.answer} />
    // )
    // const ProductComponent = products.map((product)=>
    //     <Product key={product.id} name={product.name} price={product.price} description={product.description}/>
    // )

    constructor(){
        super();
        this.isComponentMounted = false;
        this.state = {
            isComponentMounted : false,
            item: todoData,
            count: 0,
            isLoading: true,
            unReadMessages: [],
            isLogin: false,
            question: []
        }
    }

    //Component life cycles

    //situation : In Home page, when geting data from API then update state, but
    //            do not finish getting data, user click to About page
    //           => component Home is unmounted => return data from API and setState
    //              but component Home khong conf maf update => loi
    //       => solution :use a variable called isComponentMounted to know the status of component  
    //start a component, run once
    //mostly call API 
    // componentDidMount(){
    //     this.isComponentMounted = true;
    //     //get API => async => when await isComponentMounted can change to be False because of user's action 
    //     if(this.isComponentMounted){
    //         //setState
    //     }
    // }
    // componentDidMount(){
    //     setTimeout(()=>{
    //         this.setState({
    //             ...this.state,
    //             isLoading: false
    //         })
    //     },1500)
    // }
    async componentDidMount(){
        this.isComponentMounted = true
        const response = await fetch('https://wpr-quiz-api.herokuapp.com/attempts', {
            method : 'POST',
            headers : {
            'Content-Type': 'application/json'
            }
        });
        const result = await response.json();
        if(this.isComponentMounted){
            this.setState({
                ...this.state,
                question : result.questions
            })
        }
    }

    //clear timeour or interval if use
    //remove event listener
    componentWillUnmount(){
        this.isComponentMounted = false
    }
    //should not use
    componentDidUpdate(){

    }
    

    handleClick = (id) =>{
        // this.setState({
        //     ...this.state,
        //     count: this.state.count +1
        // })
        this.setState({
            item: this.state.item.map((item)=> {
                if(item.id === id ){
                    item.completed = !item.completed;
                }
                return item
            })
        })
    }
    onChange = ()=>{
        this.setState({
            ...this.state,
            isLogin: !this.state.isLogin
        })
    }
    //Conditional rendering :
    // 1. condition ? true statement : false statement
    // 2. && : true && false : if the thing on the left is true => return the thing on the right
    //                         if ------------------------ false --------- nothing
    render(){
        const todoItems = this.state.item.map((data)=> <TodoItem key={data.id} item={data} handleClick={this.handleClick}/>);
        const questionList = this.state.question.map((ques) => <div key={ques._id}>{ques.text}</div>);
        // console.log(this.state.question);
        // const wordDisplay = this.state.isLoggin ? 'in' : 'out';
        return <>
            <Header />
            <Greeting />
            <div className="lists">
                {todoItems}
            </div>
            {/* <div>
                {JokeComponents}
            </div> */}
            {/* <div>
                {ProductComponent}
            </div> */}
            <div style={{textAlign: "center", margin: "30px auto"}}>
                <h2 style={{margin: "20px auto"}}>You are currently logged {this.state.isLogin ? 'in' : 'out'}</h2>
                <button className="btn btn-dark" onClick={this.onChange}>Log {this.state.isLogin ? 'out' : 'in'}</button>
            </div>
            <div style={{textAlign: "center", margin: "30px auto"}}>
                    <h1>{this.state.count}</h1>
                    <button className="btn btn-dark" onClick={this.handleClick}>Change</button>
            </div>
            {/* <div>
                {this.state.isLoading ? <h1>Loading ... </h1> 
                : <Conditional />}
            </div> */}
            <div>
                {this.state.unReadMessages.length > 0 && <h3>You have {this.state.unReadMessages.length} unread messages</h3>}
            </div>
            {this.isComponentMounted ? questionList : <div>Loading....</div>}
            
        </>

    }
}

export default App;