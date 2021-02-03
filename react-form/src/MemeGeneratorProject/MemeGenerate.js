import React from 'react';

class MemeGenerate extends React.Component{
    constructor(){
        super();
        this.isComponentMounted = false;
        this.state = {
            topText: '',
            bottomText: '',
            randomImg : '',
            memes: []
        }
    }
    async componentDidMount(){
        this.isComponentMounted = true;
        //call API
        const response = await fetch("https://api.imgflip.com/get_memes", {
            // "method": "GET",
            // "headers": {
                
            // }
        })
        const result = await response.json();
        if(this.isComponentMounted){
            this.setState({
                ...this.state,
                randomImg:  result.data.memes[0].url,
                memes: result.data.memes
            })
        }
    }
    componentWillUnmount(){
        this.isComponentMounted = false;
    }
    handleChange = (event) =>{
        const {name, value} = event.target;
        this.setState({
            ...this.state,
            [name] : value
        })
    }
    handleClick = (e) =>{
        e.preventDefault();
        const randNum = Math.floor(Math.random()* this.state.memes.length);
        this.setState({
            ...this.state,
            randomImg: this.state.memes[randNum].url
        })
    }
    render(){
        return <div className="container">
            <input type="text" name="topText" placeholder="Top text" value={this.state.topText} onChange={this.handleChange}/>
            <input type="text" name="bottomText" placeholder="Bottom text" value={this.state.bottomText} onChange={this.handleChange}/>
            <input type="button" name="gen" value="gen" onClick={this.handleClick}/>
            <br />
            <p>{this.state.topText}</p>
            <img src={this.state.randomImg} alt="" style={{width: 400, height: 400}}/>
            <br />
            <p>{this.state.bottomText}</p>
        </div>
    }
}
export default MemeGenerate;