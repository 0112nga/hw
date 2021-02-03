import React from 'react';

function Joke(props) {
    return <div>
        <h3 style={{display: props.question ? "block" : "none"}}>Question: {props.question}</h3>
        <h3 style={{display: !props.answer && "none"}}>Answer:{props.answer} </h3>
        {/* if answer is null then display none */}
        <br/>
    </div>
}
export default Joke;